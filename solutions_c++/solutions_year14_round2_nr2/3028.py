#include<iostream>
#include<cstdio>
#include<bitset>
#include<string>
using namespace std;

int main()
{
    int t;
    scanf("%d",&t);
    for(int x=1;x<=t;x++)
    {
        long long int a,b,k,c=0;
        cin>>a>>b>>k;
        for(int i=0;i<a;i++)
        {
            for(int j=0;j<b;j++)
        {
            if((i&j)<k)
                c++;
        }
        }
        printf("Case #%d: %d\n",x,i);

    }
}

