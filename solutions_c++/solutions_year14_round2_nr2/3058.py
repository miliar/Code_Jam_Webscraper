#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstdlib>
#include<cstring>
#include<stack>
#define ll long long
using namespace std;
int main()
{
		freopen("B-small-attempt0.in","r",stdin);
		freopen("output.txt","w",stdout);

        int t,t1=0,a,b,k,i,j,c;
        ll ans;
        scanf("%d",&t);
        while(t--)
        {
            t1++; ans=0;
            scanf("%d%d%d",&a,&b,&k);
            for(i=0;i<a;i++)
            {
                for(j=0;j<b;j++)
                {
                    c=i&j;
                    if(c < k)
                        ans++;

                }

            }
            printf("Case #%d: %lld\n",t1,ans);

        }



	return 0;
}
