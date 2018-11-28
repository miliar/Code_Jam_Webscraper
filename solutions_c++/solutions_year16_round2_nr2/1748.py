#include <bits/stdc++.h>

using namespace std;

int pow10(int p) {
	int ppow = 1;
	for(int i = 0; i < p; i++) {
		ppow *= 10;
	}

	return ppow;
}

int digits(int n) {
	if(n == 0) {
		return 1;
	}
	return (int) log10(n) + 1;
}

void solve() {
	string a, b;
	cin >> a >> b;

	int ppow = 1;

	vector<pair<int, int>> aq;
	vector<pair<int, int>> bq;

	int as = 0;
	int bs = 0;
	for(int i = a.length() - 1; i >= 0; i--) {
		if(a[i] != '?') {
			as += (a[i] - '0') * ppow;
		}
		else {
			aq.push_back(make_pair(a.length()-1 - i, 0));
		}
		if(b[i] != '?') {
			bs += (b[i] - '0') * ppow;
		}
		else {
			bq.push_back(make_pair(a.length()-1 - i, 0));
		}

		ppow *= 10;
	}

	//cout << "asbs: " << as << " " << bs << endl;

	int bestDiff = abs(as - bs);
	int besta = as;
	int bestb = bs;

	int ad = 0;
	int bd = 0;

	while(true) {
		bool overflow = true;
		for(int i = 0; i < aq.size(); i++) {
			if(aq[i].second == 9) {
				aq[i].second = 0;
				ad -= pow10(aq[i].first) * 9;
			}
			else {
				aq[i].second++;
				ad += pow10(aq[i].first);
				overflow = false;
				break;
			}
		}

		if(overflow) {
			for(int i = 0; i < bq.size(); i++) {
				if(bq[i].second == 9) {
					bq[i].second = 0;
					bd -= pow10(bq[i].first) * 9;
				}
				else {
					bq[i].second++;
					bd += pow10(bq[i].first);
					overflow = false;
					break;
				}
			}
		}

		if(overflow) {
			break;
		}

		int na = as + ad;
		int nb = bs + bd;

		//cout << "ad: " << na << endl;
		//cout << "bd: " << nb << endl;
		//cout << endl;

		int diff = abs(na - nb);
		if(diff < bestDiff) {
			bestDiff = diff;
			besta = na;
			bestb = nb;
		}
		else if(diff == bestDiff) {
			if(na < besta) {
				besta = na;
				bestb = nb;
			}
			else if(na == besta) {
				if(nb < bestb) {
					bestb = nb;
				}
			}
		}
	}

	for(int i = 0; i < a.length() - digits(besta); i++) {
		cout << '0';
	}
	cout << besta << " ";
	for(int i = 0; i < a.length() - digits(bestb); i++) {
		cout << '0';
	}
	cout << bestb << endl;

	//cout << besta << " " << bestb << endl;
}

int main() {
	int t;
	cin >> t;

	for(int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";

		solve();
	}

	return 0;
}
