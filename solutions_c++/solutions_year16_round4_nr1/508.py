#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

int n,r,p,s;
string f[15][5]; // P=0; S=1; R=2;

string solve( int n, int w){
	if (f[n][w]!="") return f[n][w];
	if (n==1){
		if (w==0) return "PR";
		if (w==1) return "PS";
		if (w==2) return "RS";
	}
	string t1=solve(n-1,w);
	string t2=solve(n-1,(w+1)%3);
	string s1=t1+t2, s2=t2+t1;
	if (s1<s2) f[n][w]=s1; else f[n][w]=s2;
	return f[n][w];
}

void prepare(){
	for (int i=1; i<15; ++i)
		for (int j=0; j<3; ++j)
			f[i][j]=solve(i,j);
}

int check( int a, int b ){
	int x,y,z;
	x=y=z=0;
	for (int i=0; i<f[a][b].size(); ++i){
		if (f[a][b][i]=='P') ++x;
		if (f[a][b][i]=='R') ++y;
		if (f[a][b][i]=='S') ++z;
	}
	//cout<<f[a][b]<<" "<<x<<" "<<y<<" "<<z<<" "<<p<<" "<<r<<" "<<s<<endl;
	return x==p && y==r && z==s;
}

int main(){
	prepare();
	int T=0;
	scanf("%d", &T);
	for (int t=1; t<=T; ++t){
		scanf("%d%d%d%d", &n,&r,&p,&s);
		cout<<"Case #"<<t<<": ";
		string ans="";
		if ( check(n,0) ) ans=f[n][0];
		if ( check(n,1) && ( ans=="" || f[n][1]<ans )) ans=f[n][1];
		if ( check(n,2) && ( ans=="" || f[n][2]<ans )) ans=f[n][2];
		if (ans=="") ans="IMPOSSIBLE";
		cout<<ans<<endl;
	}
}

