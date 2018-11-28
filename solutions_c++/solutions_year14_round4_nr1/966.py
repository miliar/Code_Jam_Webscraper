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

multiset<int> cnj;

int main(){
	int n, t;
	scanf("%d",&t);
	rep(u,t){
		int x, rsp=0;
		scanf("%d %d",&n,&x);
		int g;
		cnj.clear();
		rep(i,n) scanf("%d",&g), cnj.insert(g);
		while(cnj.size()){
			int v = *cnj.rbegin();
			cnj.erase(cnj.find(v));
			multiset<int>::iterator it = cnj.upper_bound(x-v);
			if(it!=cnj.begin()){
				it--;
				cnj.erase(it);
			}
			rsp++;
		}
		printf("Case #%d: %d\n",u+1,rsp);
	}
	return 0;
}
