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
		int n, v[1010], m=0, ret;
		scanf("%d", &n);
		for(int i=0;i<n;++i) {
			scanf("%d", &v[i]);
			m = max(m,v[i]);
		}
		ret = m;
		for(int i=1;i<m;i++) {
			int tmp = i;
			for(int j=0;j<n;j++) {
				if(v[j] > i) {
					tmp  += (v[j]+i-1)/i - 1;
				}
			}
			ret = min(ret,tmp);
		}
		printf("Case #%d: %d\n", caso, ret);
	}
	return 0;
}
