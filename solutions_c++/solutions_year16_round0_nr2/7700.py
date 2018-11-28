#include<cstdio>
#include<cstring>

void revCh(char &c)
{
    if (c=='+')
        c='-';
    else c='+';
}

void flipcake (char* &s,int n)
{
    for (int i=0;i<=n;i++)
    {
        revCh(s[i]);
    }
}

int countFlip(char* s)
{
    int flip=0;
    int len=strlen(s);
    for (int i=(len-1);i>=0;i--)
    {
        if (s[i]=='-')
        {
            flip++;
            flipcake(s,i);
        }
    }
    return(flip);
}



main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);

    int t;
    char s[101];
    scanf("%d",&t);
    for (int i=1;i<=t;i++)
    {
        scanf("%100s",&s);
        printf("Case #%d: %d\n",i,countFlip(s));

    }
}
