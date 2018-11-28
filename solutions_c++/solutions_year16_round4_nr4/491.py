#include <set>
#include <map>
#include <cmath>
#include <cstdio>
#include <vector>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

#define pb push_back
#define mp make_pair
#define x first
#define y second

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<pii> vpii;

template <class T>
void read(T &x)
{
	char ch;
	for (ch=getchar();(ch<'0'||ch>'9')&&ch!='-';) ch=getchar();
	x=0;int t=1;if (ch=='-') {ch=getchar();t=-1;}
	for (;ch>='0'&&ch<='9';ch=getchar()) x=x*10+ch-'0';
	x*=t;
}

char a[4][4];
bool b[4][4];
int n,q[100000][2];
bool v[16][16];

int calc(int x)
{
	for (int i=0;i<n;i++)
		for (int j=0;j<n;j++)
			if (x&(1<<(i*n+j))) b[i][j]=1; else b[i][j]=0;
	for (int i=0;i<n;i++)
		for (int j=0;j<n;j++)
			if (a[i][j]=='1'&&b[i][j]==0) return n*n;
	int f=1,r=1;q[1][0]=0;q[1][1]=0;
	memset(v,0,sizeof(v));
	while (1)
	{
		int x=q[f][0],y=q[f][1];f++;
		if (x==(1<<n)-1) break;
		for (int i=0;i<n;i++)
			if (!(x&(1<<i)))
			{
				bool ok=0;
				for (int j=0;j<n;j++)
					if ((!(y&(1<<j)))&&b[i][j])
					{
						ok=1;
						int tx=x|(1<<i),ty=y|(1<<j);
						if (!v[tx][ty]) {v[tx][ty]=1;q[++r][0]=tx;q[r][1]=ty;}
					}
				if (!ok) return n*n;
			}
	}
	int s=0;
	for (int i=0;i<n;i++)
		for (int j=0;j<n;j++)
			if (a[i][j]=='0'&&b[i][j]==1) s++;
	return s;
}

int main()
{
	#ifndef ONLINE_JUDGE
		freopen("input.txt","r",stdin);
		freopen("output.txt","w",stdout);
	#endif
	int test;scanf("%d",&test);
	for (int T=1;T<=test;T++)
	{
		scanf("%d",&n);
		for (int i=0;i<n;i++) scanf("%s",a[i]);
		int ans=n*n;
		for (int i=0;i<(1<<(n*n));i++) ans=min(ans,calc(i));
		printf("Case #%d: %d\n",T,ans);
	}
	return 0;
}

