#include<bits/stdc++.h>

using namespace std;

#define vi vector < int >
#define pii pair < int , int >
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define foreach(it,v) for( __typeof((v).begin())it = (v).begin() ; it != (v).end() ; it++ )
#define ll long long
#define llu unsigned long long
#define MOD 1000000007
#define INF 0x3f3f3f3f
#define dbg(x) { cout<< #x << ": " << (x) << endl; }
#define dbg2(x,y) { cout<< #x << ": " << (x) << " , " << #y << ": " << (y) << endl; }
#define all(x) x.begin(),x.end()
#define mset(x,v) memset(x, v, sizeof(x))
#define sz(x) (int)x.size()

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,tc=1,i;
    scanf("%d",&t);
    while(t--)
    {
        int n;
        scanf("%d",&n);
        string s;
        cin>>s;
        int ans = 0;
        int tot = 0;
        for(i=0;i<=n;i++)
        {
            if(tot < i)
            {
                ans += (i - tot);
                tot += (i - tot);
            }
            tot += (s[i] - '0');
        }
        printf("Case #%d: %d\n",tc++,ans);
    }
    return 0;
}

