#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef map<int,int> mii;
typedef vector<int> vi;
typedef vector< vector<int> > vvi;
typedef vector<char> vc;
typedef vector<bool> vb;
typedef vector<string> vs;

#define rep(i,n) for(int i=0;i<n;i++)
#define forup(i,a,b) for(int i=a;i<=b;i++)
#define fordn(i,a,b) for(int i=a;i>=b;i--)
#define all(x) x.begin(),x.end()
#define permute(x) next_permutation(all(x))
#define pb push_back

#define debug if(printf("GD "))
#define mod 1000000007
#define digit(x) ((int(x-'0')))
int main()
{
    int t, sm, cases = 1;
    char str[1005];
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&sm);
        scanf("%s",str);
        int len = strlen(str);
        ll ans = 0, start = 0;
        rep(i,len)
        {
            if(start<i)
            {
                ans = ans + i -start;
                start = i;
            }
            start = start + digit(str[i]);
        }
        printf("Case #%d: %lld\n",cases++,ans);
    }
    return 0;
}
