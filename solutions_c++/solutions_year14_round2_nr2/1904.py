#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;
int main()
{
//    freopen("in.txt","r",stdin);
//    freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    int a,b,k;
    int test=1;
    while(T--)
    {
        scanf("%d%d%d",&a,&b,&k);

        int ans=0;
        for(int i=0;i<a;i++)
            for(int j=0;j<b;j++)
             if((i&j)<k)ans++;

             printf("Case #%d: %d\n",test++,ans);
    }
}
