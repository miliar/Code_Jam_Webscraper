#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;
const int inf = 1000000000;
const int N = 50005;
typedef long long LL;

bool ok(int x){
	int a[15], c = 0;
	while (x){
		a[c++] = x % 10;
		x /= 10;
	}
	for (int i = 0,j = c-1; i <= j; ++i,--j)
		if (a[i] != a[j]) return false;
	return true;
}
bool judge(int x){
	int tmp = (int)sqrt(1.0 * x);
	if (tmp * tmp != x) return false;
	if (ok(x) && ok(tmp)) return true;
}
int main(){
	int T, a, b;
	scanf("%d", &T);
	for (int cs = 1; cs <= T; ++cs){
		scanf("%d%d", &a, &b);
		int ans = 0;
		for (int i = a; i <= b; ++i){
			if (judge(i)) ans++;
		}
		printf("Case #%d: %d\n", cs, ans);
	}
	return 0;
}