#include<stdio.h>

//FILE *input=freopen("A-small-attempt0 (1).in","r",stdin);
//FILE *output=freopen("aa.out","w",stdout);
int a[4][4];
int is_use[17];

int main(){
	int t,tc=1;
	int r;
	int i,j;
	int cnt=0;
	int out;
	scanf("%d",&t);
	for(;t>0;t--){
		cnt=0;
		for(i=1;i<=16;i++){
			is_use[i]=0;			
		}
		scanf("%d",&r);
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				scanf("%d",&a[i][j]);
				if(i+1==r)
					is_use[a[i][j]]++;
			}
		}
		scanf("%d",&r);
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				scanf("%d",&a[i][j]);
				if(i+1==r)
					is_use[a[i][j]]++;
			}
		}
		for(i=1;i<=16;i++){
			if(is_use[i]==2){
				cnt++;
				out=i;
			}
		}
		printf("Case #%d: ",tc++);
		if(cnt>=2){
			printf("Bad magician!\n");
		}
		else if(cnt==1){
			printf("%d\n",out);
		}
		else
			printf("Volunteer cheated!\n");
	}
	return 0;
}