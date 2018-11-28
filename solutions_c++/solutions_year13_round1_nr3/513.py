#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <cmath>
#include <ctime>
#include <limits>
#include <iterator>
#include <bitset>
#define sz(m)((m).size())
#define all(a)a.begin(),a.end()
#define forn(i,n)for(int i=0,i##e=n;i<i##e;++i)
#define fori(i,m)forn(i,sz(m))
#define each(i,m)for(typeof(m.begin())i=m.begin(),i##e=m.end();i!=i##e;++i)
#define srt(s)sort(all(s))
#define dump(m)copy(all(m),ostream_iterator<typeof(m[0])>(cout,"\n"));cout<<endl
using namespace std;

int power(int x, int n) {
	int r = 1;
	forn(i, n) r *= x;
	return r;
}

int main() {
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	fout << "Case #1:" << endl;
	int T, R, N, M, K;
	fin >> T >> R >> N >> M >> K;
	forn(i, R) {
		vector<int> p(K);
		forn(j, K) fin >> p[j];
		int q = power(M - 1, N);
		string ss;
		forn(j, q) {
			int jj = j;
			vector<int> d(N);
			bool g = true;
			forn(k, N) {
				d[k] = 2 + jj % (M - 1);
				if (k > 0 && d[k-1] > d[k]) {
					g = false;
					break;
				}
				jj /= M - 1;
			}
			if (!g) continue;
			int qq = 1 << N;
			set<int> ps;
			forn(k, qq) {
				int kk = k;
				int s = 1;
				forn(l, N) {
					if (kk % 2)
						s *= d[l];
					kk /= 2;
				}
				ps.insert(s);
			}
			bool f = true;
			forn(j, K) {
				if (ps.find(p[j]) == ps.end()) {
					f = false;
					break;
				}
			}
			if (f) {
				forn(k, N) ss += d[k] + '0';
				break;
			}
		}
		if (!ss.empty()) {
			fout << ss;
		} else {
			fout << string(N, '2');
		}
		fout << endl;
	}
}