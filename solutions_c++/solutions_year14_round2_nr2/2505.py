#include<cstdio>
#include<algorithm>
#include<iostream>
#include<cstring>
#include<vector>

using namespace std;
#define ll long long

int main()
{
    int t;
    scanf("%d",&t);
    int loop;
    for(loop=1;loop<=t;loop++)
    {
        ll a,b,k;
        cin>>a>>b>>k;
       int count=0,i,j;

            for(int i=0;i<a;i++)
                for(j=0;j<b;j++)
                    if((i&j)<k)
                    count++;



        printf("Case #%d: %d\n",loop,count);
    }
return 0;
}
