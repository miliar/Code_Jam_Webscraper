#include<cstdio>
#include<cstring>

char a[2000];
int b[2000];
int T,smax;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    for(int i=1;i<=T;i++)
    {
        memset(b,0,sizeof(b));
        scanf("%d %s",&smax,a);
        b[0] = 0,b[1] = a[0]-'0';
        for(int i=2;i<smax+1;i++)
            b[i] = b[i-1] + (a[i-1]-'0');

        int cnt = 0;
        //for(int i=1;i<smax+1;i++) printf("%d ",b[i]);
        //printf("\n");
        for(int i=1;i<smax+1;i++)
        {
            if(i - b[i]>0)
            {
                cnt += i-b[i];
                for(int j = i+1;j <smax + 1; j++)
                    b[j] += i-b[i];
            }
        }
        //for(int i=1;i<smax+1;i++) printf("%d ",b[i]);
       // printf("\n");
        printf("Case #%d: %d\n",i,cnt);
    }
    return 0;
}
