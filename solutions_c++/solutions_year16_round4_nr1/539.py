#include <bits/stdc++.h>
using namespace std;
typedef long long               ll;
const int mod = 1e9+7;
#ifndef M_PI
#define M_PI acos(-1.0)
#endif

int n;

string ord[15][3];
int c[15][3][3];

int main(){
	ord[0][0]="R";
	c[0][0][0]=1;
	ord[0][1]="P";
	c[0][1][1]=1;
	ord[0][2]="S";
	c[0][2][2]=1;
	for(int i=1; i<15; ++i){
		for(int j=0; j<3; ++j){
			if(ord[i-1][j]<ord[i-1][(j+2)%3]){
				ord[i][j]=ord[i-1][j]+ord[i-1][(j+2)%3];
			}
			else{
				ord[i][j]=ord[i-1][(j+2)%3]+ord[i-1][j];
			}
			for(int k=0; k<3; ++k){
				c[i][j][k]=c[i-1][j][k]+c[i-1][(j+2)%3][k];
			}
		}
	}
	int tests;
	cin>>tests;
	for(int ct=0; ct<tests; ++ct){
		int rps[3];
		cin>>n>>rps[0]>>rps[1]>>rps[2];
		string res="X";
		for(int i=0; i<3; ++i){
			bool pos=true;
			for(int j=0; j<3; ++j){
				if(c[n][i][j]!=rps[j]){
					pos=false;
				}
			}
			if(pos){
				res=min(res, ord[n][i]);
			}
		}
		if(res=="X"){
			res="IMPOSSIBLE";
		}
		cout<<"Case #"<<ct+1<<": "<<res<<"\n";
	}
	return 0;
}
