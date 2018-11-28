#include <iostream>
#include <algorithm>
#include <vector>
#include <cassert>

using namespace std;

typedef long long int ll;

ll cand[16];

int main() {
	cand[0] = cand[15] = 1;
	int trovati = 0;
	cout << "Case #1:\n";
	
	for (int i=0; i<(ll)round(pow(2, 14)) && trovati < 50; i++) {
		// Creo la candidata jamcoin
		ll x = i;
		for (int j=14; j>=1; j--) {
			cand[j] = x%2;
			x = x/2;
		}
		
		// Verifico che sia ok in ogni base
		vector<ll> div;
		vector<ll> num;
		bool ok = true;
		for (int b = 2; b<=10 && ok; b++) {
			x = 0;
			for (int j=0; j<16; j++)
				x = x*b+cand[j];
			num.push_back(x);
			for (int j=2; j <= min((ll)100, x-1); j++)//(int)round(sqrt(x)); j++)
				if (x%j == 0) {
					div.push_back(j);
					break;
				}
			if ((int)div.size() != b-1) {
				ok = false;
				break; // allora lo scarto
			}
		}
		
		if (!ok) continue;
		
		// Se arrivo qui vuol dire che è ok, lo stampo
		trovati++;
		
		for (int j=0; j<16; j++)
			cout << cand[j];
		assert(div.size() ==9);
		//cout << endl;
		for (int j=0; j<(int)div.size(); j++)
			cout << " " << div[j];
			//cout << num[j] << " " << div[j] << endl;;
		cout << endl;
	}
	
	return 0;
}
