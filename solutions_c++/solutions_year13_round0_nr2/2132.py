#include<stdio.h>
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstdlib>
#include<climits>

int main() {

int test,s=1;
  scanf("%d",&test);

while(test--){

int nr,nc,i,j,w;
scanf("%d%d",&nr,&nc);
int tn =(nr*nc);

int a[nr][nc] ,r[nr][nc],c[nr][nc];
for(i=0;i<nr;i++){
 for(j=0;j<nc;j++){
  scanf("%d",&a[i][j]);
 }
}
 





   int b[nr],maxrow,count=0,b1[nc],maxcol;
    for (i = 0; i< nr;i++)
    {    maxrow=a[i][0];
        for ( j = 1;j< nc;j++)
        {     if(maxrow<a[i][j])
               {
                  maxrow=a[i][j];
               }
              
        }
        b[i]=maxrow;
        
    }




 
for(i=0;i<nr;i++){
   for(j=0;j<nc;j++){
     if(b[i]==a[i][j]){
        r[i][j]=1;
     }
     else r[i][j]=0;
    }
  }



  


 for ( j = 0;j< nc;j++)
    {    maxcol=a[0][j];
       for (i = 1; i< nr;i++)
        {     if(maxcol<a[i][j])
               {
                  maxcol=a[i][j];
               }
              
        }
        b1[j]=maxcol;
   }
   
 
 



  for(j=0;j<nc;j++){
    for(i=0;i<nr;i++)
   {
     if(b1[j]==a[i][j]){
        c[i][j]=1;
     }
     else c[i][j]=0;
    }
  }
 


for(j=0;j<nc;j++){
    for(i=0;i<nr;i++)
     {
        if((c[i][j]==1) || (r[i][j]==1))
         count++;
         
     }
}
if(count==tn)
 printf("Case #%d: YES\n",s);
else
 printf("Case #%d: NO\n",s);
s++;
}

return 0;


}
