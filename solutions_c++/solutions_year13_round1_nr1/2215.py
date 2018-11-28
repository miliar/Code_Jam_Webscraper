#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<iostream>
using namespace std ;

const long double EPS = 1e-9;
const long double PI = acos(-1.0);


long double strangeSum(long double r,long double n)
{
	long double ret = n*r*r + 4*(n-1)*(n)*(2*(n-1)+1)/6 + 2*r*n*(n-1);
	return ret;
}
long double calculateArea(long long r,long long n)
{
	return strangeSum(r+1,n) - strangeSum(r,n);
}

bool check(long long r,long long n,long long cap)
{
	return calculateArea(r,n) - EPS < cap;
}

int main()
{
	freopen("bull.in","r",stdin);
	freopen("bull.out","w",stdout);
	int c,c2;
	int tests;
	
	//cout << calculateArea(10000000000000000LL,50) << endl;
	
	//while (1);
	scanf("%d",&tests);
	for (int test=1;test<=tests;test++){
		long long r,cap;
		scanf("%lld%lld",&r,&cap);
		long long s = 1,e = 1000000000;
		long long ret;
		while (s<=e){
			long long mid = (s+e)>>1LL;
			if (check(r,mid,cap)){
				ret = mid;
				s = mid + 1;
			}
			else e = mid - 1;
		}
		printf("Case #%d: %lld\n",test,ret);
	}
	return 0;
}
