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

int num[1010];

int main(void){
	int TestCase;
	cin >> TestCase;
	range(Number,1,TestCase+1){
		int d;
		cin >> d;
		rep(i,1010) num[i]=0;
		int ans=0;
		rep(i,d){
			int in;
			cin >> in;
			num[in]++;
			ans=max(ans,in);
		}
		int limit=ans;
		range(i,1,limit+1){
			int cur=0;
			range(j,i+1,limit+1){
				int cmin=inf;
				range(k,1,j+1){
					int num=j/k;
					if(j%k) num++;
					if(num<=i) cmin=min(cmin,k-1);
				}
				cur+=cmin*num[j];
			}
			ans=min(ans,cur+i);
		}
		cout << "Case #"<< Number << ": ";
		cout << ans << endl;
	}
	return 0;
}


// min(D,1+max(D-i,i))
// maximum{D}
// min(D,1+D/2)
// min(D/2,2+D/6)
// min(D,1+2*(2+D/6))
// min(D,5+D/6)
// 9 ,1+5,2+3,3+3
