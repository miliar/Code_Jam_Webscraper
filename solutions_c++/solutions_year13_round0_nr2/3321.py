#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<fstream>
#include<string>
#include<cstring>
#include<vector>
#include<list>
#include<map>
#define lli long long int
using namespace std;
int main() {
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	int t,A[100][100],r[100],c[100];
	fin>>t;

	int n,m,yes;
	for(int k=1;k<=t;k++) {
		yes=1;
		fin>>n;fin>>m;
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
				fin>>A[i][j];

		for(int i=0;i<n;i++) {
			r[i]=0;
			for(int j=0;j<m;j++) {
				r[i]=max(r[i],A[i][j]);
				}
			}

		for(int j=0;j<m;j++) {
			c[j]=0;
			for(int i=0;i<n;i++)
				c[j]=max(c[j],A[i][j]);
			}
		for(int i=0;i<n;i++) {
			for(int j=0;j<m;j++) {
				if(A[i][j]!=min(r[i],c[j])) {
					yes=0;
					break;
					}
				}
			}


		if(yes==1)
			fout<<"Case #"<<k<<": YES"<<endl;
		else
			fout<<"Case #"<<k<<": NO"<<endl;
		}

	return 0;
	}
