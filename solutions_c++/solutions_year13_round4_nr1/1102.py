#include <iostream>
#include <vector>
#include <set>
#include <cassert>
using namespace std;

typedef long long ll;

const ll MOD = 1000002013;

typedef struct { ll l, r; mutable ll pop; } Tick;
bool operator<(Tick a, Tick b) {
	if(b.l != a.l) return a.l < b.l;
	if(b.r != a.r) return a.r < b.r;
	return false;
}

int main() {
	int numT;
	cin >> numT;
	for(int T = 1; T <= numT; ++T) {
		ll savings = 0;
		int N, M;
		cin >> N >> M;
		
		multiset<Tick> ticks;
		for(int m = 0; m < M; m++) {
			Tick t; cin >> t.l >> t.r >> t.pop;
			ticks.insert(t);
		}
		
		again: // inefficient but safe
		
		for(auto a = ticks.begin(); a != ticks.end();) {	
			auto b = a; ++b;
			// cerr << a->l << " " << a->r << " #" << a->pop << endl;
			
			while(b != ticks.end() && b->l == a->l) ++b;
			while(b != ticks.end() && b->l <= a->r) {
				if(b->r > a->r) {
					ll s = (b->l - a->l)*(b->r - a->r);
					ll p = min(a->pop, b->pop);
					if(p) {
						savings = (((s*p) % MOD) + savings) % MOD;
						
						a->pop -= p;
						b->pop -= p;
						
						ticks.insert(Tick{ a->l, b->r, p });
						ticks.insert(Tick{ b->l, a->r, p });
						
						// goto again;
					}
				}
				++b;
			}
			++a;
		}
		
		cout << "Case #" << T << ": " <<  savings << endl;
	}
}

