
#include <vector>
#include <list>
#include <map>
#include <set>
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
 
#define debug(x) cout<<#x<<" = "<<x<<"\n"
#define print(x) cout<<x<<endl
#define REP(i,n) for(int (i)=0;(i)<(n);(i)++)
#define FOR(i,a,n) for(int (i)=a;(i)<(n);(i)++)  
#define INF (1<<29) 
#define pb push_back 
#define sz size() 
#define ln length() 
#define mp make_pair 
#define all(a) a.begin(),a.end() 
#define fill(ar,val) memset(ar,val,sizeof ar) 
#define sqr(x) ((x)*(x)) 
#define min(a,b) ((a)<(b)?(a):(b)) 
#define max(a,b) ((a)>(b)?(a):(b)) 
 
using namespace std;
 
 
typedef int I;
typedef string STR;
typedef long long LL;
typedef map<I,I> MII;
typedef vector<I> VI;
typedef long double LD;
typedef vector<LL> VLL;
typedef vector<STR> VS;
typedef vector<VI> VVI;
typedef map<STR,I> MSI;
typedef map<I,MII> MMI;
typedef stringstream SS;
typedef map<char,I> MCI;
typedef map<STR,STR> MSS;

int main()
{
	freopen("C-large-1.in","r",stdin);
	freopen("C-large-1-output.in","w",stdout);
		
	int t;
	LL a,b,res;
	int tc = 1;
	LL ans[] = { 4004009004004,4000008000004,1234567654321,1232346432321,1214428244121,1212225222121,1210024200121,1024348434201,
				 1022325232201,1020304030201,1004006004001,1002003002001,1000002000001,40000800004,12345654321,12102420121,10221412201,
				 10000200001,404090404,400080004,125686521,123454321,121242121,104060401,102030201,100020001,4008004,1234321,1002001,44944,
				 40804,14641,12321,10201,484,121,9,4,1
			   };
	cin>>t;
	while(tc<=t){
		cin>>a>>b;
		res = 0;
		LL i;
		for(i=38;i>=0;i--){
			if(ans[i] >=a && ans[i] <= b){
				res++;
			}
		}
		cout<<"Case #"<<tc<<": "<<res<<endl;
		tc++;
	}
	return 0;
}
