#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;

ll isPrime(ll n)
{
	ll i, fl;
	fl=0;

	for(i=2; i<sqrt(n); i++)
	{
		if(n%i==0)
		{
			fl = 1;
			return i;
		}
	}
	if(fl==0)
		return -1;

}

int main()
{
	ll n, i, f, g, w, j, b, flag, Count, base, num, k;
	ll result[15], output[20];

	cin>>w;
	cin>>f>>g;
	j=50;
	cout<<"Case #1:"<<endl;
	for(n=0; n<pow(2, 14); n++)
	{
		flag = 0;
		Count=0;
		for(base=2; base<=10; base++)
		{
			k=base;
			b = n;
			num = pow(k, 15) + 1;
			while(b)
			{
				if(b&1)
					num += k;

				b=b/2;
				k *= base;
			}

			k = isPrime(num);
		//	cout<<num<<endl;
			if(k==-1)
			{
				flag=1;
				break;
			}
			else
				result[base] = k;
		}

		if(flag!=1)
		{
			b= n;
			cout<<"1";
			for(i=0; i<14; i++)
			{
				output[i]=(b&1);
				b = b/2;
			}
			for(i=13; i>=0; i--)
				cout<<output[i];
			cout<<"1 ";

			for(i=2; i<10; i++)
				cout<<result[i]<<" ";
			cout<<result[10]<<endl;
			j--;

		}

		if(j==0)
			break;
	}
	return 0;
}