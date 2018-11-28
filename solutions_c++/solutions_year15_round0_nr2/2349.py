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

int a[1001];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t,tc=1;
    scanf("%d",&t);
    while(t--)
    {
        int n,x,i;
        scanf("%d",&n);
        int ans = 0;
        for(i=0;i<n;i++)
        {
            scanf("%d",&a[i]);
            ans = max(ans,a[i]);
        }
        for(x=1;x<=1000;x++)
        {
            int tmp = 0 , mx = 0;
            for(i=0;i<n;i++)
            {
                if(a[i] > x)
                {
                    tmp += ((a[i]+x-1)/x)-1;
                    mx = max(mx,x);
                }
                else
                {
                    mx = max(mx,a[i]);
                }
            }
            tmp += mx;
            ans = min(ans,tmp);
        }
        printf("Case #%d: %d\n",tc++,ans);
    }
    return 0;
}

