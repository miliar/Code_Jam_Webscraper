    using namespace std;
#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <cstring>
#include <string>

#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)

#define SET(a,x) memset((a),(x),sizeof(a))
#define COPY(a,b) memcpy((a),(b),sizeof(a))
// set = 0
#define PB push_back
#define TR(c,it) for(typeof(c.begin()) it=c.begin();it!=c.end();it++)

#define EXIST(c,x) (c.find(x)!=c.end())

typedef long long LL;
typedef pair<int,int>II;
typedef pair<int,II>III;

#define ST first
#define ND second

typedef vector<int>VI;
typedef vector<VI>VVI;
typedef vector<II>VII;
typedef vector<VII>VVII;

int ntest,n,x,s[11111];

int main(){

	freopen("A-large.in","r",stdin);
	freopen("out","w",stdout);

	cin >> ntest;
	FOR(test,1,ntest){

		cin >> n >> x;
		FOR(i,1,n) cin >> s[i];

		sort(s+1,s+n+1);
		int l = 1, r = n;
		int res = 0;
		while(l <= r){
			if(s[r] + s[l] <= x){
				res++;
				l++;
				r--;
			} else{
				r--;
				res++;
			}
		}
		cout << "Case #"<<test<<": "<<res <<endl;
	}


	return 0;
}