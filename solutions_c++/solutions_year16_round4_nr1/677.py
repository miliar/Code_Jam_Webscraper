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

int s[3],w[3],a[100010],b[100010],c[100010];
char ans[100010];
char d[3];

bool large(int l1,int r1,int l2,int r2)
{
	for (int i=0;i<r1-l1;i++)
	{
		if (d[a[l1+i]]<d[a[l2+i]]) return 0;
		if (d[a[l1+i]]>d[a[l2+i]]) return 1;
	}
	return 0;
}

int main()
{
	#ifndef ONLINE_JUDGE
		freopen("input.txt","r",stdin);
		freopen("output.txt","w",stdout);
	#endif
	int test;read(test);
	d[0]='S';d[1]='P';d[2]='R';
	for (int T=1;T<=test;T++)
	{
		int n;read(n);read(s[2]);read(s[1]);read(s[0]);
		bool ok=0;
		printf("Case #%d: ",T);
		for (int t=0;t<3;t++)
		{
			int l=1;a[l]=t;
			for (int j=1;j<=n;j++)
			{
				for (int k=1;k<=l;k++) b[k]=(a[k]+1)%3;
				for (int k=1;k<=l;k++)
				{
					c[2*k-1]=a[k];c[2*k]=b[k];
				}
				l<<=1;for (int k=1;k<=l;k++) a[k]=c[k];
			}
			memset(w,0,3*sizeof(int));
			for (int k=1;k<=l;k++) w[a[k]]++;
			if (w[1]==s[1]&&w[2]==s[2])
			{
				for (int i=1;i<=n;i++)
				{
					int t=1<<(i-1);
					for (int j=0;j<l;j+=(t<<1))
						if (large(j+1,j+t+1,j+t+1,j+t+t+1))
							for (int k=0;k<t;k++)
								swap(a[k+j+1],a[k+j+1+t]);
				}
				if (!ok)
					for (int i=1;i<=l;i++) ans[i]=d[a[i]];
				bool t=0;
				for (int i=1;i<=l;i++)
				{
					if (ans[i]<d[a[i]]) break;
					if (ans[i]>d[a[i]]) {t=1;break;}
				}
				if (t)
					for (int i=1;i<=l;i++) ans[i]=d[a[i]];
				ok=1;
			}
		}
		if (!ok) 
			puts("IMPOSSIBLE");
		else
		{
			for (int i=1;i<=(1<<n);i++) putchar(ans[i]);
			puts("");
		}
	}
	return 0;
}

