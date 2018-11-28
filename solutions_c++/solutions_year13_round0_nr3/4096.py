#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <ctime>
#include <string.h>
using namespace std;

#define rep(i,a) for((i)=0;(int)(i)<(a);(i)++)
#define rrep(i,a,b) for((i)=(a);(i)>=(b);(i)--)
#define maX(a,b) ((a)>(b)?(a):(b))
#define miN(a,b) ((a)<(b)?(a):(b))
#define pb(x) push_back(x)
#define pii pair<int,int>
#define pis pair<int,string>
#define psi pair<string,int>
#define pss pair<string,string>
#define ll long long
#define ull unsigned long long
#define fi first
#define se second
#define re return
#define sz(x) ((int)(x).size())
#define vi vector<int>
#define vs vector<string>
#define vpii vector< pii >
#define S(x) scanf("%d",&x)

template<class T> T abs(T x){return x>0?x:-x;}
inline int toInt(string s) {int v;istringstream sin(s);sin>>v;return v;}
inline ll toll(string s) {ll v;istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}
template<class T> inline T sqr(T x) {return x*x;}
template<class T> inline T gcd(T a,T b) {if (a<0) a=-a;if (b<0) b=-b;return (b==0)?a:gcd(b,a%b);}
template<class T> inline T lcm(T a,T b) {return a*(b/gcd(a,b));}
ull V[39]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};

int cal(ull n)
{
    int res=0,i;
    rep(i,39)   if(V[i]<=n) res++;
    return res;
}
void solve()
{
    ull A,B;
    cin>>A>>B;
    cout<<cal(B)-cal(A-1)<<endl;
	
}
int main()
{
		int totTC,testCase;
		cin>>totTC;
		for(testCase=1;testCase<=totTC;testCase++){
			printf("Case #%d: ",testCase);
			solve();
		}
        return 0;
}

