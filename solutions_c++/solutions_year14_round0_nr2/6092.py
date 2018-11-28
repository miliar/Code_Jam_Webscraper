#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>

using namespace std;
typedef long long lli;

lli mod_power(lli base, lli exp, lli mod)
{
	base %= mod;
	if (base==0) return 0;
	if ((base%mod) ==1) return 1;
	if (exp == 1) return base%mod;
	if (exp==0) return 1;
	if ((exp&1)) return (base*(mod_power(base*base,exp/2,mod)%mod))%mod;
	return mod_power(base*base,exp/2,mod)%mod;

}


int main()
{
	int t;
	cin >> t;
	for (int i=1;i<=t;i++)
	{
		double c,f,x;
		cin >> c >> f >> x;

		double num = (x/c - 2/f - 1);
		lli n = (int)num;
		if (num < 1 && num >= 0) n = 0;
		else if (num<0) n=-1;
		n++;
		double tottime=0.0;
		for (lli j=0;j<n;j++)
		{
			tottime += c/(2+j*f);
		}
		tottime += x/(2+n*f);
		cout << "Case #" << i;
		printf(": %0.7f\n",tottime);
	}





	return 0;
}
