#include<stdio.h>
#include<string.h>

#define NMAX 5

int v[NMAX][NMAX],f[NMAX*NMAX];

void citeste()
{
    int c,i,j;
    scanf("%d",&c);
    for(i=1;i<=4;++i)
        for(j=1;j<=4;++j)
            scanf("%d",&v[i][j]);
    for(j=1;j<=4;++j)
        ++f[v[c][j]];
}

int main()
{
    //freopen("date.in","r",stdin);
    //freopen("date.out","w",stdout);
    int t,nr=0,i,ok,sol;

    scanf("%d",&t);
    while(t-- && ++nr)
    {
        memset(f,0,sizeof(f));
        ok=3;sol=0;

        citeste();
        citeste();

        for(i=1;i<=16;++i)
            if(f[i]==2)
            {
                if(sol)
                {
                    ok=2;
                    break;
                }
                sol=i;
                ok=1;
            }

        printf("Case #%d: ",nr);
        switch(ok)
        {
            case 1:{printf("%d\n",sol);break;}
            case 2:{printf("Bad magician!\n");break;}
            case 3:{printf("Volunteer cheated!\n");break;}
        }
    }

    return 0;
}
