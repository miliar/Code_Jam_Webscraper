#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main ()
{
	ifstream cin ( "A-small-attempt0.in" );
	ofstream cout ( "output.txt" );
	int t;
	cin >> t;
	int k = 1;
	while (t--)
	{
		int a, b;
		vector < vector <int> > c1 (4, vector <int> (4)), c2 (4, vector <int> (4));
		cin >> a;
		--a;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				cin >> c1 [i][j];
		cin >> b;
		--b;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				cin >> c2 [i][j];
		int ans = -1;
		bool flag = false;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				if (c1 [a][i] == c2 [b][j])
				{
					if (ans != -1)
						flag = true;
					else
						ans = c1 [a][i];
				}
		cout << "Case #" << k++ << ": ";
		if (ans == -1)
			cout << "Volunteer cheated!" << endl;
		else if (flag)
			cout << "Bad magician!" << endl;
		else
			cout << ans << endl;
	}
}