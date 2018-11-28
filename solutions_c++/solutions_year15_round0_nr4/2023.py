#include <bits/stdc++.h>
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
#define ll long long
#define ull unsigned ll
using namespace std;
int ans[4][4][4]={{{1,1,1,1},{1,1,1,1},{1,1,1,1},{1,1,1,1}},{{0,1,0,1},{1,1,1,1},{0,1,0,1},{1,1,1,1}},{{0,0,0,0},{0,0,1,0},{0,1,1,1},{0,0,1,0}},{{0,0,0,0},{0,0,0,0},{0,0,0,1},{0,0,1,1}}};
int main()
{
	freopen("input.txt","r",stdin);//redirects standard input
    freopen("output.txt","w",stdout);//redirects standard output
	int t,j;
	cin>>t;
	for(j=1;j<=t;j++)
	{
		int x,r,c;
		cin>>x>>r>>c;
		cout<<"Case #"<<j<<": ";
		if(ans[x-1][r-1][c-1])
			cout<<"GABRIEL"<<endl;
		else
			cout<<"RICHARD"<<endl;			
	}
	return 0;
}