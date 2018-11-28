//Aditya Dixit
#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <functional>
#include <algorithm>
#include <cstdlib>
#include <iomanip>
#include <stack>
#include <queue>
#include <deque>
#include <limits>
#include <cmath>
#include <numeric>
#include <set>

using namespace std;

#define gx getchar_unlocked
#define px putchar_unlocked
#define ps putchar_unlocked(' ')
#define pn putchar_unlocked('\n')
#define LIM
#define MOD 1000000007
#define pb push_back
#define mp make_pair
#define MEM(a, b) memset(a, (b), sizeof(a))
#define CLR(a) memset(a, 0, sizeof(a))
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define ABS(X) ( (X) > 0 ? (X) : ( -(X) ) )
#define rep(i,n) for(int i =0; i < n ; i++)
#define reps(i,x,y) for(int i =x; i < y ; i++)
#define repb(i,x,y) for(int i =x; i >= y ; i--)
#define all(a) a.begin(),a.end()
#define ff first
#define ss second
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define sqr(x) ((x)*(x))
#define EPS 1e-9

#ifndef ONLINE_JUDGE
#define TRACE
#endif

#ifdef TRACE
    #define trace(x)            cerr<<x<<endl;
    #define trace1(x)           cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<endl;
    #define trace2(x,y)         cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<" | "#y" = "<<y<<endl;
    #define trace3(x,y,z)       cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<" | "#y" = "<<y<<" | "#z" = "<<z<<endl;
    #define trace4(a,b,c,d)     cerr<<__FUNCTION__<<":"<<__LINE__<<": "#a" = "<<a<<" | "#b" = "<<b<<" | "#c" = "<<c<<" | "#d" = "<<d<<endl;
    #define trace5(a,b,c,d,e)   cerr<<__FUNCTION__<<":"<<__LINE__<<": "#a" = "<<a<<" | "#b" = "<<b<<" | "#c" = "<<c<<" | "#d" = "<<d<<" | "#e" = "<<e<<endl;
    #define trace6(a,b,c,d,e,f) cerr<<__FUNCTION__<<":"<<__LINE__<<": "#a" = "<<a<<" | "#b" = "<<b<<" | "#c" = "<<c<<" | "#d" = "<<d<<" | "#e" = "<<e<<" | "#f" = "<<f<<endl;
#else
    #define trace(x)
    #define trace1(x)
    #define trace2(x,y)
    #define trace3(x,y,z)
    #define trace4(a,b,c,d)
    #define trace5(a,b,c,d,e)
    #define trace6(a,b,c,d,e,f)
#endif


const int INF = 2000000000;
const double pi=acos(-1.0);

typedef long long int i64;
typedef long int i32;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef pair<int,PII> tri;

int main()
{
	freopen("aain.txt","r",stdin);
	freopen("aaout.txt","w",stdout);
	
	ios_base :: sync_with_stdio(false);
	cin.tie(0);

	int t,tt = 1;
	cin >> t;
	
	while(t--){
		int n;
		string s;
		cin >> n >> s;
		
		int sum = 0,ans = 0;
		
		rep(i,n+1){
			if( s[i] != '0'){
				if(i > sum ){
					ans += i-sum;
					sum = i;
				}
			}
			sum += s[i]-'0';
		}
		cout << "Case #" << tt++ << ": " << ans << endl;
	}
	return 0;
}
