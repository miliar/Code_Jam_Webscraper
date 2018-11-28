#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
#include<cmath>
using namespace std;
int main()
{
//    freopen("in.txt","r",stdin);
//    freopen("out.txt","w",stdout);
    int t,a,b,c,cnt=0,ans;
    scanf("%d",&t);
    while(t--)
    {
        ans=0;
        cnt++;
        scanf("%d%d%d",&a,&b,&c);
        for(int i=0;i<a;i++)
        {
            for(int j=0;j<b;j++)
            {
                int d=i&j;
                if(d<c)
                    ans++;
            }
        }
        printf("Case #%d: %d\n",cnt,ans);
    }
    return 0;
}
