#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
using namespace std;


int main()
{
	freopen("A-small-practice.in","rt",stdin);
	freopen("aout.out","wt",stdout);
	long long t,n,a[11];
	long long i,sum,tmp,r,j;
	scanf("%lld",&t);
	for(j=1;j<=t;j++)
	{
		printf("Case #%lld: ",j);
		r=0;
		for(i=0;i<10;i++)
		{
			a[i]=0;
		}
		scanf("%lld",&n);
		if(n==0)
		{
			printf("INSOMNIA\n");
		}
		else
		{
			for(sum=n;r!=10;sum+=n)
			{
				tmp=sum;
				while(tmp!=0)
				{
					if(a[tmp%10]==0)
					{
						a[tmp%10]=1;
						r++;
					}
					tmp=tmp/10;
				}
			}
			printf("%lld\n",sum-n);
		}
	}
	return 0;
}
