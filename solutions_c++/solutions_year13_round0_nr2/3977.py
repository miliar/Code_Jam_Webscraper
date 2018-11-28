#include<stdio.h>

int start=1;
int main() {

int test ;
  scanf("%d",&test);
if(test>=1&&test<=100){
while(test--){

int numRows,numCols,i,j,w;
scanf("%d%d",&numRows,&numCols);
int TotalNum =(numRows*numCols);

int arr[numRows][numCols] ,r[numRows][numCols],c[numRows][numCols];
for(i=0;i<numRows;i++){
 for(j=0;j<numCols;j++){
  scanf("%d",&arr[i][j]);
 }
}
 


/*int test,w;
  scanf("%d",&test);
for(w=0;w<test;w++){*/

   int b[numRows],max,count=0,b1[numCols],max1;
    for (i = 0; i< numRows;i++)
    {    max=arr[i][0];
        for ( j = 1;j< numCols;j++)
        {     if(max<arr[i][j])
               {
                  max=arr[i][j];
               }
              
        }
        b[i]=max;
        
    }

// for (i = 0; i< numRows;i++) 
 // printf("%d\n",b[i]);
 
 
for(i=0;i<numRows;i++){
   for(j=0;j<numCols;j++){
     if(b[i]==arr[i][j]){
        r[i][j]=1;
     }
     else r[i][j]=0;
    }
  }

 /*for(i=0;i<numRows;i++){
   printf("\n");
   for(j=0;j<numCols;j++){
     printf("%d",r[i][j]);
   }
 }*/

 /*for(i=0;i<numRows;i++){
   for(j=0;j<numCols;j++){
     if(r[i][j]==1)
        count++;
    }
    }
  if(count==TotalNum)
  printf("yes");*/
//printf("\n");
  


 for ( j = 0;j< numCols;j++)
    {    max1=arr[0][j];
       for (i = 1; i< numRows;i++)
        {     if(max1<arr[i][j])
               {
                  max1=arr[i][j];
               }
              
        }
        b1[j]=max1;
   }
   
 
 /*  for (j=0; j< numCols;j++) 
 printf("%d\n",b1[j]); */
   

  for(j=0;j<numCols;j++){
    for(i=0;i<numRows;i++)
   {
     if(b1[j]==arr[i][j]){
        c[i][j]=1;
     }
     else c[i][j]=0;
    }
  }
 /*for(i=0;i<numRows;i++){
   printf("\n");
   for(j=0;j<numCols;j++){
  printf("%d",c[i][j]);
  }
 }*/
for(j=0;j<numCols;j++){
    for(i=0;i<numRows;i++)
     {
        if((c[i][j]==1) || (r[i][j]==1))
         count++;
         
     }
}
if(count==TotalNum)
 printf("Case #%d: YES\n",start);
else
 printf("Case #%d: NO\n",start);
start++;}
}
return 0;


}
