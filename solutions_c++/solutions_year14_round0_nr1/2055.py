#include <cstdio>
#include <iostream>
#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <functional>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef map<int,int> mii;
typedef vector<int> vi;
typedef vector< vector<int> > vvi;
typedef vector<string> vs;

#define rep(i,n) for(int i=0;i<(n);i++)
#define forup(i,a,b) for(int i=(a);i<(b);i++)
#define fordn(i,a,b) for(int i=(a);i>(b);i--)
#define all(x) x.begin(),x.end()
#define permute(x) next_permutation(all(x))
#define gi(x) scanf("%d",&x)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second

int T,r,x;

int main() {
	gi(T);
	rep(z,T) {
		vi fs,sc,v(8,0);
		gi(r); r--;
		rep(i,4)
			rep(j,4) {
				gi(x);
				if(i==r) fs.pb(x);
			}
		gi(r); r--;
		rep(i,4)
			rep(j,4) {
				gi(x);
				if(i==r) sc.pb(x);
			}
		sort(all(fs));
		sort(all(sc));
		vi::iterator it=set_intersection(all(fs),all(sc),v.begin());
		v.resize(it-v.begin());
		printf("Case #%d: ",z+1);
		if((int)v.size()==1) printf("%d\n",v[0]);
		else if(v.empty()) printf("Volunteer cheated!\n");
		else printf("Bad magician!\n");
	}
	return 0;
}
