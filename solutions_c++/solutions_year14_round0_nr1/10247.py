#include <cstdio>
#include <algorithm>
using namespace std;
void increase(int cnt[], int mat[4][4], int x){
	for(int i=0;i<4;i++)
		cnt[mat[x-1][i]]++;
}
int main(){
	int r;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&r);
	for(int rr=1;rr<=r;rr++){
		int cnt[20] = {0,};
		int mat[4][4] = {0,};
		for(int t=0;t<2;t++){
			int a;
			scanf("%d",&a);
			for(int i=0;i<4;i++){
				for(int j=0;j<4;j++){
					scanf("%d",&mat[i][j]);
				}
			}
			increase(cnt, mat, a);
		}
		int res = 0, res_inx = -1;
		for(int i=1;i<=16;i++){
			if(cnt[i] == 2){
				res++;
				res_inx = i;
			}
		}
		printf("Case #%d: ",rr);
		if(res == 1) printf("%d\n",res_inx);
		else if(res >= 2) printf("Bad magician!\n");
		else printf("Volunteer cheated!\n");
	}
	return 0;
}
