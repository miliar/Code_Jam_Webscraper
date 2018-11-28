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
const int MOD=1000*1000*1000 + 7;
//const lli INF=1000000000000000000ll;

string s[10];
int m,n;
vector<string> v[10];

int vv(vector<string>& v)
{
    set<string> st;
    for(int i=0;i<v.size();i++)
    {
        for(int j=0;j<=v[i].size();j++)
            st.insert(v[i].substr(0,j));
    }
    return st.size();
}

int bst=0;
int ways=0;

void bt(int x)
{
    if(x==m)
    {
        int sum=0;
        for(int i=0;i<n;i++)
            sum+=vv(v[i]);
        if(sum>bst)
            bst=sum,ways=0;
        if(sum==bst)
            ways++;
        return;
    }
    for(int i=0;i<n;i++){
        v[i].PB(s[x]);
        bt(x+1);
        v[i].pop_back();
    }
}

int main()
{
	ios::sync_with_stdio(false);
	int tt;
	cin>>tt;
	for(int zz=1;zz<=tt;zz++)
    {
        cin>>m>>n;
        bst=0;
        ways=0;
        for(int i=0;i<m;i++)
            cin>>s[i];
        bt(0);
        cerr<<zz<<endl;
        cout<<"Case #"<<zz<<": "<<bst<<' '<<ways<<endl;
    }
    return 0;
}
