#include<stdio.h>
int main()
{
   int t,a[4][4],b[4][4];
   scanf("%d",&t);
   for(int i=0;i<t;i++){
	   int r1,r2;
	   scanf("%d",&r1);
	   for(int j=0;j<4;j++){
		   for(int k=0;k<4;k++){
			   scanf("%d",&a[j][k]);
		   }
	   }
	   scanf("%d",&r2);
	   	   for(int j=0;j<4;j++){
	   		   for(int k=0;k<4;k++){
	   			   scanf("%d",&b[j][k]);
	   		   }
	   	   }
	   	   int count=0;
	   	   int num=0;
	   	  for(int j=0;j<4;j++){
	   		  for(int k=0;k<4;k++){
	   			 // printf("Comapring %d %d\n",a[r1-1][j],b[r2-1][k]);
	   			  if(a[r1-1][j] == b[r2-1][k]){
	   				  count++;
	   				  num=a[r1-1][j];
	   			  }
	   		  }
	   	  }
	   	  if(count==1){
	   		  printf("Case #%d: %d\n",i+1,num);
	   	  }
	   	  else if(count==0){
	   		  printf("Case #%d: Volunteer cheated!\n",i+1);

	   	  }
	   	  else{
	   		  printf("Case #%d: Bad magician!\n",i+1);
	   	  }
   }

  return 0;
}
