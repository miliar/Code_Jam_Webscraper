#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main()
{
	ofstream ofs("magic_trick.txt");

	int testcase;
	cin >> testcase;

	int tc = 0;

	vector<int> vec1, vec2;
	int row1, row2, tmp;

	while (tc != testcase)
	{
		tc++;
		cin >> row1;

		for (int i = 0; i < 16; ++i)
		{
			cin >> tmp;
			vec1.push_back(tmp);
		}

		cin >> row2;

		for (int i = 0; i < 16; ++i)
		{
			cin >> tmp;
			vec2.push_back(tmp);
		}

		int count = 0;
		int ans;

		for (int j = 4*(row1-1); j < 4*row1; j++)
		{
			int k = vec1[j];
			for (int l = 4*(row2-1); l < 4*row2; l++)
			{
				if (k == vec2[l])
				{
					count++;
					ans = k;
				}
			}
		}

		ofs << "Case #" << tc << ": ";
		if (count == 1)
		{
			ofs << ans;
		}
		else if (count == 0)
		{
			ofs << "Volunteer cheated!";
		}
		else
		{
			ofs << "Bad magician!";
		}
		ofs << endl;

		vec1.clear();
		vec2.clear();
	}
}