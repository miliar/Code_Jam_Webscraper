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

const int N = (1<<20) + 100;
int a[N];
int in[N];
int tt[N];
int out[30];
int main() {
	int TT;
	scanf("%d", &TT);
	for(int cc = 1; cc <= TT; ++cc){
		int p;
		scanf("%d", &p);
		int now = 0;
		for(int i=0; i<p; ++i){
			scanf("%d", a + i);
		}
		for(int i=0; i<p; ++i){
			int x;
			scanf("%d", &x);
			while(x--){
				in[now++] = a[i];
			}
		}
		int n = 1;
		while((1<<n) < now) ++n;
		out[0] = in[1];
		for(int i = 1; i < n; ++i){
			for(int j=0; j<(1<<i); ++j){
				int now = 0;
				for(int k = 0; k < i; ++k){
					if((1<<k) & j) now += out[k];
				}
				tt[j] = now;
			}
			sort(tt, tt + (1<<i));
			int pos = 0;
			for(; pos < (1<<i); ++pos){
				if(tt[pos]!=in[pos])break;
			}
			out[i] = in[pos];
		}
		printf("Case #%d:", cc);
		for(int i=0; i<n; ++i)printf(" %d", out[i]);
		printf("\n");
	}
	return 0;
}

