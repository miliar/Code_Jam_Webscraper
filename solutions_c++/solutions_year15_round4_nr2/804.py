#include <bits/stdc++.h>

using namespace std;

inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}
template<class T> inline T sqr(T x) {return x*x;}

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef long long ll;

#define all(a)  (a).begin(),(a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define pb push_back
#define mp make_pair
#define each(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define exist(s,e) ((s).find(e)!=(s).end())
#define range(i,a,b) for(int i=(a);i<(b);++i)
#define rep(i,n)  range(i,0,n)
#define clr(a,b) memset((a), (b) ,sizeof(a))
#define dump(x)  cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;

const double eps = 1e-10;
const double pi  = acos(-1.0);
const ll INF =1LL << 62;
const int inf =1 << 29;

int n;
long double v,x;
long double r[110],c[110];

int main(void){
	int TestCase;
	cin >> TestCase;
	range(Number,1,TestCase+1){
		cin >> n;
		cin >> v >> x;
		rep(i,n) cin >> r[i]  >> c[i];
		if(n>=3) continue;

		double ans=0.0;
		if(n==1){
			if(c[0]==x)
				ans=v/r[0];
			else
				ans=-1.0;
		}else{
			if(c[0]==c[1]){
				if(c[0]==x)
					ans=v/(r[0]+r[1]);
				else
					ans=-1.0;
			}else{
				double val=r[0]*r[1]*(c[1]-c[0]);
				double t1=(r[1]*c[1]*v-r[1]*x*v)/val;
				double t2=(-r[0]*c[0]*v+r[0]*x*v)/val;
				if(t1<0.0||t2<0.0)
					ans=-1.0;
				else
					ans=max(t1,t2);
			}
		}
		cout.precision(10);
		cout << "Case #"<< Number << ": ";
		if(ans<0.0)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << fixed << ans << endl;
	}
	return 0;
}