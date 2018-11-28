#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;
int n,t,a[10],qq;
int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
scanf("%d",&t);
for(int tt=1;tt<=t;tt++){
    scanf("%d",&n);
    for(int i=0;i<10;i++){a[i]=0;}
   qq=10;
   printf("Case #%d: ",tt);
   for(int i=1;i<1000001;i++){
    long long p=(long long) i*n;
long long ans=p;
    while(p){
       int aa=p%10;
        p/=10;
        if(!a[aa]){qq--;}
        a[aa]=1;
    }
if(!qq){printf("%lld\n",ans);break;}
   }
if(qq){printf("INSOMNIA\n");}
}



    return 0;
}
