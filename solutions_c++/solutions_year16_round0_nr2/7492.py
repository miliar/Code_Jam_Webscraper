#include<cstdio>
#include<cstring>

char a[105];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("eq.out","w",stdout);
    int n,t;
    scanf("%d",&t);
    for(int round=1;round<=t;round++)
    {
        scanf("%s",a);
        n = strlen(a);
        int c = 1;
        for(int i=1;i<n;i++)
        {
            if(a[i] != a[i-1])
                c++;
        }
        if(a[n-1] == '+')
            c--;
        printf("Case #%d: %d\n",round,c);
    }
}
