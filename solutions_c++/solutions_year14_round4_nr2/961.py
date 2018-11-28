#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>

#include <iostream>
#include <iomanip>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <complex>
#include <functional>
#include <numeric>
#define MOD 1000000007

using namespace std;

template<class T> void pv(T a, T b) { for (T i = a; i != b; ++i) cout << *i << " "; cout << endl; }

typedef long long ll;

#define F first
#define S second
#define mp make_pair
#define fr(i,a,b) for(int i=a;i<b;i++)
#define rep(x,y) for(int(x)=(0);(x)<(y);(x)++)
#define dbg(x) cout << #x << " == " << x << endl
#define _ << " _ " <<
#define oo 100000000
#define N 1010
bool mk[N];
int ls[N], pos[N], g[N];
int n;

int main(){
	int t;
	scanf("%d",&t);
	rep(u,t){
		scanf("%d",&n);
		rep(i,n){
			scanf("%d",&g[i]);
		}
		rep(i,n) mk[i]=false;
		int rsp=0;
		rep(i,n){
			int p=-1;
			rep(j,n){
				if(mk[j]==false && (p==-1 || g[j]<g[p])) p = j;
			}
				int a=0,b=0;
			rep(j,n){
				if(j != p && mk[j]==false){
					if(j<p) a++;
					else b++;
				}
			}
			mk[p]=true;
			rsp += min(a,b);
		}
		printf("Case #%d: %d\n",u+1,rsp);
	}
	return 0;
}
