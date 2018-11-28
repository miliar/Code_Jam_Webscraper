#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

int tc;
int n,par[55],ppl[55];
char c[55][55];
int ret;

void doit2(int k,int at) {
	if (at == n) {
		int v[55],w[55];
		memset(v,0,sizeof(v));
		memset(w,0,sizeof(w));
		for (int i=0; i<n; i++) {
			v[ppl[i]]++;
			w[par[i]]++;
		}
		for (int i=0; i<k; i++)
			if (v[i] != w[i]) return;

		int cnt = 0;
		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) {
				if (par[j] == ppl[i] && c[i][j] == '0') cnt++;
				if (par[j] != ppl[i] && c[i][j] == '1') return;
			}
		}
		/*
		for (int i=0; i<n; i++) {
			printf("%d %d\n",par[i],ppl[i]);
		}
		printf("%d\n",cnt);
		*/
		ret = min(ret,cnt);
		return;
	}
	for (int i=0; i<k; i++) {
		ppl[at] = i;
		doit2(k,at+1);
	}
}

void doit(int k,int at) {
	if (at == n) {
		doit2(k,0);
		return;
	}
	for (int i=0; i<k; i++) {
		par[at] = i;
		doit(k,at+1);
	}
	par[at] = k;
	doit(k+1,at+1);
}

int main() {
	scanf("%d",&tc);
	for (int t=1; t<=tc; t++) {
		scanf("%d",&n);
		for (int i=0; i<n; i++)
			scanf("%s",c[i]);

		ret = 100000;
		doit(0,0);
		printf("Case #%d: %d\n",t,ret);
	}
    return 0;
}
