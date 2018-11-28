#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<iostream>
#include<set>
#include<map>
#include<string>
#include<vector>
using namespace std;
typedef long long lld;
#define X first
#define Y second
#define mp make_pair
#define pb push_back
#define maxn 1000010
lld val[maxn];
lld sum[maxn];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		int n;
		lld p,q,r,s;
		cin >> n >> p >> q >> r >> s;
		for(int i=0;i<n;i++)
			val[i+1]=(p*i+q)%r+s;
		for(int i=0;i<=n+1;i++)
			sum[i]=(1LL)<<60;
		sum[0]=0;
		for(int i=1;i<=n;i++)
			sum[i]=sum[i-1]+val[i];
		lld ans=sum[n];
		int j=1;
		for(int end=1;end<=n;end++)
		{
			while(max(sum[j-1],sum[end]-sum[j-1]) >= max(sum[j],sum[end]-sum[j]))
				j++;
			lld a=sum[j-1];
			lld b=sum[end]-sum[j-1];
			lld c=sum[n]-sum[end];
			lld tmp=max(a,max(b,c));
			ans=min(ans,tmp);
		}
		ans=sum[n]-ans;
		printf("Case #%d: %.12f\n",cc,1.0*ans/sum[n]);
	}
	return 0;
}
/*
8
1 1 1 1 1
10 17 1 7 1
2 100 100 200 1
20 17 3 23 100
10 999999 999999 1000000 1000000
2 1 1 1 1
3 1 99 100 1
999999 1000000 999999 1000000 1000000

1
10 17 1 7 1

 */
