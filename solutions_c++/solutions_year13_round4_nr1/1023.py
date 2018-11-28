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

int main() {
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int Q;
	fin >> Q;
	for (int cas = 0; cas < Q; ++cas) {
		fout << "Case #" << cas + 1 << ": ";
		int N, M;
		fin >> N >> M;
		vector<pair<long long, pair<bool, long long>>> v;
		long long s = 0;
		forn(i, M) {
			long long o, e, p;
			fin >> o >> e >> p;
			long long d = e - o;
			s += (d * N - d * (d - 1) / 2) * p;
			s %= 1000002013;
			v.push_back(make_pair(o, make_pair(false, p)));
			v.push_back(make_pair(e, make_pair(true, p)));
		}
		srt(v);
		vector<pair<long long, long long>> st;
		long long t = 0;
		fori(i, v) {
			if (!v[i].second.first) {
				st.push_back(make_pair(v[i].first, v[i].second.second));
			} else {
				while (v[i].second.second > 0) {
					long long q = min(st.back().second, v[i].second.second);
					long long d = v[i].first - st.back().first;
					t += (d * N - d * (d - 1) / 2) * q;
					t %= 1000002013;
					v[i].second.second -= q;
					st.back().second -= q;
					if (st.back().second == 0)
						st.pop_back();
				}
			}
		}
		fout << ((s - t) % 1000002013 + 1000002013) % 1000002013 << endl;
	}
}