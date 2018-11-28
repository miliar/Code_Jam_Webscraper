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
long long a,b,l;
int flag = 1, minx = mod, sum;
vector <int> lol;
long long modl (long long a);
int main(){
	ios_base::sync_with_stdio(false);
	fin.tie(NULL);
	fin.open("B-small-attempt0.in");
	fout.open("ss.txt");
	fin >> t;
	for(int k = 0; k < t; k++){
		fout << "Case #" << k+1 << ": ";
		fin >> a >> b >> l;
		ans = 0;
		for(int i = 0; i < a; i++)
			for(int j = 0;j < b; j++)
				if((i&j) < l)
					ans++;
		fout << ans << "\n";
	}
	return 0;
}
long long modl (long long a){
	if(a > 0)
		return a;
	else return -a;
}