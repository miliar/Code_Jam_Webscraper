#include<fstream>
#include<iostream>
using namespace std;

void exp(int &num, int pow)
{
	for (int i = 0; i < pow; i++)
		num *= num;
}

int main()
{
	int cases; cin >> cases;
	int nCase = 1;
	while (cases >= nCase)
	{
		int n; cin >> n;
		int digits = 0;
		if (n == 0)
			cout << "Case #" << nCase++ << ": INSOMNIA" << endl;
		else
		{
			bool check[10] = { false };
			bool cont = true;
			int copy = n;
			while (cont == true)
			{
				for (int i = 1; i < n; i++)
				{
					int base = 10;
					exp(base, i);
					if (n / base == 0)
					{
						digits = i + 2;
						break;
					}
				}
				int cpy = n;
				for (int i = 0; i < digits; i++)
				{
					if (cpy > 0)
					{
						check[cpy % 10] = true;
						cpy /= 10;
					}
				}
				cont = false;
				for (int i = 0; i < 10; i++)
					if (check[i] == false)
						cont = true;
				if (cont == false)
					cout << "Case #" << nCase++ << ": " << n << endl;
				n += copy;
			}
		}
	}
}

