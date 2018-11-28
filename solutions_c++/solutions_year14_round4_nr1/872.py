#define FROM_FILE
#define TO_FILE

//-Wl,--stack,52800000
#include <bits/stdc++.h>

using namespace std;

#define foreach(i, c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define MP make_pair
#define PB push_back
#define FF first
#define SS second
#define All(n) (n).begin(), (n).end()

typedef long long int lli;
typedef unsigned long long int ull;
typedef pair<int,int> pii;
typedef pair<lli,lli> pll;
typedef vector<int> vi;

#ifdef FROM_FILE
void* __VERY__LONG__FROM=freopen("in.txt","r",stdin);
#endif

#ifdef TO_FILE
void* __VERY__LONG__TO=freopen("out.txt","w",stdout);
#endif

//const int MAXN=;
//const int MOD=1000*1000*1000 + 7;
//const lli INF=1000000000000000000ll;

int main()
{
	ios::sync_with_stdio(false);
    int tt;
    cin>>tt;
    for(int z=1;z<=tt;z++)
    {
        int n,m;
        cin>>n>>m;
        vector<int> v(n);
        for(int i=0;i<n;i++)
            cin>>v[i];
        sort(All(v));
        deque<int> dd(n);
        for(int i=0;i<n;i++)
            dd[i]=v[i];
        int ans=0;
        while(dd.size()>1)
        {
            if(dd.back()+dd.front()<=m)
            {
                ans++;
                dd.pop_back();
                dd.pop_front();
            }
            else
            {
                dd.pop_back();
                ans++;
            }
        }
        ans+=dd.size();
        cout<<"Case #"<<z<<": "<<ans<<endl;
    }
    return 0;
}
