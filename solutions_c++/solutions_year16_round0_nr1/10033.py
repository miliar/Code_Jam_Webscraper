#include <iostream>
#include <vector>
#include <queue>
#include <chrono>
using namespace std;
#define DB(a) << #a " == " << (a) << ";	"
#define REP(n) for (int i = 0; i < int(n); ++i)
#define FOR(i,n) for (int i = 0; i < int(n); ++i)
#define SEG(i,a,b) for (int i = (a); i <= (b); ++i)
#ifdef DBG
#define WR(things_to_wrap) things_to_wrap
int __GOV = 0, __GOVTH = int(2e9);
#define OP {if (++__GOV > __GOVTH) cerr << "exit(1): __GOV exceeded " << __GOVTH << endl, exit(1);}
#else
#define WR(things_to_wrap)
#define OP
#endif
#define CR(text_to_cerr) WR(cerr << "" text_to_cerr << endl;)
typedef long long int lli;

const int NMAX = (int)2e5;
bool d[10];
int cs = 0;
WR(int maxlocgov = 0; int maxn = -1;)

inline void chdgt(lli n){
	CR("checking digits from " DB(n))
	do {
		if (!d[n%10]){
			++cs;
			d[n%10] = true;
			CR("increased: " DB(cs) << "with " << n%10)
		}
		n /= 10;
	} while (n);
}

void solve(){
	REP(10) d[i] = false; cs = 0;
	int N; cin >> N;
	WR(/*if (!(N%1007))*/ cerr << endl << "got to explore " DB(N) << endl;)
	if (!N) {
		cout << "INSOMNIA" << endl;
		CR("ans is INSOMNIA");
		return;
	}
	lli n = 0;
	WR(int locgov = 0;)
	while (cs != 10) { OP
		chdgt(n += N);
		WR(++locgov;)
	}
	cout << n << endl;
	CR("ans is " << n);
	WR(/*if (!(N%1007))*/ cerr << "finished in " << locgov << " increments.\n"; if (maxlocgov < locgov) { maxlocgov = locgov; maxn = N;})
}

int main(){ // WR(srand(chrono::system_clock::now().time_since_epoch().count());)
	int T; scanf("%d", &T);
	SEG(t,1,T){
		fprintf(stderr, "solving case %d...\n", t);
		printf("Case #%d: ", t);
		solve();
	}
	WR(cerr << "\nworst case was: " DB(maxlocgov) DB(maxn) << endl;)
	return 0;
}
