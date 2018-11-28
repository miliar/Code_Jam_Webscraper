#include <iostream>
#include <map>
#include <set>
#include <cstdint>
using namespace std;

#define P 1000002013

uint64_t sumnum(uint64_t n)
{
	return n*(n-1)/2;
}

uint64_t cost(uint64_t a, uint64_t b, uint64_t n)
{
	return sumnum(n)-sumnum(n-(b-a));
}

int main(void)
{
	int ti, tn;
	cin >> tn;
	for (ti = 1; ti <= tn; ti++) {
		uint64_t n, m;
		uint64_t ret = 0;
		cin >> n >> m;
		set<uint64_t> ev;
		map<uint64_t, uint64_t> fel, le, fent;
		for (int i = 0; i < m; i++) {
			uint64_t a, b, d;
			cin >> a >> b >> d;
			a--; b--;
			ev.insert(a);
			ev.insert(b);
			fel[a] += d;
			le[b] += d;
			ret = (ret + d*cost(a, b, n))%P;
		}
		for (uint64_t k : ev) {
			if (fel.find(k) != fel.end()) {
				fent[k] += fel[k];
			}
			if (le.find(k) != le.end()) {
				uint64_t x = le[k];
				for (auto it = fent.rbegin(); x > 0; ++it) {
					uint64_t y = min(x, it->second);
					it->second -= y;
					x -= y;
					ret = (ret - ((y*cost(it->first, k, n))%P) + P)%P;
				}
			}
		}
		
		cout << "Case #" << ti << ": " << ret << endl;
	}
	return 0;
}
