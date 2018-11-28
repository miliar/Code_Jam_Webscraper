#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
        freopen("abc.txt","w",stdout);
    int t,a,b,k,count,x=0,i,j;
    scanf("%d",&t);
    while(t--)
    {
        x++;
        count=0;
        scanf("%d %d %d",&a,&b,&k);
        for(i=0;i<a;i++)
        {
            for(j=0;j<b;j++)
            {
                if((i&j)<k)
                    count++;
            }
        }
        printf("Case #%d: %d\n",x,count);
    }
    return 0;
}
