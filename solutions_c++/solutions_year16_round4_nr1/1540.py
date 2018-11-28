#include <bits/stdc++.h>
using namespace std;
#define all(v) (v).begin(),(v).end()
#define pb(x) push_back(x)
#define REP(i,x,y) for(int (i)=(x);(i)<(y);(i)++)
#define REPIT(it,A) for(typeof(A.begin()) it = (A.begin()); it!=A.end();it++)
#define sqr(x) ((x)*(x))
#define mp(x,y) make_pair((x),(y))
#define fast_io() ios_base::sync_with_stdio(0);cin.tie(0); 
//#define NDEBUG 1
#define fst first
#define snd second
#define sz(v) ((int)v.size())
typedef vector<int> vi;
typedef unsigned int ui;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int,int> ii;
typedef vector<ii> vii;

int tc;
int n;
int a[3];

// 0 1 2
// P R S
// 0 > 1, 1 > 2, 2 > 0

string ans;
vi v;

vi id;
vi nxt;

int win(int u, int v){ // 1 for u wins, 0 for v wins
	return (u == 2 && v == 0) || (u == 0 && v == 1) || (u == 1 && v == 2);
}

set<int> s;

int check(){
	id.resize(v.size());
	REP(i,0,sz(v)) id[i] = i;

//	cerr << "Checking... " << endl;
	while (sz(id) >= 2){
//		string aux;
//		aux.clear();
//		REP(i,0,sz(id)){
//			if (v[id[i]] == 0) aux.pb('R');
//			if (v[id[i]] == 1) aux.pb('P');
//			if (v[id[i]] == 2) aux.pb('S');
//		}
//		cerr << aux << endl;

		nxt.clear();
		REP(i,0,sz(id)){
//			cerr << "sz(id): " << sz(id) << " ";
			if (i >= sz(id)-1) {
//				cerr << "single" << endl;
				nxt.pb(id[i]);
			}
			else {
//				cerr << "comparing " << v[id[i]] << " and " << v[id[i+1]] << endl;
				if (v[id[i]] == v[id[i+1]]) return 0;
				else if (win(v[id[i]], v[id[i+1]])) nxt.pb(id[i]);
				else nxt.pb(id[i+1]);
			}
			i++;
		}
		id = nxt;
	}
	
	ans.clear();
	REP(i,0,sz(v)){
		if (v[i] == 0) ans.pb('P');
		if (v[i] == 1) ans.pb('R');
		if (v[i] == 2) ans.pb('S');
	}
//	cerr << "OK: " << ans << endl;
	return 1;
}

int main(){
	fast_io();
	cin >> tc;
	REP(zz,1,tc+1){
		ans = "IMPOSSIBLE";
	
		cin >> n;
		v.clear();

		cin >> a[1] >> a[0] >> a[2];
		REP(i,0,3) REP(j,0,a[i]) v.pb(i);

		do{
			if (check()) break;
		} while (next_permutation(all(v)));

		cout << "Case #" << zz << ": " << ans << endl;
	}
	return 0;
}
