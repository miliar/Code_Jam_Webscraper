#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	cin>>t;
	for (int k = 1; k <= t; ++k)
	{
		long long n;
		cin>>n;
		int v[10];
		for (int i = 0; i < 10; ++i)
		{
			v[i] = 0;
		}
		if(n == 0)
		{
			cout<<"Case #"<<k<<": INSOMNIA"<<endl;
		}
		else
		{
			int j = 0;
			bool g = true;
			while(g)
			{
				j++;
				long long prueba = n*j;
				while(prueba>0)
				{
					int d = prueba%10;
					v[d] ++;
					prueba=prueba/10;
				}
				bool h =true;
				for(int i = 0 ; i < 10; i++)
				{
					if(v[i]>0)
					{
						h = h & true;
					}
					else
					{
						h = h & false;
					}
				}
				if(h == true)
				{
					g = false;
				}
			}
			cout<<"Case #"<<k<<": "<<n*j<<endl;
		}
	}
	return 0;
}