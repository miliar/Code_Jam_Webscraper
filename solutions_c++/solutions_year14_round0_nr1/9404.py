#include <stdio.h>

int a[4][4];
int b[4][4];
int k,l,i;
int main(void) {
	int T;
	scanf("%d",&T);
	for(int z=1;z<=T;z++){
	scanf("%d",&k);
	for(i=0;i<4;i++)
	{
		
			scanf("%d %d %d %d\n",&a[i][0],&a[i][1],&a[i][2],&a[i][3]);
	}
	scanf("%d",&l);
	for(i=0;i<4;i++)
	{
		
			scanf("%d %d %d %d\n",&b[i][0],&b[i][1],&b[i][2],&b[i][3]);
	}
int x,y;
	int p=0;
	int j=0;
	for(j=0;j<4;j++){
	for(i=0;i<4;i++){
		if(b[l-1][i]==a[k-1][j]){
			x=k-1;
			y=j;
			p++;
		}
	}
	}
	if(p==1){
printf("Case #%d: %d\n",z,a[x][y]);
continue;
	}
	else if(p>1)
	{

printf("Case #%d: Bad Magician!\n",z);
continue;
	}else
	{

printf("Case #%d: Volunteer Cheated!\n",z);
continue;
	}
	}
return 0;
}