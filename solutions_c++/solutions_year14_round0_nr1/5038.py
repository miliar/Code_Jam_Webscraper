#include <stdio.h>

int main (){
freopen("a1.txt","w",stdout);
int a[4][4],x[4],y[4],b,t,ans,k=1,i,j;
scanf("%d",&t);
while(t--){
	
	scanf("%d",&b);
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			scanf("%d",&a[i][j]);
			if(b-1==i)
			x[j]=a[i][j];
		}
	}
	scanf("%d",&b);
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			scanf("%d",&a[i][j]);
			if(b-1==i)
			y[j]=a[i][j];
		}
	}
	b=0;
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			if(x[i]==y[j]){
				b++;
				ans=x[i];
				break;
			}
		}
	}
	if(b==0){
		printf("Case #%d: Volunteer cheated!\n",k);
	}
	else if(b==1){
		printf("Case #%d: %d\n",k,ans);
	}
	else
	{
		printf("Case #%d: Bad magician!\n",k);
	}
	k++;
}


return 0;
}

