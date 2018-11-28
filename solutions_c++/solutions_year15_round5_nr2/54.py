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

const int N = 1100;
int in[N];
int low[N];
int high[N];
int tmp[N];
int main() {
	int TT;
	scanf("%d", &TT);
	for(int cc = 1; cc <= TT; ++cc){
		int n, k;
		memset(low, 0, sizeof(low));
		memset(high, 0, sizeof(high));
		memset(tmp, 0, sizeof(tmp));
		scanf("%d%d", &n, &k);
		for(int i = 0; i<n - k + 1; ++i){
			scanf("%d", in + i);
		}
		int cnt = 0;
		for(int i=0; i<n - k; ++i){
			int now = in[i+1] - in[i] + tmp[cnt];
			low[cnt] = min(low[cnt], now);
			high[cnt] = max(high[cnt], now);
			tmp[cnt] = now;
			cnt ++;
			if(cnt == k)cnt = 0;
		}
		long long need = 0;
		int maxx = 0;
		for(int i=0; i<k; ++i){
			high[i] -= low[i];
			need -= low[i];
			maxx = max(maxx, high[i]);
		}
		long long up = (in[0] - need);
		if(up > 0) up %= k;
		else{
			up = k - (-up % k);
			if(up == k) up = 0;
		}
		long long hh = 0;
		for(int i=0; i<k; ++i){
			if(high[i] < maxx) hh+= maxx - high[i];
		}
		if(hh < up){
			++maxx;
		}
		printf("Case #%d: %d\n", cc, maxx);
	}
	return 0;
}

