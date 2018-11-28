#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
        freopen("abc.txt","w",stdout);
    long int t,a,b,k,count,x=0,i,j;
    scanf("%ld",&t);
    //
    while(t--)
    {
        x++;
        count=0;
        scanf("%ld %ld %ld",&a,&b,&k);
        for(i=0;i<a;i++)
        {
            for(j=0;j<b;j++)
            {
                if((i&j)<k)
                    count++;
            }
        }
        printf("Case #%ld: %ld\n",x,count);
    }
    return 0;
}

