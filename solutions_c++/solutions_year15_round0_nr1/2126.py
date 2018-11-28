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
		int n, sum=0, ret = 0;
		char s[1010];
		scanf("%d %s", &n, s);
		for(int i=0; s[i]; ++i) {
			int val = s[i] - '0';
			if(val) {
				if(sum < i) {
					ret += i-sum;
					sum = i;
				}
			}
			sum += val;
		}
		printf("Case #%d: %d\n", caso, ret);
	}
	return 0;
}
