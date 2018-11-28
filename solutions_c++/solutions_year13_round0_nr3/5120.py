#include <cstdio>
#include <vector>
#include <algorithm>
#define all(qw) qw.begin(),qw.end()
using namespace std;
vector <long long> vec;
bool isPal(long long k)
{
	int ar[123];
	int i;
	int n;
	for(n=0;k;n++)
	{
		ar[n]=k%10;
		k/=10;
	}
	for(i=0;i<n;i++)
	{
		if(ar[i]!=ar[n-i-1]) return 0;
	}
	return 1;
}
int main()
{
	long long i;
	for(i=1;i<=10000000;i++)
	{
		if(isPal(i) && isPal(i*i))
		{
			vec.push_back(i*i);
		}
	}
	int Test,tt;
	long long a,b;
	scanf(" %d",&Test);
	for(tt=1;tt<=Test;tt++)
	{
		printf("Case #%d: ",tt);
		scanf(" %lld %lld",&a,&b);
		printf("%d\n",int(upper_bound(all(vec),b)-lower_bound(all(vec),a)));
	}
	return 0;
}
