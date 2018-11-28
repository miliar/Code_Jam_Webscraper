#include <iostream>
#include <string>
#include <vector>
#include <cstring>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#define mp make_pair
#define pb push_back
#define fi first
#define se second
using namespace std;

typedef long long ll;
int partidos[30];
typedef pair<double, int> pdi;
vector<pdi> ratio;

bool calcRatio(int n) {
	ratio.clear();
	int soma = 0;
	for(int i = 0; i < n; i++)
		soma += partidos[i];
	bool good = true;
	if(soma != 0) {
		for(int i = 0; i < n; i++) {
			if(partidos[i] == 0)
				ratio.pb(mp(-0.00000001, i));
			else
				ratio.pb(mp(-(double)partidos[i] / soma, i));
			if(-ratio[i].fi > 0.5)
				good = false;
 		}
		sort(ratio.begin(), ratio.end());
	}
	return good;
}

int main() {

	int t, n;
	cin >> t;
	for(int i = 0; i < t; i++) {
		cin >> n;
		memset(partidos, 0, sizeof partidos);
		int soma = 0;
		for(int j = 0; j < n; j++) {
			cin >> partidos[j];
			soma += partidos[j];
		}
		cout << "Case #" << i+1 << ":";
		while(soma > 0) {
			calcRatio(n);
			cout << " ";
			int j = 0;
			if(-ratio[j].fi > 0 && partidos[ratio[j].se] > 0) {
				partidos[ratio[j].se]--;
				cout << (char)(ratio[j].se + 'A');
				soma--;
				bool good = false;
				calcRatio(n);
				if(partidos[ratio[j].se] > 0) {
					int idx = ratio[j].se;
					partidos[idx]--;
					soma--;
					if(calcRatio(n)) {
						cout << (char)(idx + 'A'); 
						good = true;
					}
					else {
						partidos[idx]++;
						soma++;
						calcRatio(n);
					}
				}

				/*if(!good && partidos[ratio[j+1].se] > 0) {
					int idx = ratio[j+1].se; 
					cout << idx;
					partidos[idx]--;
					soma--;
					if(calcRatio(n))
						cout << (char)(idx + 'A');
					else {
						partidos[idx]++;
						soma++;
						calcRatio(n);
					}
				}*/
			}
		}		
		cout << endl;
	}

	return 0;
}
