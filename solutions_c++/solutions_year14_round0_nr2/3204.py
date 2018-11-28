#include<stdio.h>
#include<math.h>
#include<iostream>
#include<stdlib.h>
#include<vector>
#include<map>
#include<set>
#include<cstring>
#include<algorithm>
#define LL long long
#define N 11
#define M 121
#define println() printf("\n")
#define scani(t) scanf("%d",&t)
#define scanl(t) scanf("%lld",&t)
#define printi(t) printf("%d",t)
#define printl(t) printf("%lld",t)
using namespace std;
int main()
{   
/*#ifndef ONLINE_JUDGE
freopen("input.txt","r",stdin);
freopen("re.txt","w",stdout);
#endif*/
LL i=1,t;double C,F,X,f,ttime,time1,time2;
scanl(t);
while(i<=t)
{f=2;ttime=0;
scanf("%lf%lf%lf",&C,&F,&X);
if(X<=C)
{
printf("Case #%lld: %0.6lf\n",i,X/f);
i++;
continue;        
}        
while(1)
{
ttime+=C/f;
time1=(X-C)/f;//don't buy
time2=(X)/(f+F);//buy
if(time1>time2)
f+=F;
else
{
 ttime+=(X-C)/f;
 printf("Case #%lld: %0.6lf\n",i,ttime);

 break;   
}        
        
        
        
        
        
}
   
           
i++;           
           
           
}//t

   
    
    
return 0;    
}
