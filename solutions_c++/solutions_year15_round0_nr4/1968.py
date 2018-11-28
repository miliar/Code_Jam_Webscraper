#include<iostream>
#include<cstdio>
#include<algorithm>
#include<fstream>
using namespace std;
long long t,x,r,c;
int main()
{
    freopen("D-small-attempt3.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%lld",&t);
    for(int o=1; o<=t; o++)
    {
        scanf("%lld%lld%lld",&x,&r,&c);
        if((r*c)%x!=0)
        {
            printf("Case #%d: RICHARD\n",o);
            continue;
        }
        int k=x-(min(r,c)+1);
        if(k>=min(r,c))
        {
            printf("Case #%d: RICHARD\n",o);
            continue;
        }
        else if(k>0&&r==c)
        {
            printf("Case #%d: RICHARD\n",o);
            continue;
        }
        if(r>=3&&c>=3&&x>=7)
        {
            printf("Case #%d: RICHARD\n",o);
            continue;
        }
        if(min(r,c)==2&&x>=4)
        {
            printf("Case #%d: RICHARD\n",o);
            continue;
        }
        printf("Case #%d: GABRIEL\n",o);
    }
    return 0;
}
