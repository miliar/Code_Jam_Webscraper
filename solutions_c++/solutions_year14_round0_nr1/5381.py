#include <iostream>
#include <algorithm>

using namespace std;

const int rowCount = 4;
int CT[rowCount * rowCount];

int main(int argc, char const *argv[])
{
	int cases; cin >> cases;

	for (int tc = 1; tc <= cases; ++tc)
	{

		int rowf, x;
		cout << "Case #" << tc << ": ";
		fill(CT, CT + rowCount * rowCount, 0);
		cin >> rowf;
		for (int j = 0; j < rowCount; ++j)
		{
			for (int i = 0; i < rowCount; ++i)
			{
				cin >> x;
				if (j == rowf - 1) CT[x - 1] ++;
			}
			
		}

		cin >> rowf;
		for (int j = 0; j < rowCount; ++j)
		{
			for (int i = 0; i < rowCount; ++i)
			{
				cin >> x;
				if (j == rowf - 1) CT[x - 1] ++;
			}
			
		}

		int unique = -1;

		for (int i = 0; i < rowCount * rowCount; i ++)
			if (CT[i] == 2) {
				if (unique == -1)
					unique = i + 1;
				else
					unique = -2;

			}
		if (unique == -2) cout << "Bad magician!" << endl;
		else if (unique == -1) cout << "Volunteer cheated!" << endl;
		else cout << unique << endl;
		
	}
	return 0;
}