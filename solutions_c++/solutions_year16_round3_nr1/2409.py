#include <bits/stdc++.h>

using namespace std;

bool pairCompare(const std::pair<int, int>& firstElem, const std::pair<int, int>& secondElem) {
	return firstElem.second > secondElem.second;
}

int main()
{
	ios_base::sync_with_stdio(false);
	int n;
	cin >> n;

	for(int j = 0; j < n; ++j)
	{
		string ans = "";

		int nParty;
		cin >> nParty;
		
		vector<pair<int, int>> arrParty;

		int nJumlah = 0;
		for (int i = 0; i < nParty; ++i) {
			int tot;
			cin >> tot;
			arrParty.push_back(make_pair(i, tot));
			nJumlah += tot;
		}

		int jumlah = 0;
		sort(arrParty.begin(), arrParty.end(), pairCompare);
		while(arrParty[0].second) {
			if (jumlah >= 2 && jumlah % 2 == 0)
				ans += " ";
			if ((jumlah == nJumlah - 2) && nJumlah > 2 && nJumlah % 2 == 1) {
				ans += " ";
				++jumlah;
			}
			ans += arrParty[0].first + 'A';
			--arrParty[0].second;
			sort(arrParty.begin(), arrParty.end(), pairCompare);
			++jumlah;
		}

		cout << "Case #" << j+1 << ": " << ans << endl;
	}

	return 0;
}