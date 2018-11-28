#include<cstdio>
#include<iostream>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<cstring>

#define INF 2000000000
#define INF_LL 2000000000000000000ll
#define MOD_7 1000000007
#define MOD_9 1000000009

typedef long long ll;

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    long long int t,sv,len,i;
    long long int ans=0;
    char s[110];
    scanf("%lld",&t);
    sv=t;

    while(t--)
    {
        ans=0;
        i=0;
        scanf("%s",s);
        len=strlen(s);

        if(s[0]=='-')
        {
            ans=1;
            while(i<len&&s[i]!='+')
            i++;
        }

        while(i<len)
        {
            if(s[i]=='+')
            i++;
            else
            {
                ans+=2;
                while(i<len&&s[i]!='+')
                i++;
            }
        }

        printf("Case #%lld: %lld\n",sv-t,ans);
    }

    return 0;
}
