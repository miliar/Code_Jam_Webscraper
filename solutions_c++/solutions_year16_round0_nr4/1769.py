#include <iostream>

using namespace std;

int main()
{
	int T, test, i;
	long long K, C, S, pow, a;

	cin>>T;
	for (test = 1; test <= T; test++)
	{
		cin>>K>>C>>S;

		cout<<"Case #"<<test<<": ";

		if (K <= S)
		{
			pow = 1LL;
			for(i = 1; i < C; i++)
			{
				pow *= K;
			}

			for (i = 0; i < K; i++)
			{
				cout<<((long long)i*pow)+1LL<<" ";
			}
		}
		else
		{
			cout<<"IMPOSSIBLE";
		}

		cout<<endl;
	}

	return 0;
}
