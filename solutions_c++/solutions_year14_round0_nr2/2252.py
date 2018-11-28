#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>
#include<vector>
#include<algorithm>
#include<map>
#include<queue>
#include<set>
#include<limits.h>
#include<iostream>
using namespace std;
int main()
{
    ios::sync_with_stdio(false);
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,b;
    scanf("%d",&t);
    for(b=1;b<=t;b++)
    {
        double c,f,x;
        scanf("%lf %lf %lf",&c,&f,&x);
        double cookie=2.0;
        double time=0,res=x/cookie,curr=0;
        while(1)
        {
            time+=c/cookie;
            cookie+=f;
            curr=time+x/cookie;
            if(curr>res)
                break;
            else
                res=curr;
        }
        printf("Case #%d: %.7lf\n",b,res);

    }
    return 0;

}
