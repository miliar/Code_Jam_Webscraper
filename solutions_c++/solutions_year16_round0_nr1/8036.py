#include <iostream>
using namespace std;

int main() {
	bool y[10],ok;
	long long a,b,c,d,e,i,j,f,g;
	cin >> a;
	for (i=1;i<=a;i++)
	{
		for (j=0;j<=9;j++)y[j] = false;
		c = 0;
		cin >> b;
		cout << "Case #" << i << ": ";
		if (b ==0) cout << "INSOMNIA\n";
		else
		{
			e = 0;
			ok = false;
			while (true)
			{
				e = e + b;
				d = e;
				while (d > 0 )
				{
					f = d % 10;
					if (!y[f])
					{
						y[f] = true;
						c++;
						if (c == 10)
						{
							ok = true;
							break;
						}
					}
					d = d /10;
				}
				if(ok) break;
			}
			cout << e << "\n";
		}
	}
}