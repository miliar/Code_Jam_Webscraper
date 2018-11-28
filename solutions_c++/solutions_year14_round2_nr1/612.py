#include<iostream>
#include<algorithm>
#include<vector>
#include<iomanip>
#include<cstring>
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

char sl[105][105];
int poz[105], d[105];
vi w;

int TEST()
{
	int n;
	int res = 0;
	cin >> n;
	RE(i, n) cin >> sl[i];
	RE(i, 105) poz[i] = 0;
	RE(i, n) d[i] = strlen(sl[i]);
	while(true) {
		int konce = 0;
		RE(i, n) if(poz[i] == d[i]) konce++;
		if(konce == n) return res;
		if(konce > 0) return -1;
		w.clear();
		char lit = sl[0][poz[0]];
		RE(i, n) {
			if(sl[i][poz[i]] != lit) return -1;
			int a = 0;
			while(poz[i] < d[i] && sl[i][poz[i]] == lit) {
				poz[i]++;
				a++;
			}
			w.pb(a);
		}
		sort(w.begin(), w.end());
		int x = w[w.size() / 2];
		RE(i, n) res += abs(x - w[i]);
	}
	return 0;
}

int main()
{
	ios_base::sync_with_stdio(0);
	
	int ile_t;
	cin >> ile_t;
	RI(test, ile_t) {
		int a = TEST();
		if(a >= 0)
			cout << "Case #" << test << ": " << a << "\n";
		else
			cout << "Case #" << test << ": " << "Fegla Won" << "\n";
	}
	return 0;
}
