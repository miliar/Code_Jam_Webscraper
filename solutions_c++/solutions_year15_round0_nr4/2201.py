#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<string>
#define fortodo(i,a,b) for (int i=(a);i<=(b);i++)
using namespace std;
const int maxn=20;
string s[2];
int f[5][5][5],T;

inline void judge(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
}

int main(){
	judge();s[1]="GABRIEL";s[0]="RICHARD";
	fortodo(i,1,4) fortodo(j,1,4) f[1][i][j]=1;
	f[2][1][1]=0;f[2][1][2]=1;f[2][1][3]=0;f[2][1][4]=1;
	f[2][2][1]=1;f[2][2][2]=1;f[2][2][3]=1;f[2][2][4]=1;
	f[2][3][1]=0;f[2][3][2]=1;f[2][3][3]=0;f[2][3][4]=1;
	fortodo(i,1,4) f[2][4][i]=1;
	f[3][1][1]=0;f[3][1][2]=0;f[3][1][3]=0;f[3][1][4]=0;
	f[3][2][1]=0;f[3][2][2]=0;f[3][2][3]=1;f[3][2][4]=0;
	f[3][3][1]=0;f[3][3][2]=1;f[3][3][3]=1;f[3][3][4]=1;
	f[3][4][1]=0;f[3][4][2]=0;f[3][4][3]=1;f[3][4][4]=0;
	f[4][1][1]=0;f[4][1][2]=0;f[4][1][3]=0;f[4][1][4]=0;
	f[4][2][1]=0;f[4][2][2]=0;f[4][2][3]=0;f[4][2][4]=0;
	f[4][3][1]=0;f[4][3][2]=0;f[4][3][3]=0;f[4][3][4]=1;
	f[4][4][1]=0;f[4][4][2]=0;f[4][4][3]=1;f[4][4][4]=1;
		cin>>T;
	fortodo(i,1,T){
		int x,r,c;
		cin>>x>>r>>c;
		cout<<"Case #"<<i<<": "<<s[f[x][r][c]]<<endl;
	}
	return 0;
}

