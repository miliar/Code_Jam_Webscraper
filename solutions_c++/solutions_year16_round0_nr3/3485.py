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
#define eb emplace_back

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



void main2(){
	cout<<endl;
	int N, J;
	cin >> N >> J;
	assert(N == 16 && J == 50);
	int found = 0;
	rep(mask, 1<<14){
		string s = "1";
		rep(i,14) s += mask>>i&1 ? '1' : '0';
		s += '1';
		vi ev;
		rep(b,2,11){
			long x = 0;
			rep(i,sz(s)){
				x *= b;
				x += s[i] - '0';
			}
			int ok = 0;
			for(long i = 2; i * i <= x; i++){
				if(x % i == 0){
					ev.eb(i);
					ok = 1;
					break;
				}
			}
			if(!ok){
				goto next;
			}
		}
		cout<<s;
		for(long e: ev)cout<<" "<<e;
		cout<<endl;
		if(++found == J)return;
		next:;
	}
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
