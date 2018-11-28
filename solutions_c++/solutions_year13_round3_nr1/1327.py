#include<iostream>
#include<vector>
#include<string.h>
#include<set>
#include<algorithm>
#include<math.h>
#include<stdio.h>
#include<stdlib.h>
using namespace std;

#define s(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
typedef long long int ll;
int main()
{
   int t,i,j,n,l,ans,cnt,mx;
   //ios::sync_with_stdio(false);
   freopen("a.in","r",stdin);
   freopen("a.out","w",stdout);
    cin>>t;
    string s;
    int test=1;
    while(t--)
    {
        cin>>s>>n;
        int ar[s.length()];
        for(i=0;i<s.length();i++)
        {
            if(s[i]!='a' && s[i]!= 'e' && s[i] !='i' && s[i]!='o' && s[i]!='u')
            {
                ar[i] = 1;
            }
            else
            {
                ar[i]  = 0;
            }
        }
        ans=0;
    for(i=0;i<s.length();i++)
    {
        mx=0;
        cnt=0;
        for(j=i;j<s.length();j++)
        {
            if(ar[j] == 1)
            cnt++;
            else
            cnt =0;
            if(cnt>mx)
            mx=cnt;
            if(mx>=n)
            ans++;
        }
    }
    printf("Case #%d: %d\n",test++,ans);
    }
   return 0;
}
