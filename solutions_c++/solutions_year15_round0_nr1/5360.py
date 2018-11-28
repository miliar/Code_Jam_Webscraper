#include<iostream>
#include<stdio.h>
#include<assert.h>
using namespace std;


int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    int p[1005];
   // scanf("%d",&T);
   cin>>T;
    for(int cas=0;cas<T;cas++)
    {
        int smax;
        cin>>smax;
        //scanf("%d",&smax);
        string s;
        cin>>s;
        assert((smax +1 )==s.size());
        for(int i=0;i<=smax;i++)
        {
            p[i]= (s[i]-'0');
        }
        int ans=0;
        int now=p[0];
        for(int i=1;i<=smax;i++)
        {
            if(now>= i)
            {
                now+=p[i];
            }else
            {
                ans+=i-now;
                now= i+p[i];
            }
        }
        printf("Case #%d: %d\n",cas+1,ans);

    }
    return 0;
}
