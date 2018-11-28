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

const int max_n=10010;
int T;
int n,x;
int s[max_n];

int main() {
	gi(T);
	for(int z=1;z<=T;z++) {
		printf("Case #%d: ",z);
		gi(n); gi(x);
		rep(i,n) gi(s[i]);
		sort(s,s+n);
		int ans=0;
		int l=0,r=n-1;
		while(l<=r) {
			ans++;
			if(l==r)
				break;
			if((s[l]+s[r]<=x)) {
				l++; r--;
			}
			else r--;
		}
		printf("%d\n",ans);
	}
	return 0;
}
