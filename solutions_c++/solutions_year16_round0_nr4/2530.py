#include <iostream>
#include <stdio.h>
#include <string.h>
#include <set>
#include <math.h>

using namespace std;
typedef long long ll;

int main()
{
    //freopen("D-small-attempt2.in","r",stdin);
    //reopen("A-small-attempt0.out","w",stdout);
    int t,ca;
    int k,c,s;
    scanf("%d",&t);
    for(int ca = 1;ca <= t ; ca++){
        scanf("%d %d %d",&k,&c,&s);
        printf("Case #%d:",ca);
        ll sum = 0;
        for(ll i = 1 ; i <= s ; i++){
            printf(" %I64d",sum+1);
            sum += (ll)(pow(k*1.0,(c-1))+0.1);
        }
        printf("\n");
    }
    return 0;
}
