#include <iostream>
#include <cstdio>

using namespace std;

void wypisz(int h, int a)
{
	if(a == 1)
		cout << "Case #" << h << ": " << "RICHARD" << "\n";
	else
		cout << "Case #" << h << ": " << "GABRIEL" << "\n";
}

int main()
{
	int v;
	cin >> v;
	for(int h = 1 ; h <= v ; h++)
	{
		int x, a , b;
		cin >> x >> a >> b;
		//cout << " " << a << " " << b << " " << x << "\n";
		if(a > b)
			swap(a, b);

		if(a == 1 && b == 1)
		{
			if(x == 1)
			{
				wypisz(h, 2);
				continue;
			}
			if(x == 2)
			{
				wypisz(h, 1);
				continue;
			}
			if(x == 3)
			{
				wypisz(h, 1);
				continue;
			}
			if(x == 4)
			{
				wypisz(h, 1);
				continue;
			}
		}
		if(a == 1 && b == 2)
		{
			if(x == 1)
			{
				wypisz(h, 2);
				continue;
			}
			if(x == 2)
			{
				wypisz(h, 2);
				continue;
			}
			if(x == 3)
			{
				wypisz(h, 1);
				continue;
			}
			if(x == 4)
			{
				wypisz(h, 1);
				continue;
			}
		}
		if(a == 1 && b == 3)
		{
			if(x == 1)
			{
				wypisz(h, 2);
				continue;
			}
			if(x == 2)
			{
				wypisz(h, 1);
				continue;
			}
			if(x == 3)
			{
				wypisz(h, 1);
				continue;
			}
			if(x == 4)
			{
				wypisz(h, 1);
				continue;
			}
		}
		if(a == 1 && b == 4)
		{
			if(x == 1)
			{
				wypisz(h, 2);
				continue;
			}
			if(x == 2)
			{
				wypisz(h, 2);
				continue;
			}
			if(x == 3)
			{
				wypisz(h, 1);
				continue;
			}
			if(x == 4)
			{
				wypisz(h, 1);
				continue;
			}
		}
		////// 2
		if(a == 2 && b == 2)
		{
			if(x == 1)
			{
				wypisz(h, 2);
				continue;
			}
			if(x == 2)
			{
				wypisz(h, 2);
				continue;
			}
			if(x == 3)
			{
				wypisz(h, 1);
				continue;
			}
			if(x == 4)
			{
				wypisz(h, 1);
				continue;
			}
		}
		if(a == 2 && b == 3)
		{
			if(x == 1)
			{
				wypisz(h, 2);
				continue;
			}
			if(x == 2)
			{
				wypisz(h, 2);
				continue;
			}
			if(x == 3)
			{
				wypisz(h, 2);
				continue;
			}
			if(x == 4)
			{
				wypisz(h, 1);
				continue;
			}
		}
		if(a == 2 && b == 4)
		{
			if(x == 1)
			{
				wypisz(h, 2);
				continue;
			}
			if(x == 2)
			{
				wypisz(h, 2);
				continue;
			}
			if(x == 3)
			{
				wypisz(h, 1);
				continue;
			}
			if(x == 4)
			{
				wypisz(h, 1);
				continue;
			}
		}
		/////// 3
		if(a == 3 && b == 3)
		{
			if(x == 1)
			{
				wypisz(h, 2);
				continue;
			}
			if(x == 2)
			{
				wypisz(h, 1);
				continue;
			}
			if(x == 3)
			{
				wypisz(h, 2);
				continue;
			}
			if(x == 4)
			{
				wypisz(h, 1);
				continue;
			}
		}
		if(a == 3 && b == 4)
		{
			if(x == 1)
			{
				wypisz(h, 2);
				continue;
			}
			if(x == 2)
			{
				wypisz(h, 2);
				continue;
			}
			if(x == 3)
			{
				wypisz(h, 2);
				continue;
			}
			if(x == 4)
			{
				wypisz(h, 2);
				continue;
			}
		}
		///// 4
		if(a == 4 && b == 4)
		{
			if(x == 1)
			{
				wypisz(h, 2);
				continue;
			}
			if(x == 2)
			{
				wypisz(h, 2);
				continue;
			}
			if(x == 3)
			{
				wypisz(h, 1);
				continue;
			}
			if(x == 4)
			{
				wypisz(h, 2);
				continue;
			}
		}
	}
}