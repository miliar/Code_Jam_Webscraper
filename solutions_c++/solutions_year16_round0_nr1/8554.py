#include <iostream>
#include <set>

using namespace std;

typedef long long int ll;

set < int > digitos;

void dragao(ll n)
{
	while(n>=10)
	{
		digitos.insert(n%10);
		n/=10;
	}
	digitos.insert(n);
}

int main()
{
	ios::sync_with_stdio(false);

	int t=0, t0=0;
	cin>>t;

	while(t0<t)
	{
		ll n=0;
		cin>>n;

		digitos.clear();

		int ultimo=0;

		for(ll i=1; i<=10000; i++)
		{
			dragao(i*n);
			if(digitos.size()==10)
			{
				ultimo=i;
				break;
			}
		}

		cout<<"Case #"<<t0+1<<": ";
		if(ultimo==0)	cout<<"INSOMNIA"<<endl;
		else cout<<n*ultimo<<endl;

		t0++;
	}

	return 0;
}
