#include <cstdio>
bool test[10];
void init()
{
    for(int i=0;i<10;i++)test[i]=0;
    return;
}
bool check(int x)
{
    while(x!=0)
    {
        int tmp=x%10;
        x/=10;
        test[tmp]=1;
    }
    for(int i=0;i<10;i++) if(test[i]==0)return 0;
    return 1;
}
int main()
{
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;i++)
    {
        printf("Case #%d: ",i);
        init();
        int N;
        scanf("%d",&N);
        if(N==0)puts("INSOMNIA");
        else
        {
            int x=N;
            while(!check(x))
            {
                x+=N;
            }
            printf("%d\n",x);
        }
    }
    return 0;
}
