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

bool check(vector<int>& v,int t,int w)
{
    for(int i=0;i<v.size();i++)
    {
        w-=(v[i]-1)/t;
        if(w<0)
            return 0;
    }
    return 1;
}

bool check(vector<int>& v,int t)
{
    for(int w=0;w<t;w++)
        if(check(v,t-w,w))
            return true;
    return false;

}

int main()
{
	ios::sync_with_stdio(false);
	int tt;
	cin>>tt;
	for(int _z=1;_z<=tt;_z++)
	{
        int n;
        cin>>n;
        vector<int> v(n);
        for(int i=0;i<n;i++)
            cin>>v[i];
        sort(All(v));
        reverse(All(v));
        int d=0;
        int u=1001;
        while(d<u-1)
        {
            int mid=(d+u)/2;
            if(check(v,mid))
                u=mid;
            else
                d=mid;
        }
        printf("Case #%d: %d\n",_z,u);
	}
    return 0;
}
