#include <iostream>
#include <cstdio>
#include <cstring>
#include <map>
#include <set>

using namespace std;

#define forsn(i,s,n) for(int i = (s);i < (int)(n);i++)
#define forn(i,n) forsn(i,0,n)
#define contains(x,c) (c.find(x) != c.end())

typedef long long int tint;
typedef pair<int, int> pii;

const int MOD = 1000002013;

map<int, tint> inicios;
map<int, tint> fines;
set<pii> sucesos; //suceso, 0 inicio, 1 fin.
map<int, tint> inicios_actuales;

void add_to_map(int k, tint v, map<int,tint>& map) {
	if (!contains(k, map)) {
		map[k] = 0;
	}
	map[k] += v;
}

tint cost(tint d, tint n) {
	if (!d) return 0;
	return ((d * n) - ((d * (d - 1)) / 2)) % MOD;
}

int main() {
	freopen("a.in","r",stdin);
	freopen("a.out", "w", stdout);
	int casos, n, m;
	scanf("%d",&casos);
	forn(caso, casos) {
		inicios.clear();
		fines.clear();
		inicios_actuales.clear();
		sucesos.clear();
		tint res = 0;
		scanf("%d %d",&n,&m);
		tint original = 0;
		forn(i, m) {
			int i, f, v;
			scanf("%d %d %d",&i,&f,&v);
			add_to_map(i, v, inicios);
			add_to_map(f, v, fines);
			sucesos.insert(make_pair(i, 0));
			sucesos.insert(make_pair(f, 1));
			original += ((cost(f - i, n) * v) % MOD);
		}
		for(typeof(sucesos.begin()) it = sucesos.begin();it != sucesos.end();it++) {
			//cout << it->first << ' ' << it->second << endl;
			if (!(it->second)) { //Es un inicio.
				inicios_actuales[it->first] += inicios[it->first];
			} else { //Es un fin. Hay que sacar genteeeee
				tint debo_sacar = fines[it->first];
				//cout << debo_sacar << endl;
				for(typeof(inicios_actuales.rbegin()) back_it = inicios_actuales.rbegin();
				     back_it != inicios_actuales.rend() && debo_sacar;back_it++) {
						 //cout << it->first << " SOY YO " << endl;
					//cout << back_it->first << " SOY YO " << endl;
					tint saco = min(inicios_actuales[back_it->first], debo_sacar);
					inicios_actuales[back_it->first] -= saco;
					debo_sacar -= saco;
					tint d = ((it->first) - (back_it->first));
					res += ((saco) * cost(d, n)) % MOD;
					res %= MOD;
					//cout << cost(d,n) << " PUU" << endl;
					//cout << saco << ' ' << back_it->first << ' ' << d << endl;
				}
			}
		}
		
		cout << "Case #" << caso + 1 << ": " << (original - res) << endl; //Cambiar el 5 :)
	}
}
