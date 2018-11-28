/*
    Just For You 97116:)
*/

#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("laoutput.txt","w",stdout);
    long long int t,n,m,i,j,k,l,x,y,z,flag,count,sum,d;
    scanf("%lld",&t);
    for(z=1;z<=t;z++)
    {
        k=0;
        scanf("%lld",&n);
        int a[2600]={0};
        for(i=0;i<n*2-1;i++)
        {
            for(j=0;j<n;j++)
            {
                scanf("%lld",&x);
                a[x]++;
                if(x>k)
                    k=x;
            }
        }
        printf("Case #%lld: ",z);
        for(i=1;i<=k;i++)
        {
            if(a[i]!=0&&a[i]%2!=0)
                printf("%lld ",i);
        }
        printf("\n");
    }
	return 0;
}