#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cstdlib>
#include<cmath>
#include<cctype>
#include<ctime>
#include<algorithm>
#include<iomanip>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<cassert>
#include<bitset>

using namespace std;
int TT;
int n;
const int N = 1e3+100;
int a[N];
int main() {
	scanf("%d", &TT);
	for(int rr = 1; rr<=TT; ++rr){
		scanf("%d", &n);
		int ans=0;
		for(int i=0; i<n; ++i){
			scanf("%d", a+i);
			ans = max(ans, a[i]);
		}
		for(int i=1; i<=ans; ++i){
			int t = i;
			for(int j=0; j<n; ++j){
				t += (a[j] - 1) / i;
			}
			ans = min(ans, t);
		}
		printf("Case #%d: %d\n", rr, ans);
	}
	return 0;
}

