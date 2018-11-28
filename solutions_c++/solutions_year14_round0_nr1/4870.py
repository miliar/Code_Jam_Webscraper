#include <iostream>
#include<stdio.h>
using namespace std;

int main() {
    freopen("A-small.in","r",stdin);
    freopen("output.txt","w",stdout);

int T,r1,r2,x,i,j,t,count;
scanf("%d",&T);
t=1;
while(t<=T){
	int a[4][4],b[17]={0};
	scanf("%d",&r1);
for(i=1;i<=(r1-1)*4;i++)
	scanf("%d",&x);
	for(i=1;i<=4;i++){
			scanf("%d",&x);
			b[x]=1;
	}
	for(i=1;i<=(4-r1)*4;i++)
	scanf("%d",&x);

		scanf("%d",&r2);
for(i=1;i<=(r2-1)*4;i++)
	scanf("%d",&x);
	for(i=1;i<=4;i++){

			scanf("%d",&x);
			b[x]+=1;
	}
		for(i=1;i<=(4-r2)*4;i++)
	scanf("%d",&x);
	count=0;
	j=0;
	for(i=1;i<=16;i++){
		if(b[i]==2){
		j=i;
		count+=1;
		}
	}
	if(count>=2)
	printf("Case #%d: Bad magician!\n",t);
    else if(j==0)
        printf("Case #%d: Volunteer cheated!\n",t);

		else
			printf("Case #%d: %d\n",t,j);

	t++;

}
return 0;
}
