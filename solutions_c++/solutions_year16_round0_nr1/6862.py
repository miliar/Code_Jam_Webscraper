#include <iostream>
#include <string.h>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <set>
#include <utility>
#include <stack>
#include <cmath>
#include <cassert>
using namespace std;
typedef long long int ll;

int main(int argc, char const *argv[])
{
	ll t,n;
	cin>>t;
	for (int i = 0; i < t; ++i)
	{
		cin>>n;
		if(n==0)
		{
			cout<<"Case #"<<i+1<<": INSOMNIA\n";
			continue;
		}
		ll bin = 0;
		ll m = 0;
		while(bin != 1023)
		{
			m++;
			ll r = m*n;
			while(r!=0)
			{
				bin = bin | (1<<(r%10));
				r = r/10;
			}
		}
		cout<<"Case #"<<i+1<<": "<<m*n<<"\n";
	}
}
