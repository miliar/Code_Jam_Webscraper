#include<iostream>

using namespace std;

int main()
{
	int t,n;
	cin >> t;
	for (int i=1; i<=t; i++)
	{
		cin >> n;
		cout << "Case #" << i << ": ";
		if (n==0)
			cout << "INSOMNIA"<< endl;
		else
		{
			int count[10], ans=n, c=0, rem, ctr = n;
			for (int j=0; j<10; j++)
				count[j] = 0;
			while (1)
			{
				while (n>0)
				{
					rem = n%10;
					if (!count[rem])
					{
						count[rem] = 1;
						c++;
					
					}
					n = n/10;
				}
				if (c == 10)
				{
					cout << ans << endl;
					break;
				}
				ans += ctr;
				n = ans;
			}
		}
	}
}
