#include<stdio.h>
#include<iostream>
using namespace std;
 
int chk_pal(int n)
{
char a[5];
int i=0,j;
while(n>0)
{
    a[i++]=n%10;
    n/=10;
}
for(j=0;j<i/2;j++)
{
    if(a[j]!=a[i-j-1])
    return 0;
}
return 1;
}
int a[1002];
int main()
 {
        int t,i,j,n,k=1;
     for(i=1;i<=31;i++)
     {
        if(chk_pal(i))
        {
        if(chk_pal(i*i))
        a[i*i]=1;
        }
    }
    scanf("%d",&t);
    while(t--){
            int ans=0;
            scanf("%d%d",&i,&j);
            for(n=i;n<=j;n++)
            if(a[n]==1)
            ans++;
            printf("Case #%d: %d\n",k++,ans);
        }
            return 0;
}