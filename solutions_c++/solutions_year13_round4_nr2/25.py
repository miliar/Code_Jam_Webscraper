#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <sstream>

using namespace std;

const int maxn=50010;

int n;
long long P;
long long f1(long long k)
{
	long long ans=0;
	int p=n-1;
	k--;
	while(k)
	{
		ans|=(1ll<<p);
		p--;
		k=(k-1)/2;
	}
	return ans;
}
long long f2(long long k)
{
	long long ans=(1ll<<n)-1;
	int p=n-1;
	k=(1ll<<n)-k;

	while(k)
	{
		ans^=(1ll<<p);
		p--;
		k=(k-1)/2;
	}
	return ans;
}
int main()
{
	int T,ii=0;
	freopen("B-large.in","r",stdin);
	freopen("B1.out","w",stdout);
	
	cin>>T;
	for(ii=1;ii<=T;ii++)
	{
		cin>>n>>P;

		printf("Case #%d: ",ii);
		long long l=1,r=(1ll<<n),mid;

		while(l<r)
		{
			mid=(l+r+1)/2;
			if(f1(mid)>=P)
				r=mid-1;
			else
				l=mid;
		}
		cout<<l-1;
		printf(" ");
		l=1,r=(1ll<<n),mid;
		while(l<r)
		{
			mid=(l+r+1)/2;
			if(f2(mid)>=P)
				r=mid-1;
			else
				l=mid;
		}
		cout<<l-1<<endl;
	}
}