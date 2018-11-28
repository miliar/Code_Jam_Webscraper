#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<queue>
#include<set>
#include<vector>
#include<map>
#include<deque>
#include<cstdlib>
#include<functional>
#include<utility>
#include<ctime>
#include<sstream>
#define pb push_back
#define mp make_pair
#define fr(i,n) for(int i=0;i<n;++i)
#define fn(i,n) for(int i=n-1;i>=0;--i)
#define fe(i,a) for(__typeof(a.begin()) i=a.begin();i!=a.end();++i)
using namespace std;
typedef long long LL;
typedef long double LD;
typedef pair<int,int> pii;
int test,n,ans,m,a[100100];

int main()
{
	scanf("%d",&test);
	for (int t=1;t<=test;t++)
	{
		ans=0;
		scanf("%d%d",&n,&m);
		for (int i=0;i<n;i++) scanf("%d",a+i);
		sort(a,a+n);
		for (int l=0,r=n-1;l<=r;++ans)
			if (a[r]+a[l]<=m)
				r--,l++;
			else
				r--;
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
