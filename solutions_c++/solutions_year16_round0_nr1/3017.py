#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;
typedef long long LL;
const int maxm=1000000;

int n,vis=0;

bool check(LL x)
{
     for(;x;x/=10) vis|=(1<<(x%10));
     return (vis==1023);
}

int main()
{
    int TT;
    scanf("%d",&TT);
    for(int i=1;i<=TT;i++)
    {
        scanf("%d",&n);
        printf("Case #%d: ",i);
        LL sum=0; int flag=0; vis=0;
        for(int j=1;j<=maxm;j++)
        {
            sum+=n;
            if(check(sum))
            {
               flag=1;
               cout<<sum<<endl;
               break;
            }
        }
        if(!flag) printf("INSOMNIA\n");
    }
    return 0;
}

