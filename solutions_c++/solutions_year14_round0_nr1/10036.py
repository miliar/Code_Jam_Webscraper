#include <iostream>
#include <vector>
#include <map>
using namespace std;

int main()
{

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;

	for (size_t i = 0; i < T; i++)
	{
		unsigned int row1, row2;
		cin >> row1;
		map<int,int>a;

		int A[4][4];

		for (size_t j = 0; j < 4; j++)
		{
			for (size_t k = 0; k < 4; k++)
			{
				cin >> A[j][k];
				if (j == row1 - 1)
					++a[A[j][k]];
			}
		}

		cin >> row2;

		int B[4][4];

		for (size_t j = 0; j < 4; j++)
		{
			for (size_t k = 0; k < 4; k++)
			{
				cin >> B[j][k];
				if (j == row2 - 1)
					++a[B[j][k]];
			}
		}

		if (a.size() == 7)
		{
			cout << "Case #" << i+1 << ": ";
			for (map<int,int>::iterator i = a.begin(); i != a.end(); i++)
			{
				if (i->second > 1)
					cout << i->first << endl;
			}
		}
		if (a.size() == 8) cout << "Case #" << i+1 << ": Volunteer cheated!\n";
		if (a.size() < 7) cout << "Case #" << i+1 << ": Bad Magician!\n";

	}

}