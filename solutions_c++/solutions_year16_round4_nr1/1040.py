#include <bits/stdc++.h>
/*
#include<stdio.h>
#include<iostream>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<map>
#include<set>
#include<vector>
#include<string>
#include<complex>
*/
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef complex<double> cplx;

#define sqr(x) ((x)*(x))
#define pb push_back
#define X first
#define Y second
#define sit(a) set<a>::iterator
#define mit(a,b) map<a,b>::iterator

const ll mod=1000000007LL;
const int inf=0x3f3f3f3f;
const int maxn=100005,maxm=1005;
const double eps=1e-10;
const double pi=acos(-1.0);

int T;

int n,r,p,s;
int x[15][3];
string c[2];

void solve()
{
	int i,j,k;
	x[0][0]=r,x[0][1]=p,x[0][2]=s;
	for(i=1;i<=n;i++)
	{
		int t=1<<(n-i+1);
		x[i][0]=t/2-x[i-1][1];
		x[i][1]=t/2-x[i-1][2];
		x[i][2]=t/2-x[i-1][0];
		for(j=0;j<3;j++) if(x[i][j]<0||x[i][j]>x[i-1][j]) {printf("IMPOSSIBLE\n");return;}
	}
	if(x[n][2]) c[0]="S";
	else if(x[n][1]) c[0]="P";
	else c[0]="R";
	int cur=0;
	for(i=n-1;i>=0;i--)
	{
		int ct=!cur;
		c[ct]="";
		int l=c[cur].length();
		for(j=0;j<l;j++)
		{
			if(c[cur][j]=='P') c[ct]=c[ct]+"PR";
			else if(c[cur][j]=='R') c[ct]=c[ct]+"RS";
			else c[ct]=c[ct]+"PS";
		}
		cur=ct;
	}
	for(int l=1;l<=(1<<(n-1));l<<=1)
	{
		for(i=0;i<(1<<n);i+=l*2)
		{
			if(c[cur].substr(i,i+l)>c[cur].substr(i+l,i+2*l))
			{
				for(j=0;j<l;j++) swap(c[cur][j+i],c[cur][j+i+l]);
			}
		}
	}
	cout<<c[cur]<<"\n";
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for(int ca=1;ca<=T;ca++)
	{
		printf("Case #%d: ",ca);
		scanf("%d %d %d %d",&n,&r,&p,&s);
		solve();
	}
	return 0;
}
