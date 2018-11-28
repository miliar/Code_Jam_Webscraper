#include <cstdio>
#include <cstring>
int T, k1, k2, x, ans;
int w[22];

int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	scanf("%d",&T);
	for ( int I(1); I <= T; I++){
		memset(w,0,sizeof(w));
		scanf("%d",&k1);
		for ( int i(1); i<=4; i++){
			for ( int j(1);j<=4;j++){
				scanf("%d",&x);
				w[x] = i;
			}
		}
		ans = 0;
		scanf("%d",&k2);
		for ( int i(1);i<=4;i++){
			for ( int j(1);j<=4;j++){
				scanf("%d",&x);
				if (i==k2){
					if (w[x]==k1){
						if (ans==0) ans = x;	// answer
						else ans = -1;			// bad ...
					}
				}
			}
		}
		printf("Case #%d: ",I);
		if ( ans == -1 ) printf("Bad magician!\n");
		else if (ans) printf("%d\n",ans);
		else printf("Volunteer cheated!\n");
	}
	return 0;
}
