#include <iostream>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#define lli long long int
#define gc getchar//_unlocked
#define mod 1000000007

using namespace std;

/*
inline lli fastread()
{
    lli number = 0;
    char c = gc();
    while(c < '0')
        c = gc();
    while(c>='0' && c<='9')
    {
        number = (number<<3)+(number<<1)+c-'0';
        c = gc();
    }
    return number;
}
*/

int main()
{
    freopen("te.txt","r",stdin);
    freopen("ans.txt","w",stdout);
    int t,r=0;
    scanf("%d",&t);
    while(t--)
    {
        int n,ans=0,b=0,i;
        char s[10005];
        scanf(" %d",&n);
        scanf(" %s",s);

        for(i=0;i<n+1;i++)
        {
            if(b>=i)
            {
                b+=int(s[i]-'0');
                continue;
            }
            else{
                ans+=i-b;
                b=i+int(s[i]-'0');
            }
        }
        printf("Case #%d: %d\n",++r,ans);

    }

    return 0;
}
