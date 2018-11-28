#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <fstream>
using namespace std;
vector <double> v,v2,v1,v3;
int t,n;
int y,z;
int f = 0;
ifstream fin("D-large.in");
ofstream fout("ss.txt");
int main(){
	std::ios_base::sync_with_stdio(false);
	fin.tie(NULL);
	fin >> t;
	for(int l = 0; l < t; l++){
		fin >> n;
		y=0,z=0;
		v.resize(n);
		v2.resize(n);
		for(int i = 0; i < n; i++)
			fin >> v2[i];
		for(int  i = 0; i < n; i++)
			fin >> v[i];
		sort(v.begin(),v.end());
		v3 = v;
		sort(v2.begin(),v2.end());
		v1 = v2;
		for(int i = 0; i < v.size(); i++)
			for(int j = 0;j  < v2.size(); j++){
				if(v2[j] > v[i]){
					y++;
					v2.erase(v2.begin()+j);
					break;
				}
			}
		for(int i =v1.size()-1; i >=0; i--){
			f =0;
			for(int j= 0; j < v3.size(); j++){
				if(v3[j] > v1[i]){
					f = 1;
					v3.erase(v3.begin()+j);
					break;
				}
			}
			if(f!=1){
				z++;
				v3.erase(v3.begin());
			}
		}
		fout << "Case #" << l+1 << ": " << y << " " << z << "\n";
		v1.clear(),v2.clear(),v3.clear(),v.clear();
	}
	return 0;
}