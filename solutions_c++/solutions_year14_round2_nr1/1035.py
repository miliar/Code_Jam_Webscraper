#include <iostream>
#include <string>
#include <vector>
#include <limits>
#include <cstdlib>
#include <algorithm>
using namespace std;
typedef vector<int> vi;
class Info {
public:
	char a;
	vi qtd;
};
int T, N;
typedef vector<Info> vin;
vin vals;
string aux;
bool can;
int main() {
	ios_base::sync_with_stdio(false);
	cin >> T;
	for (int caso=1; caso<=T; caso++) {
		cout << "Case #" << caso << ": ";
		vals.clear(); can = true;
		cin >> N;
		N--;

		cin >> aux;
		for (int i=0; i<aux.length(); i++) {
			char c = aux[i];
			int qtd = 0;
			do {
				i++;
				qtd++;
			} while (i<aux.length() && aux[i] == c);
			i--;

			Info inf;
			inf.a = c;
			inf.qtd.push_back(qtd);
			vals.push_back(inf);
		}
		
		while (N--) {
			int infidx = 0;
			cin >> aux;
			if (!can) continue;

			for (int i=0; i<aux.length(); i++) {
				if (infidx >= vals.size() || aux[i] != vals[infidx].a) {
					can = false;
					continue;
				}
				int qtd = 0;
				do {
					i++;
					qtd++;
				} while (i<aux.length() && aux[i] == vals[infidx].a);
				i--;

				vals[infidx].qtd.push_back(qtd);
				infidx++;
			}
			if (infidx != vals.size())
				can = false;
		}

		if (!can) {
			cout << "Fegla Won\n";
			continue;
		}


		int res = 0;

		for (int i=0; i<vals.size(); i++) {
			int best = numeric_limits<int>::max();
			for (int j=0; j<vals[i].qtd.size(); j++) {
				int curr = 0;
				for (int k=0; k<vals[i].qtd.size(); k++) {
					curr += abs(vals[i].qtd[j]-vals[i].qtd[k]);
				}
				best = min(best,curr);
			}
			res += best;
		}

		cout << res << "\n";
	}
}