#include <stdio.h>
#include <iostream>
#define MAXN 1000005
using namespace std;

int T;
long long int N;
long long int ANS[MAXN];
bool seen[10];

void see(int x)
{
    while(x){
        seen[x%10]=true;
        x/=10;
    }
}

bool allseen()
{
    for(int i=0;i<10;i++)if(!seen[i])return false;
    return true;
}

int main()
{
    scanf("%d",&T);
    for(int i=0;i<=100000;i++)ANS[i]=0;
    for(int kase=1;kase<=T;kase++)
    {
        printf("Case #%d: ",kase);

        scanf("%lld", &N);
        if(N==0){puts("INSOMNIA");continue;}
        if(ANS[N]!=0){printf("%d\n",ANS[N]);continue;}
        for(int i=0;i<10;i++)seen[i]=false;
        long long int now=N;
        while(!allseen())
        {
            see(now);
            now+=N;
        }
        printf("%d\n",ANS[N]=now-N);
    }
    return 0;
}
