#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
using namespace std;
long long a,b,it,backwards,cx,ans;
double x;
int t,T;

bool palin(long long x)
{
    backwards=0;
    cx=x;
    while(cx!=0)
    {
        backwards*=10;
        backwards+=cx%10;
        cx/=10;
    }
    return (x==backwards);

}

int main()
{
    scanf("%d",& T);
    for(t=1;t<=T;t++)
    {
        ans=0;
        scanf("%I64d%I64d",& a,& b);

        x=sqrt(a);
        if (ceil(x) == floor(x)) it=(long long)(x);
        else it=(long long)x+1;

        while(1)
        {
            if (it*it > b) break;

            if (palin(it))
                if (palin(it*it)) ans++;
            it++;
        }

        printf("Case #%d: %I64d\n", t, ans);
    }
return 0;
}
