#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

char per[16],tmp[16];
int n,m,r,p,s;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int c,t,i,f;
    scanf("%d",&t);
    for(c=0;c<t;c++)
    {
        scanf("%d %d %d %d",&n,&r,&p,&s);
        memset(per,'P',p*sizeof(char));
        memset(per+p,'R',r*sizeof(char));
        memset(per+p+r,'S',s*sizeof(char));
        n=1<<n;
        per[n]='\0';
        f=0;
        do
        {
            memcpy(tmp,per,n*sizeof(char));
            m=n;
            f=0;
            while((m!=1)&&(f==0))
            {
                for(i=0;i<m;i=i+2)
                {
                    if(tmp[i]==tmp[i+1])
                    {
                        f=1;
                        break;
                    }
                    if(((tmp[i]=='P')&&(tmp[i+1]=='R'))||((tmp[i]=='R')&&(tmp[i+1]=='S'))||((tmp[i]=='S')&&(tmp[i+1]=='P')))
                    {
                        tmp[i/2]=tmp[i];
                    }
                    else
                    {
                        tmp[i/2]=tmp[i+1];
                    }
                }
                m=m/2;
            }
        }while((f==1)&&(next_permutation(per,per+n)==true));
        printf("Case #%d: ",c+1);
        if(f==0)
        {
            printf("%s\n",per);
        }
        else
        {
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}
