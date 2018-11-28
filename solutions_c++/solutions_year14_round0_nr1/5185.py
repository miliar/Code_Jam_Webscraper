#include<cstdio>
#include <iostream>
#include <cstring>
#include <sstream>
#include <string>
#include <cmath>
using namespace std;
int main(){
int t,r1,r2,b[4][4],a[4][4];
int c1[4],c2[4],eli,i,j,k,count,var;
scanf("%d",&t);
for(k=1;k<=t;k++){
scanf("%d",&r1);
{for(i=1;i<=4;i++)
for(j=1;j<=4;j++)
scanf("%d",&a[i][j]);
for(i=1;i<=4;i++)
    c1[i]=a[r1][i];
}scanf("%d",&r2);
{for(i=1;i<=4;i++)
for(j=1;j<=4;j++)
scanf("%d",&b[i][j]);
for(i=1;i<=4;i++)
    c2[i]=b[r2][i];
}count=0;
for(i=1;i<=4;i++)
{var=c1[i];
 for(j=1;j<=4;j++)
 if(var==c2[j]){
    count++;eli=var;
     }
}if(count==1)
 printf("Case #%d: %d\n",k,eli);
 else if(count>1)
 printf("Case #%d: Bad magician!\n",k);
 else if(count==0)
printf("Case #%d: Volunteer cheated!\n",k);
}return 0;
}
