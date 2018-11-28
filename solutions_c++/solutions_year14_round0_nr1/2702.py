#include<stdio.h>
int main(){
	FILE *f;
	f=fopen("out.txt","w");
	int t,l=1;
	scanf("%d",&t);
	while(t--){
		int k,p,i,j;
		scanf("%d",&k);
		int a[4][4],b[4][4];
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				scanf("%d",&a[i][j]);
			}
		}
		scanf("%d",&p);
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				scanf("%d",&b[i][j]);
			}
		}
		int flag=0,m;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				if(a[k-1][i]==b[p-1][j]){
					flag++;
					m=a[k-1][i];
				}
			}
		}
		if(flag==0){
			fprintf(f,"Case #%d: Volunteer cheated!\n",l);
		}
		else if(flag==1){
			fprintf(f,"Case #%d: %d\n",l,m);
		}
		else{
			fprintf(f,"Case #%d: Bad magician!\n",l);
		}
		l++;
	}
}
