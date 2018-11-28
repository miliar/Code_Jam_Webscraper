/*
LANG: C++
ID: fox05711
PROG: b-small.cpp
*/
//==========================================
#include <iostream>
#include <cctype>
#include <map>
#include <set>
#include <sstream>
#include <cstring>
#include <queue>
#include <stack>
#include <vector>
#include <string>
#include <list>
#include <cmath>
#include <algorithm>
#include <set>
#include <fstream>

using namespace std;
int main(){
	ifstream fin("b-small.in");
	ofstream fout("b-small.out");
	int t;
	fin>>t;
	for (int i=0;i<t;i++){
		int n,m;
		int a[10][10];
		fin>>n>>m;
		int mi=100;
		for (int j=0;j<n;j++){
			for (int k=0;k<m;k++){
				fin>>a[j][k];
				mi=(a[j][k]<mi?a[j][k]:mi);
			}
		}
		bool to=true;
		for (int j=0;j<n;j++){
			for (int k=0;k<m;k++){
				if (a[j][k]==mi){
					bool fc=true,fr=true;
					for (int jj=0;jj<n;jj++) 
						if (a[jj][k]!=mi) {fc=false;break;}
					for (int kk=0;kk<m;kk++)
						if (a[j][kk]!=mi) {fr=false;break;}
					if (!fc && !fr) to=false;
				}
			}
		}
		if (to) fout<<"Case #"<<(i+1)<<": YES"<<endl;
		else fout<<"Case #"<<(i+1)<<": NO"<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}
