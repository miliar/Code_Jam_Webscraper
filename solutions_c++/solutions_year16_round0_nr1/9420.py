#include <iostream>
#include <cstdlib>
using namespace std;

int c, n, tn;
bool num[10];


void null_n()
{
	for (int i = 0; i < 10; ++i)
	{
		num[i] = false;
	}
}

void check_n(int an)
{
	while (an && c < 10)
	{
		if (!num[an % 10])
		{
			num[an % 10] = true;
			c++;
		}
		an /= 10;
	}
}


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		cin >> n;
		if (!n)
		{
			cout << "Case #" << i + 1 << ": INSOMNIA\n";
			continue;
		}
		null_n();
		c = 0;
		tn = n;
		check_n(tn);
		while (c < 10)
		{
			tn += n;
			check_n(tn);
		}
		cout << "Case #" << i + 1 << ": " << tn << "\n";
	}
	return 0;
}