#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
	int T;

	cin >> T;

	T++;

	for (int t = 1; t < T; ++t)
	{
		bool impossible = false;
		int P,Q;
		char c;

		cin >> P;
		cin >> c;
		cin >> Q;

		int n=0;

		while (P<Q)
		{
			if (Q%2 != 0)
			{
				impossible = true;
				break;
			}
			Q /= 2;
			n++;
		}

		int nx = n;

		if (P!=Q && !impossible)
			P = P%Q;

		while (P!=Q && nx<=40 && !impossible)
		{
			if (Q%2 != 0)
			{
				impossible = true;
				break;
			}

			Q /= 2;
			if (Q<P)
				P = P%Q;
			nx++;
		}

		if (nx > 40)
			impossible = true;

		cout << "Case #" << t << ": ";

		if (n>40 || impossible){
			cout << "impossible\n";
			continue;
		}
		cout << n << '\n';
	}
	return 0;
}