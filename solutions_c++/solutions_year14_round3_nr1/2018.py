#include<stdlib.h>
#include<string.h>
#include<vector>
#include<algorithm>
#include<fstream>
#include<iostream>
#include<math.h>
using namespace std;

int t;
long long x,y,cx,cy,n,co;

int main(){
    long long i,j;
    int t1;
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    
    scanf("%d",&t);
    for(t1=1;t1<=t;t1++)
    {
        scanf("%l64d/%l64d",&x,&y);
        cx = x;
        cy = y;
        for(;cy%2==0 && cx%2==0;)
        {
            cx/=2;
            cy/=2;
        }
        x = cx;
        y = cy;
        //printf("%lld,%lld\n",x,y);
        for(;cy%2==0;)
        {
            cy/=2;
        }
        if(cx%cy!=0)
        {
            printf("Case #%d: impossible\n",t1);
            continue;
        }
        x = x/cy;
        y = y/cy;
        //printf("%lld,%lld\n",x,y);
        for(n=2,co = 1;;n*=2,++co)
        {
            if(y/n<=x)break;
        }
        printf("Case #%d: %lld\n",t1,co);
    }
    scanf(" ");
}
