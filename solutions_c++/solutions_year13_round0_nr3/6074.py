#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<cstdlib>
#include<ctime>
#include<map>
#include<vector>
#include<queue>
#include<string>
#include<stack>
#include<set>
#include<utility>
#include<algorithm>
#include<bitset>

using namespace std;

char str[50];

bool is_pall(long long n)
{
    int i=0;

    while(n)
    {
        str[i++]=n%10+'0';

        n/=10;
    }
    str[i]='\0';

    int len=strlen(str);

    for(int j=0;j<len/2;j++)
    if(str[j]!=str[len-j-1])
    return false;

    return true;
}

//int arr[1050];

int main()
{
    freopen("in1.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int t,cas=1;
    long long h,l,i;

    scanf("%d",&t);

    while(t--)
    {
        long long sum=0;
        double in;

        scanf("%lld %lld",&h,&l);

        in=sqrt(h);
        h=in;

        if(h!=in)
        h=in+1;
        else
        h=in;

        l=sqrt(l);

        for(i=h;i<=l;i++)
        {
            if(is_pall(i)&&is_pall(i*i))
            sum++;
        }
        printf("Case #%d: %lld\n",cas++,sum);
    }
    return 0;
}
