#include<stdio.h>

int v[1010];

int is_palindrome(int x)
{
    int aux=x;
    int rev=0;
    while(aux)
    {
        rev=rev*10 + aux%10;
        aux=aux/10;
    }
    return rev==x;
}
int N,x,y;
int main()
{
freopen("c.in","r",stdin);
freopen("c.out","w",stdout);
    for(int i=1;i*i<=1000;++i)
    {
        if(is_palindrome(i) && is_palindrome(i*i))
       {
        v[i*i]=1;
       //printf("%d %d\n",i,i*i);
        }
    }
    for(int i=1;i<=1000;++i)
        v[i]+=v[i-1];
    scanf("%d",&N);
        for(int i=1;i<=N;++i)
        {
            scanf("%d%d",&x,&y);
            printf("Case #%d: %d\n",i,v[y]-v[x-1]);
        }
}
