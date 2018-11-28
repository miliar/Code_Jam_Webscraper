#include <stdio.h>
int a[4][4],a1[4][4];


int compare(int x, int y){
		
		int i,j,num,count=0;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++){
				if(a[x-1][i]==a1[y-1][j]){
					count++;num=a1[y-1][j];}}
		}

		if(count==1){
			return(num);
		}
		else if(count==0)
			return(-1);
		else
			return(999);


	}
int main(){


	
	int x,i,j,res,q,q1;
	scanf("%d",&x);
	for (i=0;i<x;i++){

		scanf("%d",&q);
		for(j=0;j<4;j++)
			scanf("%d %d %d %d\n",&a[j][0],&a[j][1],&a[j][2],&a[j][3]);
		scanf("%d",&q1);
		for(j=0;j<4;j++)
			scanf("%d %d %d %d\n",&a1[j][0],&a1[j][1],&a1[j][2],&a1[j][3]);





		res=compare(q,q1);
		if(res==-1)
			printf("Case #%d: Volunteer cheated!\n",i+1);
		else if(res==999)
			printf("Case #%d: Bad magician!\n",i+1);
		else
			printf("Case #%d: %d\n",i+1,res);

	}



return 0;

}