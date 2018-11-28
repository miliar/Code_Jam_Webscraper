#include <fstream>
#include <vector>

using namespace std;

int main()
{
	ifstream cin ("A-small-attempt1.in");
	ofstream cout ("A-small-attempt1.out");
	int tests, cases = 1;
	cin >> tests;
	for (; tests; tests--)
	{
		int num, card;
		vector <int> v, res;
		cin >> num;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
			{
				cin >> card;
				if (i == num - 1)
					v.push_back(card);
			}
		cin >> num;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
			{
				cin >> card;
				if (i == num - 1)
					if ( find(v.begin(), v.end(), card ) != v.end() )
						res.push_back(card);
			}
		if (res.size() == 0)
			cout << "Case #" << cases << ": " << "Volunteer cheated!" << endl;
		if (res.size() == 1)
			cout << "Case #" << cases << ": " << res[0] << endl;
		if (res.size() > 1)
			cout << "Case #" << cases << ": " << "Bad magician!" << endl;
		cases ++;
	}
}