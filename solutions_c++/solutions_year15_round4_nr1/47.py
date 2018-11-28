// Enjoy your stay.

#include <bits/stdc++.h>

#define long long long
#define LOOPVAR_TYPE long

#define all(x) (x).begin(), (x).end()
#define sz(x) ((LOOPVAR_TYPE)(x).size())
#define foreach(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); it++)
#define GET_MACRO(_1, _2, _3, NAME, ...) NAME
#define _rep(i, n) _rep2(i, 0, n)
#define _rep2(i, a, b) for(LOOPVAR_TYPE i = (LOOPVAR_TYPE)(a); i < (LOOPVAR_TYPE)(b); i++)
#define rep(...) GET_MACRO(__VA_ARGS__, _rep2, _rep)(__VA_ARGS__)

#define fir first
#define sec second
#define mp make_pair
#define mt make_tuple
#define pb push_back

const double EPS = 1e-9;
const double PI = acos(-1.0);
const long INF = 1070000000LL;
const long MOD = 1000000007LL;

using namespace std;

typedef istringstream iss;
typedef stringstream sst;
typedef pair<LOOPVAR_TYPE, LOOPVAR_TYPE> pi;
typedef vector<LOOPVAR_TYPE> vi;

#include <sys/time.h>
long getTime(){
	struct timeval t;
	gettimeofday(&t, NULL);
	return t.tv_sec * 1000000LL + t.tv_usec;
}

int R, C;
char a[111][111];

int dy[] = {0, 1, 0, -1};
int dx[] = {1, 0, -1, 0};
string dir = ">v<^";

void main2(){
	cin>>R>>C;
	R+=2, C+=2;
	memset(a,0,sizeof(a));
	rep(i,1,R-1)rep(j,1,C-1){
		cin>>a[i][j];
	}
	int ans = 0;
	rep(i,1,R-1)rep(j,1,C-1)if(a[i][j] != '.'){
		int d = 0;
		while(a[i][j] != dir[d]) d++;
		int y = i, x = j;
		int ok = 0;
		while(1){
			y += dy[d], x += dx[d];
			if(a[y][x] != '.'){
				if(a[y][x] == 0){
					break;
				}else{
					ok = 1;
					break;
				}
			}
		}
		if(!ok){
			int ok2 = 0;
			rep(nd,4)if(nd != d){
				y = i, x = j;
				while(1){
					y += dy[nd], x += dx[nd];
					if(a[y][x] != '.'){
						if(a[y][x] == 0){
							break;
						}else{
							ok2 = 1;
							break;
						}
					}
				}
			}
			if(ok2 == 0){
				//cout<<i<<" "<<j<<endl;
				cout<<"IMPOSSIBLE"<<endl;
				return;
			}
			ans++;
		}
	}
	cout<<ans<<endl;
}

int main(){
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	
	
	int T;
	cin >> T;
	long start = getTime(), pre = start;
	rep(tc, 1, T + 1){
		cout << "Case #" << tc << ": ";
		main2();
		long now = getTime();
		cerr << tc << "/" << T << ": " << (now - pre) / 1000000. << endl;
		if(tc == T){
			cerr << "Total: " << (now - start) / 1000000. << endl;
			cerr << "  Ave: " << (now - start) / 1000000. / T << endl;
		}
		pre = now;
	}
}
