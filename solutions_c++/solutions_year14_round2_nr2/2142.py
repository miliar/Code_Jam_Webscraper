#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
#include<string>
#include<cmath>

using namespace std;

int abs(int a)
{
    if(a<0) return a*-1;
    return a;
}

int main()
{
    int t;
    scanf("%d",&t);
    for(int tt = 1;tt<=t;tt++)
    {
        int a,b,k;
        cin >> a >> b >> k;
        int ans = 0;
        for(int i=0;i<a;i++)
        {
            for(int j=0;j<b;j++)
            {
                if((i&j) < k)
                {
                    ans++;
                }
                //printf("%d %d %d\n",i,j,i&j);
            }
        }
        printf("Case #%d: %d\n",tt,ans);
    }
    return 0;
}
