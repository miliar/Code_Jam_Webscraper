#pragma comment(linker, "/STACK:67108864")

#include <iostream>
#include <fstream> 
#include <cstdio>
#include <vector>
#include <queue>
#include <cmath>
#include <algorithm>
#include <string>
#include <cstring>
#include <cassert>
#include <complex>
#include <bitset>
#include <map>
#include <set>
#include <ctime>

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define forab(i, k, n) for(int i = (int)(k); i < (int)(n); i++)
#define forba(i, n, k) for(int i = (int)(n) - 1; i >= (int)(k); i--)

#define vi vector<int>
#define pii pair<int, int>
#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x)*(x))
#define ff first
#define ss second
#define pb push_back
#define mp make_pair

using namespace std;

typedef long long ll;

const long double pi = 3.1415926535897932384626433832795;
const long double eps = 0.000000001;
const int INF = 1E9;
const int MAXN = 22;
const int MAXM = 1 << MAXN;

inline int bit(int m, int x) {
	return (m >> x) & 1;
}

int t, n, d, mmask, cmask, nmask, last, bits, maxmv[MAXM], sstate;
long double dp[MAXM], ch[MAXM], nn[MAXN + 2];
bool crct[MAXM];
string s;
queue<int> q;

int main() {

	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	cin >> t;
	forn(tt, t) {
		cin >> s;
		n = s.size();
		nn[0] = 1;
		forab(i, 1, MAXN + 2)
			nn[i] = 1.0 * nn[i - 1] * n;

		mmask = 1 << n;
		forn(i, mmask) {
			maxmv[i] = i;
			cmask = i;
			forn(j, n - 1) {
				cmask = (cmask >> 1) + ((cmask & 1) << (n - 1));
				if (cmask < maxmv[i])
					maxmv[i] = cmask; //kagbe minmv, no vlom ispravlyat'
			}
		}

		sstate = 0;
		bits = 0;
		forn(i, n)
			if (s[n - i - 1] == 'X') {
				sstate += (1 << i);
				bits++;
			}
		sstate = maxmv[sstate];

		memset(dp, 0, sizeof(dp));
		memset(ch, 0, sizeof(ch));
		memset(crct, 0, sizeof(crct));

		dp[sstate] = 0;
		ch[sstate] = 1;
		crct[sstate] = 1;
		q.push(sstate);

		while (!q.empty()) {
			cmask = q.front();
			q.pop();
			if (cmask == mmask - 1)
				break;
			if (true) {
				//chances... 1/n
				//always minimal mask
				last = n - 1;
				d = 1;
				forn(j, n) {
					if (!bit(cmask, j)) {
						d = 0;
						last = j;
						nmask = maxmv[cmask + (1 << j)];
						dp[nmask] += dp[cmask] + ch[cmask] * n;
						ch[nmask] += ch[cmask];
					} else {
						nmask = maxmv[cmask + (1 << last)];
						dp[nmask] += dp[cmask] + ch[cmask] * (n - d);
						ch[nmask] += ch[cmask];
					}
					if (!crct[nmask])
						q.push(nmask);
					crct[nmask] = 1;
					d++;
				}
			}
		}

		printf("Case #%d:", tt + 1);
		printf(" %.10llf", dp[mmask - 1] / nn[n - bits]);
		printf("\n");
	}

	return 0;
}