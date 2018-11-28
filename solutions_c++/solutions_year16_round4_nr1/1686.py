#include <bits/stdc++.h>
using namespace std;
#define all(v) (v).begin(),(v).end()
#define pb push_back
#define sqr(x) ((x)*(x))
#define mp make_pair
#define EPS 1e-9
#define REP(i,x,y) for(int (i) = (x) ; (i) < (y) ; ++(i))
#define REPIT(it,A) for(__typeof(A.begin()) it = (A.begin()); it!=A.end();it++)
#define ones(x) __builtin_popcount(x)
#define fast_io() ios_base::sync_with_stdio(0);cin.tie(0);
#define debug(x) cout << #x << ": " << x << endl;
#define fst first
#define snd second
#define itm1 fst.fst
#define itm2 fst.snd
#define itm3 snd
#define mt(a,b,c) mp(mp(a,b),c)


typedef pair<int,int> ii;
typedef vector<int> vi;
typedef long long ll;
typedef pair<ll,ll> ill;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<ii, int> tri;
typedef pair<int,bool> ib;
typedef unsigned int ui;

const int INF = 2e9;
const int MAXN = 1e5 + 5;
const ll MOD = 1e9 + 7;


string bestP;
string bestR;
string bestS;
int ff[5000];
// P es 1 , R es 2  y S es 3
// 1 -> 1 2
// 2 -> 2 3
// 3 -> 1 3
int n;
int R, P ,S;

int win(int a, int b){
	if(a == b) return -1;
	return 3 - a - b;
}

int pot32[10];
int main(){
	fast_io();	
	int T;
	cin >> T;
	string ans = "";
	pot32[0] = 3;
	pot32[1] = 9;
	pot32[2] = 81;
	pot32[3] = 6561;
	int tmp[5000];
	for(int tc = 1 ; tc <= T ; ++tc){
		cin >> n >> R >> P >> S;
		string ans = "a";
		for(int i = 0 ; i < pot32[n] ; ++i){
			int m = i;
			for(int k = 0 ; k < (1 << n) ; ++k){
				ff[k] = m % 3;
				m /= 3;
			}
			string ret = "";
			int np = 0, nr = 0, ns = 0;
			for(int j = 0 ; j < (1 << n) ; ++j)
			if(ff[j] == 0) ret += 'P', np++;
			else if(ff[j] == 1) ret += 'R', nr++;
			else if(ff[j] == 2) ret += 'S', ns++;
			int tt = (1 << n);
			bool ok = 1;
			while(tt != 1){
				
				for(int j = 0 ; j < tt/2 ; ++j) 
				tmp[j] = win(ff[2*j], ff[2*j +1]);
				for(int j = 0 ; j < tt/2 ; ++j){
					if(tmp[j] == -1){
						ok = 0 ; break;
					}
					ff[j] = tmp[j];
				}
				tt /= 2;
				
			}
			if(np != P || ns != S || nr != R) ok = 0;	
			if(ok) ans = min(ans, ret);
	
		}	
		cout << "Case #" << tc << ": ";
		if(ans == "a") cout << "IMPOSSIBLE" << endl;
		else cout << ans << endl;



	}
	return 0;

}













