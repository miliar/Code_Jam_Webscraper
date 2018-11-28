#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cassert>
#include <bitset>
#include <unordered_set>
#include <unordered_map>

#define forn(i, n) for (int i = 0; i < (n); i++)
#define fore(i, l, r) for (int i = l; ((l) < (r) ? i <= (r) : i >= (r)); ((l) < (r) ? i++ : i--))
#define all(a) (a).begin(), (a).end()
#define sz(a) (int)((a).size())
#define mp make_pair

using namespace std;

typedef long long li;
typedef long double ld;

template<typename X> inline X abs(const X& a) { return a < 0 ? -a : a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

template<typename A, typename B> inline ostream& operator<< (ostream& out, const pair<A, B>& p) { return out << "(" << p.x << ", " << p.y << ")"; }
template<typename T> inline ostream& operator<< (ostream& out, const vector<T>& a) { out << "["; forn(i, sz(a)) { if (i) out << ','; out << ' ' << a[i]; } return out << " ]"; }
template<typename T> inline ostream& operator<< (ostream& out, const set<T>& a) { return out << vector<T>(all(a)); }
template<typename T> inline ostream& operator<< (ostream& out, pair<T*, int> a) { return out << vector<T>(a.x, a.x + a.y); }

inline ld gett() { return ld(clock()) / CLOCKS_PER_SEC; }

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9, PI = 3.1415926535897932384626433832795;

const int MAXN = 200001;

int n, q;

li tekSdvig;
vector <int> v1, v2;
int tekV = 1;
int cntSwap;



void execSwap() {
	for (int i = 0; i < n; i += 2) {
		swap(v1[i], v1[i + 1]);
		swap(v2[i], v2[i + 1]);
	}
}

void execSdvig() {
	if (tekSdvig % 2 == 0) {
		cntSwap++;
		return;
	}

	if (cntSwap % 2 != 0) {
		execSwap();
		cntSwap = 0;
	}

	if (tekV == 1) {
		forn(i, n) {
			v2[(i + tekSdvig) % n] = v1[i];
		}
		tekV = 2;
	}
	else {
		forn(i, n) {
			v1[(i + tekSdvig) % n] = v2[i];
		}
		tekV = 1;
	}
	tekSdvig = 0;

	execSwap();
}

int main() {
#ifdef _DEBUG
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	srand(time(NULL));
	ld startTime = gett();
	int T;
	cin >> T;
	vector <int> p;
	forn(i, T) {
		cout << "Case #" << i + 1 << ": ";
		int n;
		cin >> n;
		p.clear();
		p.resize(n);
		int all = 0;
		forn(j, n) {
			cin >> p[j];
			all += p[j];
		}
		while (all > 0) {
			forn(a, p.size()) {
				forn(b, p.size()) {
					p[a]--;
					p[b]--;
					all -= 2;
					bool ok = true;
					forn(k, p.size()) {
						if (p[k] > all / 2) {
							ok = false;
							break;
						}
					}
					if (ok) {
						cout << (char)('A' + a) << (char)('A' + b) << " ";
					}
					else {
						p[a]++, p[b]++, all += 2;
					}
				}
				if (all == 0)
					break;
				p[a]--;
				all--;
				bool ok = true;
				forn(k, p.size()) {
					if (p[k] > all / 2) {
						ok = false;
						break;
					}
				}
				if (ok) {
					cout << (char)('A' + a) << " ";
				}
				else {
					p[a]++, all += 1;
				}
			}
		}
		cout << endl;


	}
	cerr << "Time: " << gett() - startTime << " ms" << endl;
}