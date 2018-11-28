#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;
const double INF = 1;
int main()
{
	ifstream cin("D-large.in");
	ofstream cout("output.txt");

	int t;
	cin >> t;
	int n, deceitfulWar, War, naomiscore;
	for (int l = 1; l <= t; ++l)
	{
		cin >> n;
		vector<double> naomi(n), ken(n);
		for (int i = 0; i < n; ++i)
			cin >> naomi[i];
		for (int i = 0; i < n; ++i)
			cin >> ken[i];

		cout << "Case #" << l << ": ";

		naomiscore = 0;
		double min; int minind;
		for (int i = 0; i < n; ++i)
		{
			min = INF; minind = -1;
			for (int j = 0; j < n; ++j)
			{
				if (ken[j]>naomi[i] && ken[j] < min)
				{
					min = ken[j];
					minind = j;
				}
			}
			if (minind != -1)
			{
				ken[minind] = -ken[minind];
			}
			else
			{
				++naomiscore;
				min = INF; minind = -1;
				for (int j = 0; j < n; ++j)
				{
					if (ken[j] < min && ken[j] > 0)
					{
						min = ken[j];
						minind = j;
					}
				}
				ken[minind] = -ken[minind];
			}
		}
		int warscore = naomiscore;
		for (int i = 0; i < n; i++)
			ken[i] = abs(ken[i]);
		naomiscore = 0;
		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());
		while (!naomi.empty())
		{
			if (naomi[naomi.size() - 1] > ken[ken.size() - 1])
			{
				naomiscore++;
				naomi.erase(naomi.begin() + naomi.size() - 1);
				ken.erase(ken.begin() + ken.size() - 1);
			}
			else
			{
				naomi.erase(naomi.begin());
				ken.erase(ken.begin() + ken.size() - 1);
			}
		}
		cout << naomiscore << " ";


		
		cout << warscore << endl;
	}
}