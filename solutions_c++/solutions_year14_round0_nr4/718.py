#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
vector<double> naomi, tmp_naomi;
vector<double> ken,   tmp_ken;

int main()
{
	int t; cin >> t;
	for (int loop = 1; loop <= t; loop++)
	{
		int n; cin >> n;
		naomi.resize(n);
		ken.resize(n);
		for (int nloop = 0; nloop < n; nloop++) cin >> naomi[nloop];
		for (int nloop = 0; nloop < n; nloop++) cin >> ken  [nloop];
		sort(naomi.begin(), naomi.end());
		sort(ken.begin(),   ken.end());

		int war_point = 0, war_ken_cur = 0;
		int deceitful_point = 0;
		for (int nloop = 0; nloop < n; nloop++)
		{
			bool naomi_win = true;
			while (war_ken_cur < n)
			{
				if (ken[war_ken_cur] > naomi[nloop])
				{
					naomi_win = false;
					break;
				}
				war_ken_cur++;
			}
			war_ken_cur++;
			if (naomi_win == true) war_point++;
		}


		while (naomi[n - 1] > 0)
		{
			if (naomi[n - 1] > ken[n - 1])
			{
				deceitful_point++;
				naomi[n - 1] = -100;
				ken[n - 1] = -100;
			}
			else
			{
				for (int nloop = 0; nloop < n; nloop++)
					if (naomi[nloop]>0)
					{
						naomi[nloop] = -100;
						ken[n - 1] = -100;
						break;
					}
			}
			sort(naomi.begin(), naomi.end());
			sort(ken.begin(), ken.end());
		}

		cout << "Case #" << loop << ": " << deceitful_point << " " << war_point << endl;

		/*
		cerr << "naomi: ";
		for (int nloop = 0; nloop < n; nloop++) cerr << naomi[nloop] << " "; cerr << endl;
		cerr << "ken: ";
		for (int nloop = 0; nloop < n; nloop++) cerr << ken[nloop] << " "; cerr << endl;
		*/
	}
}