#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <deque>
#include <iterator>	
#include <list>
#include <map>
#include <memory>
#include <numeric>
#include <queue>
#include <set>	
#include <stack>
#include <utility>
#include <sstream>
#include <string>

using namespace std;

const int IX[]={1,0,-1,0,1,1,-1,-1};
const int IY[]={0,1,0,-1,-1,1,1,-1};
const int MAXN=10000000;

int DAT,n,m,t[20],ans;
long long b[MAXN+3],i,j,k;

bool pa(long long a)
{
	int n=0;
	while (a)
	{
		t[++n]=a%10;
		a/=10;
	}
	for (int i=1;i<=n;i++)
		if (t[i]!=t[n-i+1]) return false;
	return true;
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	m=0;
	b[0]=0;
	for (i=1;i<=MAXN;i++)
	{
		if (pa(i)&&pa(i*i))
			b[++m]=i*i;
	}
	scanf("%d",&DAT);
	for (int cas=1;cas<=DAT;cas++)
	{
		ans=0;
		cin>>i>>j;
		for (n=1;n<=m;n++)
			if (b[n]<=j && b[n]>=i) ++ans;
		printf("Case #%d: %d\n",cas,ans);
	}
	return 0;
}
