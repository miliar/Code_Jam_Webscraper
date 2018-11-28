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
	for(int _z=1;_z<=tt;_z++)
	{
        int n;
        string s;
        cin>>n>>s;
        for(int i=0;i<n+1;i++)
            s[i]-='0';
        int up=s[0];
        int need=0;
        for(int i=1;i<n+1;i++)
        {
            while(s[i] && i>up)
            {
                up++;
                need++;
            }
            up+=s[i];
        }
        printf("Case #%d: %d\n",_z,need);
	}
    return 0;
}
