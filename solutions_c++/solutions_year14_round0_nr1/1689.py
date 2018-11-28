#include <bits/stdc++.h>
using namespace std;
int T,a,b,ar[5],nr[5],tt,ct,ans;
int main(){
	freopen("input.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d", &T);
	for (int tc=1; tc<=T; tc++){
		scanf("%d", &a);
		memset(ar,0,sizeof ar);
		memset(nr,0,sizeof nr);
		ct=0;ans=0;
		for (int i = 1; i < 5; ++i){
			for (int j = 1; j < 5; ++j){
				scanf("%d", &tt);
				if (i==a)
					ar[j]=tt;
			}
		}
		scanf("%d", &b);
		for (int i = 1; i < 5; ++i){
			for (int j = 1; j < 5; ++j){
				scanf("%d", &tt);
				if (i==b)
					nr[j]=tt;
			}
		}
		// for (int i = 0; i < 5; ++i){
		// 	printf("%d ", ar[i]);
		// }
		// printf("\n");
		// for (int i = 0; i < 5; ++i){
		// 	printf("%d ", nr[i]);
		// }
		for (int i = 1; i < 5; ++i){
			for (int j = 1; j < 5; ++j){
				if (ar[i]==nr[j]) {
					ct++;
					ans=ar[i];
				}
			}
		}
		//printf("%d\n", ct);
		printf("Case #%d: ", tc);
		if (ct>1)
			printf("Bad magician!\n");
		else if (ct==1)
			printf("%d\n", ans);
		else
			printf("Volunteer cheated!\n");
	}
}