#include<iostream>
#include<algorithm>
#include<vector>
#include<cstring>
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

struct cmp {
	bool operator()(string a, string b) {
		int d = min(a.length(), b.length());
		RE(i, d) if(a[i] != b[i]) return a[i] < b[i];
		return a.length() < b.length();
	}
};

char sl[100][15];
int ile_sl, k; // k < 5 serwerow
int t[10];
vi odw[6];
int rodz[10];
vector<string> w[10];

int Badaj(int mask) { // -1 jesli nie ok
	RE(i, k)
		odw[i].clear();
	RE(i, ile_sl) {
		rodz[i] = mask % k;
		mask /= k;
		odw[rodz[i]].pb(i);
	}
	RE(i, k) if(odw[i].empty()) return -1;
	int res = 0;
	RE(serwer, k) {
		set<string> secik;
		RE(i, odw[serwer].size()) {
			int a = odw[serwer][i];
			RE(j, w[a].size()) 
				secik.insert(w[a][j]);
		}
		res += secik.size() + 1;
	}
	return res;
}

pii Test() {
	cin >> ile_sl >> k;
	RE(i, ile_sl) {
		w[i].clear();
		string s;
		cin >> s;
		//cout << ">>> uwaga:\n";
		while(!s.empty()) {
			w[i].pb(s);
			//cout << s << "\n";
			s.erase(s.end() - 1);
		}
	}
	int res = -1;
	int sposoby = 0;
	
	int M = 1; // k ^ ile_sl
	RE(_, ile_sl)
		M *= k;
	RE(mask, M) {
		int a = Badaj(mask);
		if(a > res) {
			res = a;
			sposoby = 1;
		}
		else if(a == res)
			sposoby++;
	}
	return mp(res, sposoby);
}

int main()
{
	ios_base::sync_with_stdio(0);
	int z;
	cin >> z;
	RI(i, z) {
		pii P = Test();
		cout << "Case #" << i << ": " << P.st << " " << P.nd << "\n";
	}	
	return 0;
}
