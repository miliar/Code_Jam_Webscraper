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
double pi;
int ok(long long _n,long long _r,double t)
{
	double n=_n;
	double r=_r;
	double area=(2*r-3)*n+2*(1+n)*n;
	//area*=pi;
	if (area-1e-10<=t)
	{
		return 1;
	}
	return 0;

}
int main()
{
	
	freopen("E:\\gcj\\input.in","r",stdin);
	freopen("E:\\gcj\\ouput.txt","w",stdout);
	int T;
	pi=acos(-1.0);
	cin >> T;
	for (int kk=1;kk<=T;++kk)
	{
		long long r,t;
		cin >> r >> t;
		long long l=1,h=t,mid;
		long long ans;
		while (l<=h)
		{
			mid=(l+h)/2;
			if (ok(mid,r,t))
			{
				ans=mid;
				l=mid+1;
			}
			else
			{
				h=mid-1;
			}
		}
		printf("Case #%d: %lld\n",kk,ans);
	}
	return 0;
}