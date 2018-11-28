#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <list>
#include <stack>
#include <set>
#include <map>

using namespace std;

bool is2(long long a)
{
	while (a!=1)
	{
		if (a%2==1)
			return 0;
		a/=2;
	}
	return 1;
}
long long gcd(long long a, long long b)
{
	while (b)
	{
		swap(b,a%=b);
	}	
	return a;
}
void go()
{
	long long p,q;
	char c;
	cin>>p>>c>>q;
	long long g = gcd(p,q);
	p/=g;
	q/=g;
	if (!is2(q))
	{

		cout<<"impossible";
		return;
	}
	int res = 1;
	while (p<q/2)
	{
		q/=2;
		res++;
	}
	cout<<res;
}
int main()
{	
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int cases;
	cin>>cases;
	for (int curcase=1;curcase<=cases;curcase++)
	{
		cout<<"Case #"<<curcase<<": ";
		{
			go();
		}
		cout<<"\n";
	}
	return 0;
}
