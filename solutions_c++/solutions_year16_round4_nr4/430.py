#include <bits/stdc++.h>
using namespace std;

#define mp(x, y) make_pair((x), (y))

typedef long long ll;

int q;
int n;
int g[42][42];
int gg[42][42];

int main()
{
	scanf("%d\n", &q);

	for(int x=1; x<=q; x++) {
		scanf("%d\n", &n);
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				char c;
				scanf("%c", &c);
				g[i][j]=c-'0';
			}
			scanf("\n");
		}
		int ans=n*n;
		for(int m1=0; m1<(1<<(n*n)); m1++) {
			int diff=0;
			for(int i=m1, j=0; j<n*n; i>>=1, j++) {
				gg[j/n][j%n]=g[j/n][j%n]|(i&1);
				diff+=(gg[j/n][j%n]^g[j/n][j%n]);
			}
			if(diff>=ans) continue;
			int ok1=0, ok2=1;
			for(int m2=0; ok2 && m2<(1<<(n*n)); m2++) {
				int ok=1;
				int mat1[4]={-1, -1, -1, -1}, mat2[4]={-1, -1, -1, -1};
				int cnt=0;
				for(int i=m2, j=0; ok && i>0; i>>=1, j++) {
					if(i&1) {
						int w=j/n, m=j%n;
						if(gg[w][m]==0 || mat1[w]!=-1 || mat2[m]!=-1) {
							ok=0;
						} else {
							mat1[w]=m;
							mat2[m]=w;
							cnt++;
						}
					}
				}
				if(!ok) continue;
				if(cnt==n) ok1=1;
				else {
					int ok=1;
					for(int w=0; ok && w<n; w++) {
						for(int m=0; ok && m<n; m++) {
							if(gg[w][m]==1 && mat1[w]==-1 && mat2[m]==-1) {
								ok=0;
							}
						}
					}
					if(ok) ok2=0;
				}
			}
			if(ok1 && ok2) ans=min(ans, diff);
		}
		printf("Case #%d: %d\n", x, ans);
	}

	return 0;
}
