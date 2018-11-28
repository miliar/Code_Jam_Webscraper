#include<map>
#include<set>
#include<list>
#include<cmath>
#include<queue>
#include<stack>
#include<cstdio>
#include<string>
#include<vector>
#include<complex>
#include<cstdlib>
#include<cstring>
#include<numeric>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<functional>
 
#define mp          make_pair
#define pb          push_back
#define all(x)      (x).begin(),(x).end()
#define rall(x)     (x).rbegin(),(x).rend()
#define rep(i,n)    for(int i=0;i<(n);i++)
#define rep2(i,d,n) for(int i=(d);i<(n);i++)
#define sz(s)       (s).size()
#define clr(a)      memset((a),0,sizeof(a))
#define mclr(a)     memset((a),-1,sizeof(a))
 
using namespace std;
 
typedef    long long          ll;
typedef    unsigned long long ull;
typedef    vector<bool>       vb;
typedef    vector<int>        vi;
typedef    vector<vb>         vvb;
typedef    vector<vi>         vvi;
typedef    pair<int,int>      pii;
typedef    vector<pair<int,int> > vpii;
 
const int INF=1<<30;
const double EPS=1e-9;
 
const int dx[]={1,0,-1,0},dy[]={0,-1,0,1};

int main(){
	int t;
	cin >> t;
	rep(lp,t){
		int a,b,k;
		vector<int> ans;
		cin >> a >> b >> k;
		rep(i,a){
			rep(j,b){
				ans.pb(i&j);
			}
		}

		int res = 0;
		rep(i,ans.size()){
			if(ans[i] < k){
				res++;
			}
		}

		cout << "Case #" << (lp+1) << ": " << res << endl;
	}
}