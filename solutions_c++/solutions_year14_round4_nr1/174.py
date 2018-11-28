#include <bits/stdc++.h>

#define FWD(a,b,c) for(int a=(b); a<(c); ++a)
#define SIZE(a) ((int)a.size())
#define pb push_back
#define PII pair<int, int>
#define x first
#define y second

using namespace std;

typedef long long LL;

int n, x;
int S[10010];

int main(){
	int Z; scanf("%d", &Z); FWD(z,1,Z+1){
		int c = 0;
		scanf("%d %d", &n, &x);
		FWD(i,0,n) scanf("%d", &S[i]);
		sort(S, S+n);
		int j = n-1;
		FWD(i,0,n){
			if(S[i] == -1) continue;
			++c;
			while(i < j && S[i] + S[j] > x) --j;
			S[j] = -1;
			j = max(0, j-1);
		}
		printf("Case #%d: %d\n", z, c);
	}
	return 0;
}
