#include <stdio.h>
#include <string.h>
#include<iostream>
using namespace std;
int main()
{

    char s[1051];
  long long  int n,j,k,l,m,t,r,x;
  int i;
     freopen("1.txt","r",stdin);
     freopen("2.txt","w",stdout);
    scanf("%lld",&n);

    for(i=0; i<n; i++)
    {
        scanf("%lld %s",&t,&s);

        k=0;
        m=0;
        for(j=0; j<strlen(s); j++)
        {
            if(s[j]=='0')continue;
            else
            {
                x=s[j]-48;

                if(j<=k)
                {
                    k=k+x;
                    continue;
                }
                else
                {
                    r=j-k;
                    m=m+r;
                    k=k+r+x;
                }
            }
        }
        //cout<<k<<endl;
        //   m=0;

        printf("Case #%d: %lld\n",i+1,m);
    }

    return 0;
}
