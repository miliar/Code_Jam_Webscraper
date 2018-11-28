#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#include <map>
#include <queue>
#include <stdlib.h>
#include <set>
#include <algorithm>
#include <math.h>
#include <stdio.h>
#include <unistd.h>
#include <stack>
#include <sstream>
#include <iomanip>
#include <bitset>
#define ff first
#define ss second

using namespace std;

typedef long long ll;

bool vis[10];
int cnt;

void check(ll i){
	int a;
	while(i != 0){
		a = i%10;
		if(!vis[a]){
			vis[a] = 1;
			cnt++;
		}
		i/=10;
	}
}

int main() {
	int t,n,tc=1;

	scanf("%d", &t);
	while(t--){
		scanf("%d", &n);		
		if(n == 0){
			printf("Case #%d: INSOMNIA\n", tc++);
			continue;
		}
		memset(vis,0,sizeof(vis));
		ll num = n;
		cnt = 0;
		while(cnt != 10){
			check(num);
			num += n;
		}
		printf("Case #%d: %lld\n", tc++, num-n);
	}

	return 0;
}
