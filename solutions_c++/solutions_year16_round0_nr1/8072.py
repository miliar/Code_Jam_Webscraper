#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

bool jud[10];
void init(long long n)
{
    int i;
    while(n>0)
    {
        i=n%10;
        n =n/10;
        jud[i]=true;
    }
}

int main ()
{
    freopen("countingsheep.in","r",stdin);
    freopen("countingsheep.out","w",stdout);
    int T;
    int n,i;int k;
    scanf("%d",&T);
    for(i=1;i<=T;i++)
    {
        int j=1;
        memset(jud,false,sizeof(jud));
        scanf("%d",&n);
        printf("Case #%d: ",i);
        if(n == 0)
        {
            printf("INSOMNIA\n");
            continue;
        }

        while(1)
        {
           bool f=true;
           init(n*j);
           for(k=0;k<=9;k++)
           {
               if(jud[k] == false)
                f=false;
           }
           if(f)
            break;
           j++;
        }
        printf("%lld\n",(long long)n*j);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
