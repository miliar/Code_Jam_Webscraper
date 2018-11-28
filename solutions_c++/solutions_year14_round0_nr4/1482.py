#include <bits/stdc++.h>
using namespace std;
int T,y,z,N,cmin,cmax;
double a[1010],b[1010],c[1010];
int main(){
	freopen("input.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc){
		memset(a,0,sizeof a);
		memset(b,0,sizeof b);
		memset(c,0,sizeof c);
		scanf("%d", &N);
		for (int i = 0; i < N; ++i){
			scanf("%lf", &a[i]);
		}
		for (int i = 0; i < N; ++i){
			scanf("%lf", &b[i]);
			c[i]=b[i];
		}
		sort(a,a+N);
		sort(b,b+N);
		// for (int j = 0; j < N; ++j){
		// 		printf("%lf ", a[j]);
		// 	}
		// 	printf("\n");
		// for (int j = 0; j < N; ++j){
		// 		printf("%lf ", b[j]);
		// 	}
		// 	printf("\n");
		bool kw=0;
		y=z=0;
		for (int i = 0; i < N; ++i){
			kw=0;
			for (int j = 0; j < N; ++j){
				if (b[j]>a[i]){
					b[j]=0;
					kw=1;
					break;
				}
			}
			// for (int j = 0; j < N; ++j){
			// 	printf("%lf ", b[j]);
			// }
			// printf("\n");
			if (kw==0) {
				z++;
				for (int j = 0; j < N; ++j){
					if (b[j]!=0){
						b[j]=0;
						break;
					}
				}
			}
		}

		sort(c,c+N);
		cmin=0; cmax=N-1;
		for (int i = 0; i < N; ++i){
			if (a[i]<c[cmin]){
				c[cmax]=0;
				cmax--;
			}
			else{
				c[cmin]=0;
				cmin++;
				y++;
			}
		}
		printf("Case #%d: %d %d\n",tc, y,z);
	}
}