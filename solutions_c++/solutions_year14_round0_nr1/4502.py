#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	int t = 0;
	int round1 = 0;
	int round2 = 0;
	cin >> t;
	vector <vector<int> > v1(4);
	vector <vector<int> > v2(4);
	for (int cur = 0; cur < t; cur++)
	{
		cin >> round1;
		round1--;
		for (int i=0; i < 4; i++)
		{
			v1[i].resize(4);
			for (int j=0; j < 4; j++)
			{ 
				cin >> v1[i][j];
			}
		}
		cin >> round2;
		round2--;
		for (int i=0; i < 4; i++)
		{
			v2[i].resize(4);
			for (int j=0; j < 4; j++)
			{ 
				cin >> v2[i][j];
			}
		}
		int num = 0;
		int got = 0;
		for (int i=0; i < 4; i++)
		{
			auto& gv2 = v2[round2];
			auto iter = find(gv2.begin(), gv2.end(), v1[round1][i]);
			if (iter != gv2.end())
			{
				num++;
				got = v1[round1][i];
			}
		}
		
		if (num < 1)
		{
			cout << "Case #" << cur + 1 << ": " << "Volunteer cheated!" << endl;
		}
		else if (num == 1)
		{
			cout << "Case #" << cur + 1 << ": " << got << endl;
		}
		else
		{
			cout << "Case #" << cur + 1 << ": " << "Bad magician!" << endl;
		}
	}
	return 0;
}
