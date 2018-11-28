#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<iomanip>
using namespace std;
#define ll long long
#define ld long double
#define vi vector<int>
#define pb push_back
#define mini(a,b) a=min(a,(b))
#define maxi(a,b) a=max(a,(b))
#define RE(i,n) for(int i=0,_n=(n);i<_n;++i)
#define RI(i,n) for(int i=1,_n=(n);i<=_n;++i)
#define pii pair<int,int>
#define mp make_pair
#define st first
#define nd second
const int nax = 1e3+5, inf = 1e9 + 5;

int hp[nax], gold[nax];
int ona, wieza, n;

vi f(int x) {
	vi odp;
	RE(ile_wieza, 15) {
		int ile_ona = 0;
		while(x > 0) {
			ile_ona++;
			x -= ona;
		}
		x += ona * ile_ona;
		odp.pb(ile_wieza - ile_ona);
		x -= wieza;
		if(x <= 0) return odp;
	}
	RE(_, 50) cout << "dupa\n";
	return odp;
}

int t[nax], nowy[nax];

void Test()
{
	cin >> ona >> wieza >> n;
	RE(i, n) cin >> hp[i] >> gold[i];
	RE(i, nax) t[i] = -inf;
	t[1] = 0;
	RE(iii, n) {
		vi w = f(hp[iii]);
		RE(i, nax) nowy[i] = t[i];
		RE(w_id, w.size()) {
			int a = w[w_id];
			if(a >= 0) {
				for(int i = nax - 1; i >= 0; --i)
					if(t[i] >= 0) {
						if(i + a >= nax) {
							RE(_, 500) cout << "slabo\n";
						}
						maxi(nowy[i + a], t[i] + gold[iii]);
					}
			}
			else {
				RE(i, nax) if(t[i] >= 0 && i + a >= 0)
					maxi(nowy[i + a], t[i] + gold[iii]);
			}
		}
		int x = hp[iii];
		int licz = 0;
		while(x > 0) {
			licz++;
			x -= wieza;
		}
		RE(i, nax - licz) maxi(nowy[i + licz], t[i]);
		RE(i, nax) maxi(t[i], nowy[i]);
	}
	int res = 0;
	RE(i, nax) maxi(res, t[i]);
	cout << res << "\n";
}

int main() {
	ios_base :: sync_with_stdio(0);
	int z;
	cin >> z;
	RI(i, z) {
		cout << "Case #" << i << ": ";
		Test();
	}
	return 0;
}