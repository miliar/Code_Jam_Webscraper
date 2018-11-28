
#include<string>
#include<vector>
#include<stack>
#include<algorithm>
#include <map>
#include <queue>
#include <string.h>
#include <fstream>
#include <cmath>

using namespace std;

ofstream cout("out.txt");
ifstream cin("A-large.in");

int main(void)
{

	int t;
	cin >> t;

	

	for (int tc = 1; tc <= t; tc++)
	{

		vector < vector<pair<char, int> > > vec;

		int n;
		cin >> n;
		int mxLen = 0;

		for (int i = 0; i < n; i++)
		{
			string x;
			cin >> x;
			
			vector<pair<char, int> > curvec;
			char cch = x[0];
			int cc = 1;

			for (int j = 1; j < x.size(); j++)
			{
				if (x[j] == cch)
				{
					cc++;
				}
				else
				{
					curvec.push_back(make_pair(cch, cc));
					cch = x[j];
					cc = 1;
				}
			}
			curvec.push_back(make_pair(cch, cc));

			vec.push_back(curvec);

			mxLen = max(mxLen, (int)curvec.size());
			
		}

		int j = 0;

		bool can = true;

		for (int i = 1; i < vec.size(); i++)
		{
			if (vec[i].size() != vec[0].size())
			{
				can = false;
				break;
			}
		}

		int res = 0;

		while (can && j < mxLen)
		{
			vector<int> med;
			med.push_back(vec[0][j].second);
			for (int i = 1; i < vec.size(); i++)
			{
				if (vec[i][j].first != vec[0][j].first)
				{
					can = false;
					break;
				}
				else
				{
					med.push_back(vec[i][j].second);
				}
			}

			sort(med.begin(), med.end());
			int sz = med.size();

			int median = med.size() % 2 != 0 ? med[sz / 2] : (med[sz / 2] + med[sz / 2 - 1]) / 2;

			for (int i = 0; i < sz; i++)
			{
				res += abs(med[i] - median);
			}

			j++;

		}

		if (can)
		{
			cout << "Case #" << tc << ": " << res << endl;
		}
		else
		cout << "Case #" << tc << ": " << "Fegla Won" << endl;

	}

	return 0;
}