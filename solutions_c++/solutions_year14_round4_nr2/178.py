#include <bits/stdc++.h>

#define FWD(a,b,c) for(int a=(b); a<(c); ++a)
#define SIZE(a) ((int)a.size())
#define pb push_back
#define PII pair<int, int>
#define x first
#define y second

using namespace std;

typedef long long LL;

int n, c;
int T[1010];

int main(){
	int Z; scanf("%d", &Z); FWD(z,1,Z+1){
		c = 0;
		scanf("%d", &n);
		FWD(i,0,n) scanf("%d", &T[i]);
		int p = 0;
		int k = n-1;
		while(p <= k){
			int m = p;
			FWD(i,p+1,k+1) if(T[i] < T[m]) m = i;
			c += min(m-p, k-m);
			if(m-p < k-m){
				while(m > p){
					swap(T[m], T[m-1]);
					--m;
				}
				++p;
			}else{
				while(m < k){
					swap(T[m], T[m+1]);
					++m;
				}
				--k;
			}
		}
		printf("Case #%d: %d\n", z, c);
	}
	return 0;
}
