#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
int main()
{

	freopen("E:\\gcj\\input.in","r",stdin);
	freopen("E:\\gcj\\ouput.txt","w",stdout);
	int T;	
	cin >> T;
	for (int kk=1;kk<=T;++kk)
	{
		long long n,p,m;
		cin >> n >> p;
		m=(1LL<<n);
		long long a1,a2;
		if (p==1)
		{
			a1=a2=0;
		}
		else if (p==m)
		{
			a1=a2=m-1;
		}
		else
		{
			a1=0;
			long long k=m/2;
			long long tmp=p;
			long long x=2;
			while (1)
			{
				if (tmp<=k)
				{
					break;
				}
				else
				{
					a1+=x;
					x*=2;
					tmp-=k;
					k/=2;
				}
			}
			if (a1==1)
			{
				a1=0;
			}
			a2=2;
			k=m/2;
			long long mi=k;
			tmp=p;
			while (1)
			{
				if (tmp>=k)
				{
					break;
				}
				else
				{
					a2*=2;
					k/=2;				
				}
			}
			a2=m-a2;
		}
		printf("Case #%d: %lld %lld\n",kk,a1,a2);
	}
	return 0;
}