#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
long long int largeno(long long int n)
{
if(n==0)return -1;
int d,visited[10],check=0;
memset(visited,-1,sizeof(visited));
long long int x=0,y=0;
while(check<10)
    {
    y+=n;
    x=y;
    while(x!=0)
    {
     d=x%10;
     if(visited[d]==-1){visited[d]=1; check++;}
     if(check==10)break;
     x/=10;
    }
    }
return y;
}

int main()
{
int t;
long long int n,res;
scanf("%d",&t);
for(int i=0;i<t;i++){
scanf("%lld",&n);
res=largeno(n);
if(res==-1)printf("Case #%d: INSOMNIA\n",i+1);
else printf("Case #%d: %lld\n",i+1,res);
}

return 0;
}
