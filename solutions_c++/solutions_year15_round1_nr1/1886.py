#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;
#define pb(X) push_back(X)
#define mp(X,Y) make_pair(X,Y)
#define sz(X) (int)X.size()
#define clr(X) memset(X,0,sizeof(X));
#define xx first
#define yy second
typedef pair<int, int> pii;
typedef long long ll;
typedef unsigned long long ull;

int main(){
	int T;
	scanf("%d", &T);
	for(int caso=1;caso<=T;caso++) {
		int md = 0,n, v[1010], s=0, s2=0;
		scanf("%d",&n);
		for(int i=0;i<n;i++) {
			scanf("%d",&v[i]);
		}
		for(int i=0;i<n-1;i++) {
			int d = v[i] - v[i+1];
			if(d>0) s+=d;
			if(d > md) md = d;
		}
		for(int i=0; i<n-1; i++) {
			s2 += min(md,v[i]);
		}
		printf("Case #%d: %d %d\n",caso,s,s2);
	}
	return 0;
}
