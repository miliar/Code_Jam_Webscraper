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

long long n;
long long d[17];
void go()
{
	cin>>n;
	d[0]=1;
	for (int i=1;i<=16;i++)
		d[i]=10*d[i-1];
	long long res = 0;
	if (n%10==0)
	{
		n--;
		res++;
	}
	while (n)
	{
		vector<long long> state;
		long long cn = n;
		while (cn)
		{
			state.push_back(cn%10);
			cn/=10;
		}
		int q = state.size();
		if (q==1)
		{
			res+=state[0];
			break;
		}
		int l = 0;
		long long first = 0;
		bool c = q%2;
		for (int i=q-1;i>=(q/2+c);i--)
		{
			first += state[i]*d[l++];
		}
		if (first != 1)
		{
			res+=first;
			res++;
		}
		for (int i=0;i<(q/2+c);i++)
		{
			res += state[i]*d[i];
		}
		if (first == 1)
			res++;
		n = 0;
		for (int i=0;i<q-1;i++)
		{
			n += 9 * d[i];
		}
	}
	cout<<res;
}
int main()
{	
	freopen("A-large(1).in","r",stdin);
	freopen("2.out","w",stdout);
	int cases;
	cin>>cases;
	for (int curcase=1;curcase<=cases;curcase++)
	{
		cout<<"Case #"<<curcase<<": ";
		{
			go();
		}
		if (curcase!=cases)
			cout<<"\n";
	}
	return 0;
}
