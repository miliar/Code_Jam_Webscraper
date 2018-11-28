#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<iostream>
#include<map>
#include<string>
#include<vector>
using namespace std;
typedef long long lld;
#define pb push_back
#define mp make_pair
#define X first
#define Y second
int s[100010];
map<int,int>f;
map<int,int>::iterator ll;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		f.clear();
		int n;
		scanf("%d",&n);
		for(int i=1;i<=n;i++)
		{
			scanf("%d",&s[i]);
			f[s[i]]=1;
		}
		int T=0;
		for(ll=f.begin();ll != f.end();ll++)
			ll->Y=++T;
		for(int i=1;i<=n;i++)
			s[i]=f[s[i]];
		int l=1;
		int r=n;
		int ans=0;
		for(int t=1;t<=n;t++)
		{
			int at=-1;
			for(int i=l;i<=r;i++)
				if(s[i] == t)
				{
					at=i;
					break;
				}
			if(at == -1)
			{
				while(1);
			}
			int dl=at-l;
			int dr=r-at;
			ans+=min(dl,dr);
			if(dl < dr)
			{
				for(int i=at;i>l;i--)
					swap(s[i],s[i-1]);
				l++;
			}
			else
			{
				for(int i=at;i<r;i++)
					swap(s[i],s[i+1]);
				r--;
			}
		}
		printf("Case #%d: %d\n",cc,ans);
	}
	return 0;
}
/*
2
3
1 2 3
5
1 8 10 3 7

1
8
3 1 8 7 6 5 4 2

 */
