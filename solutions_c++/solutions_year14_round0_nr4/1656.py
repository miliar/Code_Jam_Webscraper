#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int war(const vector<double> &naomi, const vector<double> &ken)
{
	int ans = naomi.size();
	auto n = naomi.begin(), k = ken.begin();
	while (k!=ken.end())
		if (*k>*n)
		{
			ans--;
			n++;
			k++;
		}
		else
			k++;
	return ans;
}

int deceitfulWar(const vector<double> &naomi, const vector<double> &ken)
{
	int ans = 0;
	auto n = naomi.rbegin(), k = ken.rbegin();
	while (k!=ken.rend())
		if (*n>*k)
		{
			ans++;
			n++;
			k++;
		}
		else
			k++;
	return ans;
}

int main()
{
	int t;
	int n;
	double get;
	vector<double> naomi, ken;
	cin >> t;
	for (int i=1;i<=t;i++)
	{
		naomi.clear();
		ken.clear();
		cin >> n;
		for (int j=0;j<n;j++)
		{
			cin >> get;
			naomi.push_back(get);
		}
		sort(naomi.begin(), naomi.end());
		for (int j=0;j<n;j++)
		{
			cin >> get;
			ken.push_back(get);
		}
		sort(ken.begin(), ken.end());
		cout << "Case #" << i << ": " << deceitfulWar(naomi, ken) << " " << war(naomi, ken) << endl;
	}
	return 0;
}
