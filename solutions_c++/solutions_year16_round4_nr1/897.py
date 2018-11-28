#include <bits/stdc++.h>

using namespace std;
//memset
#define MEMSET_INF 127 // about 2B
#define set0(a) memset(a,0,sizeof(a));
#define setminus1(a) memset(a,-1,sizeof(a));
#define setinf(a) memset(a,MEMSET_INF,sizeof(a));

//stl
#define mp make_pair
#define pb push_back
//#define pc(x) putchar_unlocked(x)
//#define gc() getchar_unlocked()

//Loops
#define REP(i,n) for(int i = 0;i < (int)(n); i++)
#define REP1(i,a,b) for(int i = (int)(a);i <= (int)(b); i++)
#define REPMAP(i,mm) for(auto i = mm.begin();i !=mm.end(); i++)

//Sort
#define sortvec(vec) sort(vec.begin(), sort.end())

//Misc
#define LSOne(i) (i & (-i))	// the first Least Significant One-bit in i

//modulo
#define mod %
#define NUM 1000000007

#define LONG_LONG_MAX	9223372036854775807LL
#define LONG_LONG_MIN	(-LONG_LONG_MAX-1)

#define LMAX LONG_LONG_MAX
#define LMIN LONG_LONG_MIN
#define IMAX INT_MAX
#define IMIN INT_MIN
#define PI M_PI
#define EPS 1e-9
#define INF 1e9
#define M_PI		3.14159265358979323846
#define cin(x) scanf("%d",&x)
#define cout(x) printf("$d",x)
#define endl '\n'
#define s(n) scanf("%d",&n)
#define sll(n) scanf("%I64d",&n)
#define p(n) printf("%d",n)
#define pll(n) printf("%I64d",n)
#define all(v) (v).begin(),(v).end()

//typedef
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<string, int> msi;
typedef map<int, int> mii;
typedef tuple<int, int, int> iii;

#define MAX_N 100005
#define ROCK 'R'
#define PAPER 'P'
#define SCISSOR 'S'

int N,r,p,s;

bool ok(string ss){
	int R = 0, P = 0, S = 0;
	REP(i,ss.length()){
		if(ss[i] == ROCK)
			R++;
		else if(ss[i] == PAPER)
			P++;
		else
			S++;
	}
	if(R == r && S == s && P == p)
		return true;
	return false;
}

string make(int n, string ss){
//	cout<<n<< ""<<ss<<endl;
	if(n == 0)
	{
		return ss;
	}
	string str = make(n-1,ss);
//	cout<<str<<endl;
	ss.resize(2*str.length());
	for(int i = 0; i < (int)(2*str.length()); i+=2){
		if(str[i/2] == ROCK){
			ss[i] = 'R';
			ss[i+1] = 'S';
		}else if(str[i/2] == 'S'){
			ss[i] = 'P';
			ss[i+1] = 'S';
		}else{
			ss[i] = 'P';
			ss[i+1] = 'R';
		}
	}
//	string s1 = ss.substr(0,str.length());
//	string s2 = ss.substr(str.length());
//	if(s1 < s2)
//		ss = s1 + s2;
//	else
//		ss = s2 + s1;
	return ss;
}

void manage(string & s){
	for(int len = 2;len <s.length();len*=2){
		for(int i = 0; i <s.length();i+= 2*len){
			string s1 = s.substr(i,len);
			string s2 = s.substr(i+len,len);
			if(s2 < s1){
				int ind = 0;
				for(int j = i; j < i+len;j++){
					s[j] = s2[ind++];
				}
				ind = 0;
				for(int j = i+len; j < i+len*2;j++){
					s[j] = s1[ind++];
				}
			}
		}
	}
}

void solve() {

	cin>>N>>r>>p>>s;

	string s0 = make(N,"R");
	string s1 = make(N,"P");
	string s2 = make(N,"S");
	bool fg = 0;
	string ans;
	if(ok(s0)){
		manage(s0);
		if(fg == 0){
			ans = s0;
			fg = 1;
		}
	} if(ok(s1)){
		manage(s1);
		if(fg == 0){
			ans = s1;
			fg = 1;
		}else{
			ans = min(ans , s1);
		}
	} if(ok(s2)){
		manage(s2);
		if(fg == 0){
			ans = s2;
			fg = 1;
		}else{
			ans = min(ans , s2);
		}
	}
	if(fg == 0){
				cout<<"IMPOSSIBLE";

	}else{
		cout<<ans;
	}
}

int main() {

	cin.tie(0);
	cout.tie(0);
	cin.sync_with_stdio(0);
	cout.sync_with_stdio(0);

	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);

	int TC = 1;
	cin>>TC;
	for (int ZZ = 1; ZZ <= TC; ZZ++) {
		cout<<"Case #"<<ZZ<<": ";
//		clock_t start = clock();
//		double ans;
//		cout.precision(10);
//		cout<<fixed<<ans<<endl;
		solve();
//		clock_t end = clock();
		cout<<endl;
//		cerr <<"Time: " <<(double)(end-start)/CLOCKS_PER_SEC <<" seconds" <<endl;
	}
	return 0;
}
