#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <iomanip>
#include <set>
#include <queue>
#include <utility>
#include <map>
#include <iterator>
#include <cmath>
#include <ctime>
#include <climits>
#include <fstream>

using namespace std;
int t;
ifstream fin;
ofstream fout;
vector < string > v, v1, v2;
vector <long long> s2;
vector < vector < int > > vv1, vv, vv2;
long long ans = 0 ;
const long long mod = 1000000009;
long long n, s, g = 0;
char a, bs;
int flag = 1, minx = mod, sum;
int main(){
	ios_base::sync_with_stdio(false);
	fin.tie(NULL);
	fin.open("A-small-attempt0.in");
	fout.open("ss.txt");
	fin >> t;
	for(int k = 0; k < t; k++){
		minx = mod;
		sum = 0 ;
		ans = 0;
		g= 0;
		flag = 1;
		fout << "Case #" << k+1 << ": ";
		fin >> n;
	    v.resize(n);
		vv.resize(n);
		for(int i = 0; i < n; i++)
			fin >> v[i];
		 v1.resize(n,"");
		for(int i = 0; i < n; i++){
			a = v[i][0];
			g = 1;
			for(int j = 1; j < v[i].size(); j++){
				if(v[i][j] == v[i][j-1])
					g++;
				else {
					v1[i].push_back(a);
					a = v[i][j];
					vv[i].push_back(g);
					g = 1;
				}
			}
			v1[i].push_back(a);
			vv[i].push_back(g);
		}
		for(int i = 1; i < n; i++){
			if(v1[0] != v1[i]){
				fout << "Fegla Won";
				flag  = 0;
			}
		}
	    if(flag){
			for(int i = 0; i < vv[0].size(); i++){
				for(int j = 0; j < vv.size(); j++){
					sum+=vv[j][i],minx = min(minx,vv[j][i]);
				}
			 ans+= sum - (minx*n);
			 sum = 0;
			 minx = mod;
			}
		  fout << ans;
		}
		fout << "\n";
		vv.clear(),v.clear(),v1.clear();
	}
	return 0;
}