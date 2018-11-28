#include <bits/stdc++.h>

using namespace std;

int main()
{	
	int n;
	scanf("%d", &n);

	for(int j = 0; j < n; ++j)
	{
		string ans = "";
		string s;
		cin >> s;
		int jumlah[26];
		memset(jumlah, 0, sizeof(jumlah));
		int hasil[10];
		memset(hasil, 0, sizeof(hasil));

		for (int i = 0; i < s.length(); ++i) {
			++jumlah[s[i]-'A'];
		}

		hasil[0] += jumlah['Z'-'A'];
		jumlah['E'-'A'] -= jumlah['Z'-'A'];
		jumlah['R'-'A'] -= jumlah['Z'-'A'];
		jumlah['O'-'A'] -= jumlah['Z'-'A'];

		hasil[2] += jumlah['W'-'A'];
		jumlah['T'-'A'] -= jumlah['W'-'A'];
		jumlah['O'-'A'] -= jumlah['W'-'A'];

		hasil[4] += jumlah['U'-'A'];
		jumlah['F'-'A'] -= jumlah['U'-'A'];
		jumlah['O'-'A'] -= jumlah['U'-'A'];
		jumlah['R'-'A'] -= jumlah['U'-'A'];

		hasil[6] += jumlah['X'-'A'];
		jumlah['S'-'A'] -= jumlah['X'-'A'];
		jumlah['I'-'A'] -= jumlah['X'-'A'];

		while (jumlah['E'-'A'] && jumlah['I'-'A'] && jumlah['G'-'A'] && jumlah['H'-'A'] && jumlah['T'-'A']) {
			--jumlah['E'-'A'];
			--jumlah['I'-'A'];
			--jumlah['G'-'A'];
			--jumlah['H'-'A'];
			--jumlah['T'-'A'];
			++hasil[8];
		}

		while (jumlah['F'-'A'] && jumlah['I'-'A'] && jumlah['V'-'A'] && jumlah['E'-'A']) {
			--jumlah['F'-'A'];
			--jumlah['I'-'A'];
			--jumlah['V'-'A'];
			--jumlah['E'-'A'];
			++hasil[5];
		}

		while (jumlah['O'-'A'] && jumlah['N'-'A'] && jumlah['E'-'A']) {
			--jumlah['O'-'A'];
			--jumlah['N'-'A'];
			--jumlah['E'-'A'];
			++hasil[1];
		}

		while (jumlah['T'-'A'] && jumlah['H'-'A'] && jumlah['R'-'A'] && (jumlah['E'-'A'] >= 2) ) {
			--jumlah['T'-'A'];
			--jumlah['H'-'A'];
			--jumlah['R'-'A'];
			jumlah['E'-'A'] -= 2;
			++hasil[3];
		}

		while (jumlah['S'-'A'] && jumlah['V'-'A'] && jumlah['N'-'A'] && (jumlah['E'-'A'] >= 2) ) {
			--jumlah['S'-'A'];
			--jumlah['V'-'A'];
			--jumlah['N'-'A'];
			jumlah['E'-'A'] -= 2;
			++hasil[7];
		}

		while (jumlah['I'-'A'] && jumlah['E'-'A'] && (jumlah['N'-'A'] >= 2) ) {
			--jumlah['I'-'A'];
			--jumlah['E'-'A'];
			jumlah['N'-'A'] -= 2;
			++hasil[9];
		}

		for (int i = 0; i < 10; ++i) {
			for (int k = 0; k < hasil[i]; ++k) {
				ans += '0' + i;
			}
		}

		cout << "Case #" << j+1 << ": " << ans << endl;
	}

	return 0;
}