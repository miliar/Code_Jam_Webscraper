#include <iostream>

using namespace std;

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int T;
	cin >> T;
	for (int tt = 1 ; tt <= T ; tt++)
	{
		int x1, x2;
		cin >> x1;
		int mtx1[4][4], mtx2[4][4];
		for (int i = 0 ; i < 4 ; i++)
			for (int j = 0 ; j < 4 ; j++)
				cin >> mtx1[i][j];
		cin >> x2;
		for (int i = 0 ; i < 4 ; i++)
			for (int j = 0 ; j < 4 ; j++)
				cin >> mtx2[i][j];

		x1--;
		x2--;
		int sum = 0, numb;
		for (int i = 0 ; i < 4 ; i++)
			for (int j = 0 ; j < 4 ; j++)
				if (mtx1[x1][i] == mtx2[x2][j])
				{
					sum++;
					numb = mtx1[x1][i];
				}
		cout << "Case #" << tt << ": ";
		if (sum == 0)
			cout << "Volunteer cheated!" << endl;
		else if (sum == 1)
			cout << numb << endl;
		else
			cout << "Bad magician!" << endl;
	}
}