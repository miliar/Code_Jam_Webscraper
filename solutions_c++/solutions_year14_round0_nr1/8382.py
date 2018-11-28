#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
long long t,x,y,a[5][5],b[5][5];
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("answer.txt","w",stdout);
    scanf("%lld",&t);
    for(int o=1; o<=t; o++)
    {
        long long ans=0,k=0;
        scanf("%lld",&x);
        for(int i=1; i<=4; i++)
            for(int j=1; j<=4; j++)
                scanf("%lld",&a[i][j]);
        scanf("%lld",&y);
        for(int i=1; i<=4; i++)
            for(int j=1; j<=4; j++)
                scanf("%lld",&b[i][j]);
        for(int i=1; i<=4; i++)
            for(int j=1; j<=4; j++)
                if(a[x][i]==b[y][j])
                {
                    ans++;
                    k=a[x][i];
                }
        printf("Case #%d: ",o);
        if(ans==0) printf("Volunteer cheated!");
        else if(ans>1) printf("Bad magician!");
        else printf("%lld",k);
        printf("\n");
    }
    return 0;
}
