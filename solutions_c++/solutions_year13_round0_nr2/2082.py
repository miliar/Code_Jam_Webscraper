
//Author :krishna Kumar Tiwari


#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <complex>

#include<stdio.h>

int strt=1;
int main() {

int tc ;
  scanf("%d",&tc);
if(tc>=1&&tc<=100){
while(tc--){

int row,col,i,j,w;
scanf("%d%d",&row,&col);
int TN =(row*col);

int array[row][col] ,r[row][col],c[row][col];
for(i=0;i<row;i++){
 for(j=0;j<col;j++){
  scanf("%d",&array[i][j]);
 }
}
   int b[row],mx,cnt=0,b1[col],mx2;
    for (i = 0; i< row;i++)
    {    mx=array[i][0];
        for ( j = 1;j< col;j++)
        {     if(mx<array[i][j])
               {
                  mx=array[i][j];
               }
              
        }
        b[i]=mx;
        
    }

for(i=0;i<row;i++){
   for(j=0;j<col;j++){
     if(b[i]==array[i][j]){
        r[i][j]=1;
     }
     else r[i][j]=0;
    }
  }
 for ( j = 0;j< col;j++)
    {    mx2=array[0][j];
       for (i = 1; i< row;i++)
        {     if(mx2<array[i][j])
               {
                  mx2=array[i][j];
               }
              
        }
        b1[j]=mx2;
   }
   
  for(j=0;j<col;j++){
    for(i=0;i<row;i++)
   {
     if(b1[j]==array[i][j]){
        c[i][j]=1;
     }
     else c[i][j]=0;
    }
  }
 
for(j=0;j<col;j++){
    for(i=0;i<row;i++)
     {
        if((c[i][j]==1) || (r[i][j]==1))
         cnt++;
         
     }
}
if(cnt==TN)
 printf("Case #%d: YES\n",strt);
else
 printf("Case #%d: NO\n",strt);
strt++;}
}
return 0;


}
