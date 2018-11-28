#include <bits/stdc++.h>
#define pb push_back
#define ll long long
#define ld long double
#define endl "\n"


using namespace std;

int main() {
	ios_base::sync_with_stdio(0);	

	string toStr[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

	int n;
	cin >> n;

	for(int test = 1; test <= n; test++) {
		cout << "Case #" << test << ": ";
		string str;
		cin >> str;
		sort(str.begin(), str.end());
		int ndigits = str.length()/5;
		bool found = false;
		while(!found) { // boucle sur les nb de digits
			int digits[ndigits];
			for(int i = 0; i < ndigits; i++) digits[i] = 0;

			while(!found) {
				// test sur cette combinaison
				string comb;
				for(int i = 0; i < ndigits; i++) {
					comb.append(toStr[digits[i]]);
				}
				sort(comb.begin(), comb.end());
				
				if(comb == str) {
					found = true;
					for(int i = 0; i < ndigits; i++) cout << digits[i];
					cout << endl;
					break;
				}

				// increment
				int i = ndigits-1;
				digits[i]++;
				while(i >= 0 && digits[i] >= 10) {
					if(i == 0) digits[i] = 0;
					else digits[i] = digits[i-1];
					i--;
					digits[i]++;
				}
				if (i < 0) break;
			}

			ndigits++;
		}
	}

	return 0;
}
