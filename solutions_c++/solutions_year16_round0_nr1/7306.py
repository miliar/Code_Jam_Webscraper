#include <iostream>
#include <time.h>
#include <vector>
#include <stdio.h>
#include <memory.h>
#include <string>
#include <map>
#include <algorithm>
#include <bitset>
#include <queue>
#include <set>
#include <time.h>
#include <assert.h>
#include <unordered_map>
#if !ONLINE_JUDGE
#include "inc.h"
#endif
using namespace std;
typedef long long ll;

const int N = 1e6 + 10;
int n;

int main() {
#if !ONLINE_JUDGE
	freopen("aa.txt", "r", stdin);
	freopen("bb.txt", "w", stdout);
	decTime;
#endif

	int t;
	scanf("%d",&t);
	for(int T=1;T<=t;++T){
		set<int>st;
		scanf("%d",&n);
		printf("Case #%d: ",T);
		if(!n){
			puts("INSOMNIA");
			continue;
		}
		int cnt=0;
		while(st.size()<10){
			++cnt;
			int tmp=cnt*n;
			while(tmp){
				st.insert(tmp%10);
				tmp/=10;
			}
		}
		printf("%d\n",cnt*n);
	}

#if !ONLINE_JUDGE
	//printTime;
#endif
	return 0;
}