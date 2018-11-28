#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string.h>
#include <cstdio>
using namespace std;
int dig[10],size=0;
long long int ans;
long long int asleep(long long int tc)
{
    long long int a=tc,mul=1;
    while(size!=10)
    {
        long long int cpy=mul*a;
        while(cpy>0)
        {
            int d=cpy%10;
            if(dig[d]==0)
            size++,dig[d]=1;
            cpy/=10;
        }
        mul++;
    }
    return a*(mul-1);
}

int main()
{
    long long int n,tc,cnt=1;
    scanf("%lld\n",&n);
    while(n--)
    {
        cin>>tc;
        //cout<<tc<<" ";
        if(tc==0)
        printf("Case #%d: INSOMNIA\n",cnt++);
        else
        {
            printf("Case #%d: ",cnt++);
            cout<<asleep(tc)<<endl;
        }
        //cout<<asleep(tc)<<endl;
        memset(dig,0,sizeof(dig));
        size=0;
    }
    return 0;
}
