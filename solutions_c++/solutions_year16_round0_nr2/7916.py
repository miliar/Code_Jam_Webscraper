//FRUSTRATED
#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
#define lb lower_bound
#define ub upper_bound
#define pb push_back
#define mp make_pair
#define ll long long
#define fi(filename) freopen(filename, "r", stdin)
#define fo(filename) freopen(filename, "w", stdout)
#define popcount(i) __builtin_popcount(i)      //count one. in long long use __builtin_popcountll(i)
#define gcd __gcd
//debug
#define debug(args...) cerr<<__FUNCTION__<<":"<<__LINE__<<" ";do{cerr<<#args<<": ";dbg,args;cerr<<endl;} while(0)
struct debugger
{template<typename T> debugger& operator ,(const T& v){cerr<<v<<" ";return *this;}}dbg;
#define dbgarr(a,start,end) cerr<<__FUNCTION__<<":"<<__LINE__<<"\n";for(ll i=start;i<end;i++) cerr<<#a<<"["<<i<<"] -> "<<a[i]<<" "<<endl;
#define dbgmat(mat,row,col) cerr<<__FUNCTION__<<":"<<__LINE__<<"\n";for(ll i=0;i<row;i++) {for(ll j=0;j<col;j++) cerr<<mat[i][j]<<" ";cerr<<endl;}
#define F(i,a,n) for(int i=(a);i<(n);++i)
#define R(i,a,n) for(typeof(a) i=(a);i>=(n);--i)
#define tr(it,container) for(typeof(container.begin()) it = container.begin(); it != container.end(); ++it)
//scan
#define fastio	  ios_base::sync_with_stdio(0);cin.tie()
#define SS(args...) do{input,args;} while(0)
struct scanner
{template<typename T> scanner& operator ,(T& v){cin>>v;return *this;}}input;
#define S(x) scanf("%d",&x)
#define Sl(x) scanf("%lld",&x)
#define P(x) printf("%d\n",x)
#define Pl(x) printf("%lld\n",x)
#define M(x,i) memset(x,i,sizeof(x))      // useful to clear array of integer
#define fr first
#define se second
#define INF 2147483647
#define MOD 1000000007   //	(int)1e9+7
#define all(x)    x.begin(),x.end()
#define get getchar//_unlocked
#define put putchar//_unlocked
inline void scan(int &n) {
	n=0;
	register char p;
	do {p=get();}while(p<'0');
	while(p>='0') {
		n = (n<<3) + (n<<1) + (p - '0');
		p=get();
	}
}
inline void print(int X)
{
	int Len=-1;
	char Data[10];
	do {
		Data[++Len]=X%10+'0';
		X/=10;
	} while(X);
	while(Len>=0) put(Data[Len--]);
	put('\n');
}
int bfs(string s,int n) {
	map<string,int> used;
	used[s]=0;
	queue<string> q;
	string t;
	q.push(s);
	while(!q.empty()) {
		s=q.front();q.pop();
		if(s.find("-")==string::npos) return used[s];
		F(i,0,n) {
			t=s.substr(0,i+1);
			F(i,0,t.length()) {
				if(t[i]=='+') t[i]='-';
				else t[i]='+';
			}
			t=t+s.substr(i+1);
			if(used.find(t)==used.end()) {
				used[t]=used[s]+1;
				q.push(t);
			}
		}
	}
	return 0;
}
int main() {
	fi("B-large.in");
	fo("out.txt");
	int t,n,no=0;
	char s[105];
	int dp[105][2];
	S(t);
	while(t--) {
		scanf("%s",s);
		n=strlen(s);
		if(s[0]=='-') {
			dp[0][0]=0;
			dp[0][1]=1;
		}
		else {
			dp[0][0]=1;
			dp[0][1]=0;
		}
		F(i,1,n) {
			if(s[i]=='+') {
				dp[i][0]=min(dp[i-1][0]+2,dp[i-1][1]+1);
				dp[i][1]=min(dp[i-1][0]+1,dp[i-1][1]);
			}
			else {
				dp[i][0]=min(dp[i-1][0],dp[i-1][1]+1);
				dp[i][1]=min(dp[i-1][0]+1,dp[i-1][1]+2);
			}
		}
	//	debug(s,min(dp[n-1][0]+1,dp[n-1][1]),bfs(string(s),n));
		printf("Case #%d: %d\n",++no,min(dp[n-1][0]+1,dp[n-1][1]));
	}
	return 0;
}
