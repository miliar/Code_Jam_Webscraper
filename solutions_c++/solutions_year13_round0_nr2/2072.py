#include<stdio.h>

int start=1;

int main() {

int T ;
  scanf("%d",&T);


if(T>=1&&T<=100){
while(T--){

int R,C,i,j,w;

scanf("%d%d",&R,&C);

int tot =(R*C);


//////// scan
int arr[R][C] ,r[R][C],c[R][C];
for(i=0;i<R;i++){
 for(j=0;j<C;j++){
  scanf("%d",&arr[i][j]);
 }
}
 


   int b[R],max,count=0,b1[C],max1;
    for (i = 0; i< R;i++)
    {    max=arr[i][0];
        for ( j = 1;j< C;j++)
        {     if(max<arr[i][j])
               {
                  max=arr[i][j];
               }
              
        }
        b[i]=max;
        
    }
 
for(i=0;i<R;i++){
   for(j=0;j<C;j++){
     if(b[i]==arr[i][j]){
        r[i][j]=1;
     }
     else r[i][j]=0;
    }
  }


 for ( j = 0;j< C;j++)
    {    max1=arr[0][j];
       for (i = 1; i< R;i++)
        {     if(max1<arr[i][j])
               {
                  max1=arr[i][j];
               }
              
        }
        b1[j]=max1;
   }
   
   

  for(j=0;j<C;j++){
    for(i=0;i<R;i++)
   {
     if(b1[j]==arr[i][j]){
        c[i][j]=1;
     }
     else c[i][j]=0;
    }
  }




for(j=0;j<C;j++){
    for(i=0;i<R;i++)
     {
        if((c[i][j]==1) || (r[i][j]==1))
         count++;
         
     }
}
////////////////// print output
if(count==tot)
 printf("Case #%d: YES\n",start);
else
 printf("Case #%d: NO\n",start);
start++;}
}
return 0;
}
