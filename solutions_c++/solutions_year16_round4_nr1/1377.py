#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int n,R,P,S,r,p,s,r1,p1,s1,nr,ok;
char aux[10000],a[10000];
void constructie(int poz,int k,char ch)
{
    if(k==1)
    {
        a[poz]=ch;
        return ;
    }
    else
    {
        if(ch=='R')
        {
            constructie(poz-k/2,k/2,'R');
            constructie(poz,k/2,'S');
        }
        else if(ch=='S')
        {
            constructie(poz-k/2,k/2,'P');
            constructie(poz,k/2,'S');
        }
        else if(ch=='P')
        {
            constructie(poz-k/2,k/2,'P');
            constructie(poz,k/2,'R');
        }
    }
}
int main()
{
    freopen("input","r",stdin);
    freopen("output","w",stdout);
    int Q;
    scanf("%d\n",&Q);
    for(int test=1;test<=Q;test++)
    {
        printf("Case #%d: ",test);

        scanf("%d",&n);
        scanf("%d %d %d",&R,&P,&S);
        nr=R+P+S;
        ///P   R   S
        ///1   2   3
        ok=0;
        for(int o=1;o<=3;o++)
        {
            r=0;p=0;s=0;
            if(o==1)r=1;
            else if(o==2)p=1;
            else if(o==3)s=1;
            for(int i=1;i<=n;i++)
            {
                r1=r+p;
                p1=p+s;
                s1=s+r;
                r=r1;
                p=p1;
                s=s1;
            }
            if(r==R&&p==P&&s==S)
            {
                memset(a,0,sizeof(a));
                if(o==1) constructie(nr,(1<<n),'R');
                else if(o==2) constructie(nr,(1<<n),'P');
                else if(o==3) constructie(nr,(1<<n),'S');
                p=1;
                for(int i=1;i<=n;i++)
                {
                    for(int j=1;j<=nr;j=j+2*p)
                        if(strncmp(a+j,a+p+j,p)>0)
                        {
                            strncpy(aux,a+j,p);
                            strncpy(a+j,a+j+p,p);
                            strncpy(a+j+p,aux,p);
                        }
                    p*=2;
                }
                printf("%s",a+1);
                printf("\n");
                ok=1;
                break;
            }
        }
        if(ok==0)printf("IMPOSSIBLE\n");
    }
    return 0;
}
