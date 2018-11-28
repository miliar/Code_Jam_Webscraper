#include<bits/stdc++.h>
using namespace std;

#define sd(a) scanf("%d",&a)
#define ss(a) scanf("%s",&a)
#define sl(a) scanf("%lld",&a)
#define clr(a) memset(a,0,sizeof(a))
#define debug(a) printf("check%d\n",a)
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define ll long long
int a1[30][30];
int a[30][30];
int mark[30];
char s[30];
vector<int> v;
bool g;
void go(int cur,int n)
{
	int i;
	if(cur==n)
		return;
	bool f=0;
	for(i=0;i<n;++i)
	{
		if(mark[i] || a[v[cur]][i]==0)	continue;
		mark[i]=1;
		f=1;
		go(cur+1,n);
		mark[i]=0;
	}
	if(!f)
		g=1;
}
int main()
{
	// freopen("D.in","r",stdin);
	// freopen("D.out","w",stdout);
	int t,n,i,j,k,x;
	sd(t);
	for(int tt=1;tt<=t;tt++)
	{
		sd(n);
		for(i=0;i<n;++i)
		{
			ss(s);
			for(j=0;j<n;++j)
			{
				if(s[j]=='0')
					a1[i][j]=0;
				else
					a1[i][j]=1;
			}
		}
		int minn=1000;
		for(x=0;x<(1<<(n*n));++x)
		{
			int cnt=__builtin_popcount(x);
			bool f=0;
			for(i=0;i<n;++i)
			for(j=0;j<n;++j)
			{
				a[i][j]=a1[i][j];
				if((x&(1<<(i*n+j))) == 0)
					continue;
				if(a[i][j])
					f=1;
				else
					a[i][j]=1;
			}
			if(f)
				continue;
			v.clear();
			for(i=0;i<n;++i)
				v.PB(i);
			g=0;
			do
			{
				clr(mark);
				go(0,n);
			}while(next_permutation(v.begin(),v.end()));
			
			if(!g)
				minn=min(minn,cnt);
		}
		printf("Case #%d: %d\n",tt,minn);
	}
}
