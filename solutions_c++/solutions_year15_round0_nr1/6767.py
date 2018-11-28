#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef vector<pii> vpii;
typedef unsigned long long llu;

#define author ayushtomar
#define debug(x) cerr<<#x<<" "<<x<<endl;
#define f first
#define s second
#define mp make_pair
#define pb push_back
string s1;
int main()
{ freopen("A-small-attempt0.in","r",stdin);
  freopen("output.txt","w",stdout);
    int t,n,ans;
    scanf("%d",&t);
for(int zz=1;zz<=t;zz++)    { int i_have,i_need;
        scanf("%d",&n);
        ans=0;
        cin>>s1;
        i_have=(int)(s1[0]-'0');
        for(int i=1;i<=n;i++)
        {
            if(i>i_have&&s1[i]!='0')
            {ans+=i-i_have;
            i_have+=(i-i_have);}
            i_have+=(s1[i]-'0');
        }
        printf("Case #%d: %d\n",zz,ans);
s1.clear();
    }

return 0;
}
