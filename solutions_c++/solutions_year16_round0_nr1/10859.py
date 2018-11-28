#include <vector>
#include <valarray>
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
	long long t,n,i,j,k,count=0,z,temp,temp1,rem;
    long long check[10];
	scanf("%lld",&t);
	for(i=0;i<t;i++)
	{
		count=0;
		scanf("%lld",&n);
		for(j=0;j<=9;j++)
		{
			check[j]=0;
		}
		if(n==0)
		{
			printf("Case #%lld: INSOMNIA\n",i+1);
			continue;
		}
		z=1;
		while(count!=10)
		{
		 temp1=n*z;
		  temp=temp1;
		    z++;
		while(temp!=0)
		{
			rem=temp%10;
			if(check[rem]==0)
			{
				count++;
			}
			check[rem]=1;
			temp=temp/10;
		}
		if(count==10)
		{
		printf("Case #%lld: %lld\n",i+1,temp1);
		}
		}
	}
	return 0;
}
