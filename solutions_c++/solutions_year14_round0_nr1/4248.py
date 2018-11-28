#include<cstdio>
int T, a, ck[16], tmp, res, ans;
int main(){
	freopen("GCJ14_QR_A.in","r",stdin);
	freopen("GCJ14_QR_A.out","w", stdout);
	
	scanf("%d",&T);
	for (int t = 0; t < T; t++){
		for (int i = 0; i < 16; i++)ck[i] = 0;
		scanf("%d",&a);
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++){
				scanf("%d",&tmp);
				if (i == a-1)ck[tmp-1]++;
			}
		scanf("%d",&a); ans = -1; res = 3;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++){
				scanf("%d",&tmp);
				if (i == a-1)
					if (ck[tmp-1] == 1){
						if (ans == -1){
							ans = tmp; res = 1;
						}
						else res = 2;
					}
			}
		printf("Case #%d: ", t+1);
		if (res == 1)printf("%d\n", ans);
		if (res == 2)printf("Bad magician!\n");
		if (res == 3)printf("Volunteer cheated!\n");
	}
	return 0;
}
