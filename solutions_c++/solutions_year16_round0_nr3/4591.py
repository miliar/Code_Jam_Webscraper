#include <iostream>
#include <vector>

using namespace std;

int T;

long long interpreta(long long jam, long long base)
{
	long long res = 0;
	long long a = 2;
	while(a<jam)
		a*=10;
	a/=2;
	while(a!=0)
	{
		res *= base;
		res += (jam/a)%10;
		a /= 10;
	}
	/*while(jam!=0)
	{
		res *= base;
		res += jam%10;
		jam /= 10;
	}*/
	return res;
}

long long pow(long long a, long long b)
{
	if(b==0)
		return 1;
	if(b==1)
		return a;
	long long res = pow(a,b/2);
	res *= res;
	if(b%2)
		res *= a;
	return res;
}

long long calculajam(long long n,long long asdf)
{
	long long res = 1;
	for(int i=0;i<n-2;i++)
	{
		res*=10;
		res += asdf&1;
		asdf /= 2;
	}
	res *=10;
	res++;
	return res;
}

int main()
{
	cin >> T;
	for(int i=0;i<T;i++)
	{
		long long n,j;
		cin >> n >> j;
		long long conseguidas = 0;
		long long asdf = 0;
		cout << "Case #" << i+1 << ":" << endl;
		while(conseguidas<j)
		{
			long long jam = calculajam(n,asdf);
			//cout << jam << endl;
			vector<int> v;
			for(int ii=2;ii<=10;ii++)
			{
				long long pr = interpreta(jam,ii);
				//cout << pr << endl;
				if(pr%2==0)
				{
					v.push_back(2);
					continue;
				}
				else
				{
					for(long long k=3;k*k<=pr;k+=2)
					{
						if(pr%k==0)
						{
							v.push_back(k);
							break;
						}
					}
				}
			}
			//while(true);
			if(v.size()==9)
				{
					cout << jam;
					for(int j=0;j<9;j++)
						cout << " " << v[j];
					cout << endl;
					conseguidas++;
				}
			asdf++;
		}
	}
}
