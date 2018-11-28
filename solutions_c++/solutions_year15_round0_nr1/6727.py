#include <bits/stdc++.h>
using namespace std;

#define TRACE(x...) x
#define WATCH(x) TRACE(cout << #x" = " << x << endl)
#define PRINT(x...) TRACE(printf(x))

#define FOR(i, a, b, s) for(int i=(a); i<(b); i+=(s))
#define REP(i, n) for(int i=0; i<n; ++i)

#define all(v) (v).begin(),(v).end()
#define sz(c) int((c).size())
#define mod(a, b) ((((a)%(b))+(b))%(b))

#define gc getchar
#define pc putchar
#define pb push_back
#define mp make_pair

const double EPS = 1e-8;
const int INF = 0x3F3F3F3F;
const int NEGINF = 0xC0C0C0C0;

typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vi> vvi;
typedef long long ll;
typedef vector<ll> vll;
typedef pair<int,int> pii;


// Fast input
template<typename T>
inline void read(T &n) {
    n = 0; char ch = gc; int sign = 1;
    while(ch < '0' || ch > '9'){if(ch == '-') sign = -1; ch = gc; }
    while(ch >= '0' && ch <= '9') { n = n*10 + ch - '0'; ch = gc; }
    n *= sign; }

// Fast output
template<typename T>
inline void write(T num) {
	long n=num, i=0; char ch[19];
	if(n == 0) pc('0');
	while(n > 0) { ch[i++] = n % 10 + '0'; n /= 10; }
	while(i > 0) { pc(ch[i-1]); i--; }
	pc('\n'); }

int cmp(double x, double y=0, double tol=EPS) {
    return (x <= y+tol) ? (x+tol < y) ? -1 : 0 : 1;
}

int main( int argc, const char* argv[] ) {
    ifstream infile(argv[1]);
    ofstream outfile(string(FILE_NAME) + ".out");
    int T, t=0; infile >> T;
    string ansStr;
    while(t++ < T) {
	ansStr = "Case #" + to_string(t) + ": ";

	int strLen;
	infile >> strLen;
	string shyness;
	infile >> shyness;
	int ppl = 0; // number of people standing
	int friends = 0; // number of friends needed
	REP(i, strLen+1) {
	    if(ppl < i) {
		friends += i-ppl;
		ppl = i + (shyness[i] - '0');
	    } else {
		ppl += (shyness[i] - '0');
	    }
	    cout << "n=" << shyness[i]-'0' << ", ppl=" << ppl << ", friends=" << friends << endl;
	}
	ansStr += to_string(friends);
	
	outfile << ansStr << "\n";

	//int temp; cin >> temp;
    }
    infile.close();
    outfile.close();
    return 0;
}
