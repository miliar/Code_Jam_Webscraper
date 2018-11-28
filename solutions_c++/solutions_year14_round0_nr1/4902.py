#include <iostream>

using namespace std;

int b[4];
int a[4];

int main(int argc, char const *argv[])
{
	int T;
	cin >> T;

	for (int k = 0; k < T; ++k)
	{
		int B,A;
		int aux;

		cin >> B;

		for (int i = 1; i < 5; ++i)
		{

			for (int j = 0; j < 4; ++j)
			{
				cin >> aux;
				if (i==B)
					b[j] = aux;
			}
		}

		cin >> A;

		for (int i = 1; i < 5; ++i)
		{
			for (int j = 0; j < 4; ++j)
			{
				cin >> aux;
				if (i==A)
					a[j] = aux;
			}
		}

		int x,y=0;

		for (int i = 0; i < 4; ++i)
		{
			for (int j = 0; j < 4; ++j)
			{
				if (b[i] == a[j])
				{
					x=b[i];
					y++;
				}
			}
		}

		cout << "Case #" << k+1 << ": ";
		if (y == 1)
			cout << x;
		else if (y>1)
			cout << "Bad magician!";
		else
			cout << "Volunteer cheated!";
		cout << '\n';
	}
	return 0;
}