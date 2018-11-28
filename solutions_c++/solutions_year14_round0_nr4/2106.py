#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <list>

using namespace std;

#define fr first
#define sd second
#define pb push_back
#define mp make_pair

typedef long long ll;
typedef vector < vector < double > > vvd;
typedef vector < double > vd;
typedef vector < pair < double, double> > vdd;
typedef vector < vector < long long > > vvl;
typedef vector < long long > vl;


int main()
{
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		int n;
		cin >> n;
		vector<double> nao, ken;

		for(int i = 0; i < n; i++) {
			double b;
			cin >> b;
			nao.pb(b);
		}

		for(int i = 0; i < n; i++) {
			double b;
			cin >> b;
			ken.pb(b);
		}

		sort(nao.begin(), nao.end());
		sort(ken.begin(), ken.end());
		int nl = 0, nh = n-1;
		int kl = 0, kh = n-1;

		int dw = 0;

		while(nl != nh+1) {
			if(nao[nl] < ken[kl]) {
				nl++;
				kh--;
			} else {
				nl++;
				kl++;
				dw++;
			}
		}

		nl = 0, nh = n-1;
		kl = 0, kh = n-1;
		int w = 0;

		while(nl != nh+1) {
/*			for(int h = kl; h < ken.size(); h++) {
				cout << ken[h] << " ";
			}
			cout << endl;
*/

			if(nao[nh] > ken[kh]) {
				nh--;
				kl++;
				w++;
			} else {
				vector<double>::iterator j;
				//j = upper_bound(ken.begin() + kl, ken.end(), nao[nh]);
//				j = lower_bound(ken.begin() + kl, ken.end(), nao[nh]);
				for(j = ken.begin() + kl; j < ken.end(); j++) {
					if(*j > nao[nh]) {
						break;
					}
				}

//				cout << j - ken.begin() << " " << *j << " " <<  nao[nh] << endl;
				ken.erase(j);
				kh--;
				nh--;
			}
		}


		cout << "Case #" << t << ": " << dw << " " << w << endl;
	}

	return 0;
}
