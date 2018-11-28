#include <iostream>
#include <stdio.h>
#include <math.h>

using namespace std;

bool Check(long long num)
{
    long long temp = num;
    long long rev = 0;

    while(temp)
    {
        rev *= 10;
        rev += temp%10;
        temp /= 10;
    }
    if(num == rev)return true;
    else return false;
}

int main()
{
    freopen("C-small-attempt1.in","r",stdin);
	freopen("output.txt","w",stdout);

    int tCase;
    long long beg,en;
    long long ans;

    scanf("%d",&tCase);
    for(int tNum =1;tNum<=tCase;tNum++)
    {
        scanf("%lld%lld",&beg,&en);
        beg = ceil(sqrt(beg));
        en = sqrt(en);

        ans = 0;

        for(;beg<=en;beg++)
        {
            if(!Check(beg))continue;

            if(Check(beg*beg))ans++;
        }
        printf("Case #%d: %lld\n",tNum,ans);
    }
    return 0;
}
