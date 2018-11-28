#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define sci(fd) scanf("%d",&fd)
#define scll(fd) scanf("%lld",&fd)
#define pb push_back
#define mp make_pair
#define MOD 1000000007
#define PI 3.1415926535897932
#define pii pair < int,int > 
#define pll pair < ll,ll >
#define fi first
#define se second
#define LOGN 20
const ll infi=1000000000000000009;
char str[10009];
int main()
{
    int t,k,y=0;
    sci(t);
    while(t--)
    {
        scanf("%s",str);
        y++;
        sci(k);
        int i,j,n=strlen(str),ans=0;
        for(i=0;i<n;i++)
        {
            if(str[i]=='-'&&(n-i)>=k)
            {
                ans++;
                for(j=i;j<i+k;j++)
                str[j]=(str[j]=='+')?'-':'+';
            }
        }
        for(i=0;i<n;i++)
        {
            if(str[i]=='-')
            break;
        }
        if(i!=n)
        printf("Case #%d: IMPOSSIBLE\n",y);
        else
        printf("Case #%d: %d\n",y,ans);
    }
    return 0;
}