#include <stdio.h>
int T;
	int ra,rb;
	int a[10][10];
	int b[10][10];
	int cnt[50];
	int aa;
int main(){
	freopen("A-small-attempt1.in","r",stdin);
	freopen("out.txt","w",stdout);
	//puts("1");
	//puts("1");
	scanf("%d",&T);
	//printf("%d\n",T);
	aa=0;
	//puts("1");
	while(T--){
		//printf("1");
	    for(int i=0;i<50;++i) cnt[i]=0;
	    //printf("1");
		scanf("%d",&ra);
		//printf("~%d~\n",ra);
		for(int i=1;i<=4;++i){
			for(int j=1;j<=4;++j){
			   scanf("%d",&a[i][j]);
			}
		}
		//printf("1");
		for(int i=1;i<=4;++i){
			int kk=a[ra][i];
			cnt[kk]++;
			//printf("===========%d ",kk);
		}
		//puts("");
		//printf("1");
		scanf("%d",&rb);
		//printf("~%d~\n",rb);
		for(int i=1;i<=4;++i){
			for(int j=1;j<=4;++j){
			   scanf("%d",&b[i][j]);
			}
		}
		for(int i=1;i<=4;++i){
			cnt[b[rb][i]]++;
		}
		
		int same=0;
		int tt=-1;
		for(int i=0;i<50;++i){
		   if(cnt[i]>1) same++,tt=i;
	    }
	    //printf("%d\n",same);
		printf("Case #%d: ",++aa);
		if(same<=0) puts("Volunteer cheated!");
		if(same==1) printf("%d\n",tt);
		if(same>1) puts("Bad magician!");
		//puts("1");
	}
	return 0;
}
