#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define MP(X,Y) make_pair(X,Y)
#define SORT(X) (sort(X.begin(),X.end()))
#define SORTC(X,Y) (sort(X.begin(),X.end(),Y))
#define PUSH(X,Y) (X.push_back(Y))
#define two(X) (1<<(X))
#define twoL(X) (((LL)(1))<<(X))
#define FR(i, a, n) for(int i = (a); i < (int)(n); i++)
#define FRB(i, n, a) for(int i = (int)(n); i >= (int)(a); i--)
#define MS(x, y) memset(x, y, sizeof(x))
#define SZ(x) ((int) (x).size())
#define RZ(x,n,v) ((x).resize(n,v))
#define RI(x) scanf("%d", &x)
#define RII(x,y) scanf("%d %d", &x, &y)
#define RIII(x,y,z) scanf("%d %d %d", &x, &y, &z)
#define RL(x) scanf("%lld", &x)
#define RLL(x) scanf("%lld %lld", &x, &y)
#define RS(x) getline(cin,x)
#define PI(x) printf("%d\n", x)
#define PIG(x) printf("%d ", x)
#define PII(x,y) printf("%d %d\n",x,y)
#define PIIG(x,y) printf("%d %d ",x,y)
#define PL(x) printf("%lld\n", x)
#define PLG(x) printf("%lld ", x)
#define PLL(x,y) printf("%lld %lld\n", x,y)
#define PLLG(x,y) printf("%lld %lld ", x,y)
#define PS(x) cout<<x<<"\n"
#define PSG(x) cout<<x<<" "


typedef long long LL;
typedef vector<int> vi;
typedef vector<LL> vll;
typedef vector<string> vs;
typedef vector<double> vd;
typedef pair<int, int> pii;
typedef pair<LL, LL> pll;
typedef vector<pii> vpii;

const int MOD = 1000000007;
const double INF_LF = 1000000000000000000;
const int INF_INT = 2000000000;

template<class T> inline T sqr(T x){return x*x;} //square

template<class T> inline T gcd(T a,T b) //gcd
  {if(a<0)return gcd(-a,b);if(b<0)return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}

template<class T> inline T absval(T a) //absolute value
  {if(a<0)return -a;else return a;}

//from string to int
int toInt(string s){istringstream iss(s);int res;if(!(iss>>res))res = -1;return res;}
//from int to string
string toString(int a){ostringstream oss;oss<<a;return oss.str();}
//extracting tokens from string, delim is the delimiter
vector<string> getTokens(string s,char delim){vector<string> tokens;istringstream iss(s);string temp;while(getline(iss,temp,delim)){tokens.push_back(temp);}return tokens;}

const int MaxMatrixSize = 1000;//MaxMatrixSize
template<class T> inline void printMat(int n,T A[MaxMatrixSize][MaxMatrixSize]) //for printing matrix
  {for (int i=0;i<n;i++){for (int j=0;j<n;j++)cout<<A[i][j]<<" ";cout<<endl;}}

template<class T> inline void printVec(vector<T> A) //for printing matrix
  {for (int i=0;i<A.size();i++){cout<<A[i]<<"\n";}}

 template<class T> inline void readVec(vector<T>& A) //for printing matrix
  {for (int i=0;i<A.size();i++){cin>>A[i];}}

//distance between 2 points
double dist(double x1,double y1,double x2,double y2){return sqrt(sqr(x1-x2)+sqr(y1-y2));}
//square of distance between 2 points
double distR(double x1,double y1,double x2,double y2){return sqr(x1-x2)+sqr(y1-y2);}

//FOR COMPARISON BASED SORTING
class Compare {
public:
	bool operator()() {
		return true;
	}
};

//MAIN TASK SOLVING CLASS
class Codejam {
public:
	int task(string& s, int& smax) {
		int sum = s[0]-48;
		int fr = 0;

		FR(i,1,smax+1) {
			if(s[i]==0)
				continue;
			if(i>sum) {
				fr += (i-sum);
				sum = i+s[i]-48;
			} else {
				sum += (s[i]-48);
			}
		}

		return fr;
	}
};

//MAIN
int main() {
	freopen("TestSets/A-large.in","r",stdin);
	freopen("TestSets/Q1L.out","w",stdout);

	int t,smax;
	string s;
	cin>>t;
	Codejam cj = Codejam();
	int c = 1;

	while(t--) {
		cin>>smax;
		cin>>s;
		cout<<"Case #"<<c<<": "<<cj.task(s,smax)<<"\n";
		c++;
	}

	return 0;
}
