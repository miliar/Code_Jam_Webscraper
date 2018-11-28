#define FROM_FILE
#define TO_FILE

//-Wl,--stack,52800000
#include <bits/stdc++.h>

using namespace std;

#define foreach(i, c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define MP make_pair
#define PB push
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

map<vector<int>,int> bfs;
queue<vector<int> > q;
bool isG(vector<int>& v)
{
    int n=v.size();
    int x=0,y=n-1;
    while(x+1<n && v[x+1]>v[x])
        x++;
    while(y && v[y-1]>v[y])
        y--;
    return (y<=x);
}

int main()
{
	ios::sync_with_stdio(false);
	int tt;
	cin>>tt;
	for(int zz=1;zz<=tt;zz++)
    {
        bfs.clear();
        int n;
        cin>>n;
        vector<int> v(n);
        for(int i=0;i<n;i++)
            cin>>v[i];
        while(q.size())q.pop();
        q.PB(v);
        bfs[v]=1;
        int ans=n*n*n;
        while(q.size())
        {
            vector<int> vv=q.front();
            q.pop();
            int me=bfs[vv];
            if(isG(vv)){
                ans=me-1;
                break;
            }
            for(int i=1;i<vv.size();i++)
            {
                swap(vv[i],vv[i-1]);
                int& mm=bfs[vv];
                if(!mm){
                    mm=me+1;
                    q.PB(vv);
                }
                swap(vv[i],vv[i-1]);
            }
        }
        cout<<"Case #"<<zz<<": "<<ans<<endl;
    }
    return 0;
}
