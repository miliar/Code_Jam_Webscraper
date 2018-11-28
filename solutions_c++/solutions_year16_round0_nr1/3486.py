#include<stdio.h>
int dight(int s)
{
    if(s == 0) return 1;
    int re =0;
    while(s>0)
    {
        re=re|(1<<(s%10));
        s/=10;
    }
    return re;
}
void doit()
{
    int n;
    scanf("%d",&n);
    int s =0;
    int mark = 0;
    for(int i=0;i<=100;i++)
    {
        s+=n;
        mark = mark | dight(s);
        if(mark == 1023) break;
    }
    if(mark == 1023)printf("%d\n",s);
    else printf("INSOMNIA\n");
}
int main()
{
    int t;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
      printf("Case #%d: ",i);
      doit();
    }
}
