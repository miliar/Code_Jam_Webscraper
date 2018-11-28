#include <iostream>
#include <set>

using namespace std;

int main()
{
    cout.precision(7);
	cout << std::fixed;
    int t;
    cin >> t;
    for (int cn = 1; cn <= t; ++cn)
	{
		int n;
		cin >> n;
		set<double> naomi;
		set<double> ken;
		for (int i = 0; i < n; ++i)
		{
			double w;
			cin >> w;
			naomi.insert(w);
		}
		for (int i = 0; i < n; ++i)
		{
			double w;
			cin >> w;
			ken.insert(w);
		}
		// strategy optimal
		int opt = 0;
		set<double> onaomi(naomi);
		set<double> oken(ken);
		while (onaomi.size() > 0)
		{
			set<double>::iterator kenmove = oken.upper_bound(*onaomi.begin());
			if (kenmove != oken.end())
			{
				onaomi.erase(onaomi.begin());
				oken.erase(kenmove);
			}
			else
			{
				++opt;
				onaomi.erase(onaomi.begin());
				oken.erase(oken.begin());
			}
		}
		// strategy deceitful
		int dec = 0;
		while (naomi.size() > 0)
		{
			if (*naomi.begin() > *ken.begin())
			{
				++dec;
				naomi.erase(naomi.begin());
				ken.erase(ken.begin());
			}
			else
			{
				naomi.erase(naomi.begin());
				ken.erase(--ken.end());
			}
		}
		// output
		cout << "Case #" << cn << ": " << dec << " " << opt << "\n";
    }

    return 0;
}
