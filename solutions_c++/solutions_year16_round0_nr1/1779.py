#include <iostream>
#include <cstring>

using namespace std;

int main()
{
	int T, test, N, a, b, count;
	bool was[10];

	cin>>T;

	for (test = 1; test <= T; test++)
	{
		cin>>N;

		if (N)
		{
			memset(was, false, sizeof(was));
			a = N;
			count = 0;

			while (1)
			{
				b = a;
				do
				{
					if (!was[b%10])
					{
						was[b%10] = true;
						count++;
					}
					b /= 10;
				}
				while (b);

				if (count < 10)
				{
					a += N;
				}
				else
				{
					break;
				}
			}

			cout<<"Case #"<<test<<": "<<a<<endl;
		}
		else
		{
			cout<<"Case #"<<test<<": "<<"INSOMNIA"<<endl;
		}
	}

	return 0;
}
