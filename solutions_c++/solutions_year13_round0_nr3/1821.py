#include <cstdio>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <sstream>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#define pb push_back
#define mp make_pair
#define ST begin()
#define ED end()
#define XX first
#define YY second
#define elif else if 
#define foreach(i,x) for (__typeof((x).ST) i=(x).ST;i!=(x).ED;++i) 
using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vci;
typedef vector<string> vcs;
typedef pair<int,int> PII;

const int N = 105;

char a[100];
ll b[N];


//int f[N][20], g[N][20][2];

int check(ll x)
{
	sprintf(a, "%I64d", x);
	int n=strlen(a);
	for (int i=0;i+i<n;++i)
		if (a[i]!=a[n-1-i])
			return 0;
	return 1;
}
/*
int pre(int n, int m, int z)
{	
	memset(f, 0, sizeof f);
	f[0][0]=1;
	for (int i=0;i<n;++i)
		for (int j=0;j<=m;++j) if (f[i][j])
			for (int k=0;k*k*2+j<=m;++k)
				f[i+1][j+k*k*2]+=f[i][j];
	int s=0;
	for (int j=0;j<=m;++j)
		s+=f[n][j];
	return s;
}

int p2(int n, int m, int z)
{
	if (n==1)
		return (m>=9)+(m>=4)+(m>=1);
	if (z)
	{
		if (n<2)
			return 0;
		else
			return p2(n-2,m-2,0)+p2(n-2,m-8,0);
	}
	if (g[n][m][z]!=-1)
		return g[n][m][z];
	if (n&1)
	{
		return g[n][m][z]=pre(n/2,m,z)+pre(n/2,m-1,z)+pre(n/2,m-4,z);
	} else
		return g[n][m][z]=pre(n/2,m,z);
}

int calc()
{
	int n=strlen(a);
	if (n==1)
	{
		return (a[0]>='9')+(a[0]>='4')+(a[0]>='1');
	}
	int s=0;
	for (int i=1;i<n;++i)
		s+=p2(i,9,1);
	if (strcmp(a, "101")==0)
	{
		s=s+s-s;
		s=s-s+s;
	}
	for (int i=1,j=9,k;k=a[i-1]-'0',i+i-1<=n;++i)
	{
		int z=1+(i+i-1<n), zz=n-i-i+(i+i-1==n);
		for (int x=(i==1);x<k&&x*x*z<=j;++x)
			s+=p2(zz,j-x*x*z,0);
		j-=k*k*z;
		if (j<0) break;
	}
	int x=0;
	++s;
	for (int i=0;i+i<n;++i)
	{
		x+=(a[i]-'0')*(a[i]-'0')*2;
		if (a[i]>a[n-1-i])
		{
			x=10;
			break;
		}
	}
	s-=x>9;
	return s;
}
*/
int main()
{
	freopen("C-large-1.in","r",stdin);
	freopen("output.txt","w",stdout);

	int t=0;
	for (ll i=1;i<=10000000;++i)
	{
		if (check(i) && check(i*i))
			b[++t]=i*i;
	}
	/*
	memset(g,-1,sizeof g);
	for (int i=1;i<=1000;++i)
	{
		sprintf(a, "%d", i);
		printf("%d : %d\n", i, calc());
	}*/
	int task;
	scanf("%d", &task);
	for (int _i=1;_i<=task;++_i)
	{
		/*
		scanf("%s", a);
		int n=strlen(a);
		for (int i=n-1;i;--i)
			if (a[i]>'0')
			{
				--a[i];
				break;
			} else
				a[i]='0';
		int ans=-calc();
		scanf("%s", a);
		ans+=calc();
		printf("%d\n", ans);
		*/
		ll l,r;
		cin>>l>>r;
		int ans=0;
		for (int i=1;i<=t;++i)
			if (b[i]>=l&&b[i]<=r)
				++ans;
		printf("Case #%d: %d\n", _i, ans);
	}

	return 0;
}
