#include<iostream>
#include<algorithm>
#include<vector>
#include<iomanip>
#include<set>
using namespace std;
#define ll long long
#define ld long double
#define vi vector<int>
#define pb push_back
#define pii pair<int,int>
#define mp make_pair
#define st first
#define nd second
#define mini(a,b) a=min(a,(b))
#define maxi(a,b) a=max(a,(b))
#define RE(i,n) for(int i=0,_n=(n);i<_n;++i)
#define RI(i,n) for(int i=1,_n=(n);i<=_n;++i)
const int inf=1e9+5, nax=1e6+5;

int n, m;
string sl[10];

bool pol[10][10];

bool sprawdz(vi w)
{
	vi lan;
	lan.pb(w[0]);
	RI(i, w.size() - 1) {
		while((!lan.empty()) && !pol[lan.back()][w[i]])
			lan.pop_back();
		if(lan.empty()) return false;
		lan.pb(w[i]);
	}
	return true;
}

int main()
{
	ios_base::sync_with_stdio(0);
	int ile_t;
	cin >> ile_t;
	RI(test, ile_t) {
		cin >> n >> m;
		RE(i, n) cin >> sl[i];
		RE(i, n) RE(j, n) pol[i][j] = false;
		RE(_, m) {
			int a, b;
			cin >> a >> b;
			a--;
			b--;
			pol[a][b] = pol[b][a] = true;
		}
		
		bool jest_res = false;
		string res = "";
		
		vi w;
		RE(i, n) w.pb(i);
		do {
			if(sprawdz(w)) {
				string s;
				RE(i, w.size()) s += sl[w[i]];
				if((!jest_res) || s < res) {
					jest_res = true;
					res = s;
				}
			}
		} while(next_permutation(w.begin(), w.end()));
		
		cout << "Case #" << test << ": " << res << "\n";
	}
	return 0;
}
