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
		int inp,a;
		int row[4];
		cin >> inp;
		for (int j=1;j<=4;j++)
		{
			for (int i=0;i<4;i++)
				if (j!=inp)
					cin >> a;
				else cin >> row[i];
		}
		cin >> inp;
		int count = 0,latest;
                for (int j=1;j<=4;j++)
                {
                        for (int i=0;i<4;i++)
                                if (j!=inp)
                                        cin >> a;
                                else 
				{
					cin >> a;
					for (int k=0;k<4;k++)
					{
						if (a==row[k])
						{
							count++;
							latest=a;
						}
					}
				}
                }
		cout << "Case #" << i << ": ";
		if (count == 0) cout << "Volunteer cheated!";
		else if (count >= 2) cout << "Bad magician!";
		else cout << latest;
		cout << endl;

	}
	return 0;
}
