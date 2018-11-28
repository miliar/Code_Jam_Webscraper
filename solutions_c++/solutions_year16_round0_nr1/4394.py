#include <iostream>

using namespace std;
int main()
{
	
	int t,n,z,x;
	cin >> t;
	bool a[10],flag;
	for (int a0 = 1; a0 <= t; a0++)
	{
		cin >> n;
		if (n == 0)
		{	
			cout << "Case #" << a0 << ": INSOMNIA" << endl;
			continue;
		}
		for (int i=0;i<=9;i++)
			a[i] = false;

		int q = 1;
		int count = 0;
		while (count != 10)
		{
			x = n * q;
			while (x != 0)
			{
				z = x % 10;
				if (a[z] == false)
				{	
					a[z] = true;
					count++;
				}
				x /= 10;
			}
			q++;
		}

		cout << "Case #" << a0 << ": " << n * (q-1) << endl;
	}

return 0;
}