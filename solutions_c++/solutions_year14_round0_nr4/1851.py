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

const int max_n=1010;

int process(string s) {
	int ret=0,d=100000;
	forup(i,2,(int)s.size()) {
		ret=ret*10+(s[i]-'0');
		d/=10;
	}
	ret*=d;
	return ret;
}

int T,n;
int nm[max_n],ken[max_n];

int main() {
	gi(T);
	rep(z,T) {
		gi(n);
		string x;
		rep(i,n) {
			cin>>x;
			nm[i]=process(x);
		}
		rep(i,n) {
			cin>>x;
			ken[i]=process(x);
		}
		sort(nm,nm+n);
		sort(ken,ken+n);
		/*rep(i,n) printf("%d ",nm[i]);
		printf("\n");
		rep(i,n) printf("%d ",ken[i]);
		printf("\n");*/
		int ans1=0,ans2=0;
		int l=0,r=n-1;
		rep(i,n)
			if(nm[i]>ken[l]) {
				ans1++;
				l++;
			}
			else r--;
		set<int> S;
		rep(i,n) S.insert(ken[i]);
		rep(i,n) {
			int cur=nm[i];
			set<int>::iterator it=S.upper_bound(cur);
			//printf("%d %d %d %d\n",i,cur,*it,(int)S.size());
			if(it!=S.end()) S.erase(it);
			else {
				ans2++;
				S.erase(S.begin());
			}
		}
		printf("Case #%d: %d %d\n",z+1,ans1,ans2);
	}
	return 0;
}
