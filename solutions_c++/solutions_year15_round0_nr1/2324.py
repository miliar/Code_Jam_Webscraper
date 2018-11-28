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
char s[10000];
int n;
int have[10000];
int main() {
	scanf("%d", &TT);
	for(int rr=1; rr<=TT; ++rr){
		int ans = 10000;
		int sum = 0;
		scanf("%d", &n);
		scanf("%s", s);
		for(int i=0; i<=n; ++i){
			have[i] = s[i] - '0';
			sum += have[i];
		}
		for(int i=0; i<=1100; ++i){
			int now = i;
			for(int j=0; j<=n; ++j){
				if(now >= j) now += have[j];
			}
			if(now == i + sum) 
				ans = min(ans, i);
		}
		printf("Case #%d: %d\n", rr, ans);
	}
	return 0;
}

