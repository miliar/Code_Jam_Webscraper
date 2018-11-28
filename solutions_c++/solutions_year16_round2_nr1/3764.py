#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)
const int MOD = 1000002013;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;
ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }
int bc(int n) { return n ? bc((n-1)&n)+1 : 0; }

int main() {
    //freopen("x.in", "r", stdin);

	freopen("A-small-attempt2.in", "r", stdin);
	freopen("A-small-attempt2.out", "w", stdout);

	//freopen("C-large.in", "r", stdin);
	//freopen("C-large.out", "w", stdout);

	int tt, tn; cin >> tn;
	string map[] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };

	F1(tt,tn) {
  		printf("Case #%d: ", tt);

		string s, o;
		cin >> s;
		int len = s.length();
		char m[26] = {0};
		int O[10] = {0};
		int c = 0;
		F0(i,len) {
			m[s.at(i)-'A']++;
		}

		do {
			F0 (i,10) O[i] = 0;
			c = 0;


			while (m['S'-'A']>0) {
				if ( m['I'-'A']<=0 || m['X'-'A']<=0 ) break;

				m['S'-'A']--;
				m['I'-'A']--;
				m['X'-'A']--;

				c += 3;
				O[6]++;
			}

			while (m['S'-'A']>0) {
				if (m['E'-'A'] <=1 || m['V'-'A'] <=0 || m['N'-'A'] <= 0) break;
				m['S'-'A']--;
				m['E'-'A']--;
				m['V'-'A']--;
				m['E'-'A']--;
				m['N'-'A']--;

				c += 5;
				O[7]++;
			}

			while (m['F'-'A']>0) {
				if (m['I'-'A'] <=0 || m['V'-'A']<=0 || m['E'-'A']<=0) break;
				m['F'-'A']--;
				m['I'-'A']--;
				m['V'-'A']--;
				m['E'-'A']--;

				c += 4;
				O[5]++;
			}

			while (m['E'-'A']>0) {
				if (m['G'-'A']<=0) break;

				m['E'-'A']--;
				m['I'-'A']--;
				m['G'-'A']--;
				m['H'-'A']--;
				m['T'-'A']--;

				c += 5;
				O[8]++;
			}

			while (m['T'-'A']>0) {
				if (m['H'-'A']<=0 || m['R'-'A']<=0 || m['E'-'A']<=1) break;
				m['T'-'A']--;
				m['H'-'A']--;
				m['R'-'A']--;
				m['E'-'A'] -=2;

				c += 5;
				O[3]++;
			}

			while (m['Z'-'A']>0) {
				m['Z'-'A']--;
				m['E'-'A']--;
				m['R'-'A']--;
				m['O'-'A']--;
				c +=4;
				O[0]++;
			}

			while (m['F'-'A']>0) {
				if (m['O'-'A']<=0 || m['U'-'A'] <=0) break;
				m['F'-'A']--;
				m['O'-'A']--;
				m['U'-'A']--;
				m['R'-'A']--;

				c += 4;
				O[4]++;
			}


			while (m['N'-'A']>=2) {
				if (m['I'-'A'] <= 0 || m['E'-'A'] <= 0) break;
				m['N'-'A']--;
				m['I'-'A']--;
				m['N'-'A']--;
				m['E'-'A']--;

				c += 4;
				O[9]++;
			}


			while (m['O'-'A']>0) {
				if (m['N'-'A']<=0 || m['E'-'A']<=0) {
					break;
				}

				m['N'-'A']--;
				m['E'-'A']--;
				m['O'-'A']--;
				c += 3;
				O[1]++;
			}

			while (m['T'-'A']>0) {
				if (m['W'-'A']<=0) break;
				m['W'-'A']--;
				m['O'-'A']--;
				m['T'-'A']--;

				c += 3;
				O[2]++;
			}
		}while(0);
		F0 (i,10) {
			while(O[i]-->0)
				cout << i;
		}


		//if (c!=len) cout << s << " : Watch Out !! (" << c << "):" << len;
		cout << o << endl;
	}
	return 0;
}
