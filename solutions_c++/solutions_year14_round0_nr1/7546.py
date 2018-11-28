#include<cstdio>
#include<cstring>
int i,j,k,s,p,t,T;
bool v[20];
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    for (t=1;t<=T;t++)
    {
        memset(v,0,sizeof(v));
        scanf("%d",&s);
        for (i=1;i<=4;i++)
          if (i==s)
            for (j=1;j<=4;j++)
              scanf("%d",&k),v[k]=1;
          else for (j=1;j<=4;j++)scanf("%d",&k);
        scanf("%d",&s);
        p=0;
        for (i=1;i<=4;i++)
          if (i==s)
            for (j=1;j<=4;j++)
              scanf("%d",&k),v[k]?(p=p?-1:k):0;
          else for (j=1;j<=4;j++)scanf("%d",&k);
        printf("Case #%d: ",t);
        if (p==-1)puts("Bad magician!");
        else if (p==0)puts("Volunteer cheated!");
        else printf("%d\n",p);
    }
    return 0;
}
