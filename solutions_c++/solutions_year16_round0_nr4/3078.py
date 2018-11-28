#include<bits/stdc++.h>
using namespace std;

unsigned long long int power(int x, int y)
{
    unsigned long long int temp;
    if( y == 0)
        return 1;
    temp = power(x, y/2);
    if (y%2 == 0)
        return temp*temp;
    else
        return x*temp*temp;
}

int main()
{
    freopen("D-small-attempt2.in","r",stdin);
    freopen("D-smallHai4.out","w",stdout);
    int t,k,c,s,i,j;
    unsigned long long int d,ans;
    scanf("%d",&t);
    for(j=1;j<=t;j++){
        scanf("%d %d %d",&k,&c,&s);
        ans = 1;
        d = power(k,c-1);
        printf("Case #%d:",j);
        for(i=0;i<k;i++){
            printf(" %llu",ans);
            ans = ans + d;
        }
        printf("\n");
    }
    return 0;
}
