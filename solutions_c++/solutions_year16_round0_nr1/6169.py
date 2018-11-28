#include <bits/stdc++.h>

using namespace std;

int main()
{
	freopen("ALarge.in","r",stdin);
    freopen("Output2.out","w",stdout);
	unsigned long long t;	cin >> t;
	for(unsigned long long k=1 ; k<=t ; k++)
	{
		set<unsigned long long>num;
		unsigned long long n,i=0;	cin >> n;
		while(n)
		{
			i++;
			unsigned long long z=n*i;
			while(z>0)
			{
				num.insert(z%10);
				z/=10;
			}
			if(num.size()==10)	break;
		}
		cout << "Case #" << k << ": ";
		if(num.size()==0)	cout << "INSOMNIA" << endl;
		else cout << n*i << endl;
	}
}
