#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<algorithm>
using namespace std;
int main(void)
{
    int x;
    scanf("%d",&x);
    long long int a,b;
    bool num[10];
    int all=0;
    for(int i=1;i<=x;i++)
    {
        scanf("%lld",&a);
        memset(num,0,sizeof(num));
        all=0;
        printf("Case #%d: ",i);
        b=a;
        if(a==0)
            printf("INSOMNIA\n");
        else
        {
            while(all!=10){
            long long int t=a;
            while(t>0)
            {
                int s=t%10;
                t=t/10;
                if(!num[s])
                    all++;
                num[s]=true;
            }
            if(all==10)
                break;
            a=a+b;
            }
                printf("%lld\n",a);
        }
    }
    return 0;
}
