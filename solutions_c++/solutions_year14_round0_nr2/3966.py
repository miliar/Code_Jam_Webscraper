#include <iostream>
using namespace std;

long long n, m, i, j, k, q, s, w, v;
long double c, f, x, current, time, prod;

int main()
{
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	cin >> w;
	v = w;
	while (w--)
	{
		cin >> c >> f >> x;
		current = x / 2;
		time = 0;
		prod = 2;
		while (1)
		{
			if (time + c / prod + x / (prod + f) < current)
			{
				current = time + c / prod + x / (prod + f);
				time += c / prod;
				prod += f;
			}
			else
			{
				cout.setf(ios::fixed);
				cout.precision(7);
				cout << "Case #" << v - w << ": " << time + x / prod << endl;
				break;
			}
		}
	}
	return 0;
}




