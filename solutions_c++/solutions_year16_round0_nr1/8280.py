#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp> 

using namespace std;
using namespace __gnu_pbds;

#define INF 1000000007

typedef tree<int, null_type, less<int>, rb_tree_tag,tree_order_statistics_node_update> ordered_set;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<vector<int> > vvi;
typedef pair<int,int> ii;
typedef vector<pair<int,int> > vii;
typedef vector<vector<pair<int,int> > > vvii;

#define all(x) (x).begin(), (x).end()
#define nall(x) (x).rbegin(), (x).rend()
#define sz(a) int((a).size()) 
#define boost ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0)
#define pb push_back 
#define F first
#define S second
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define NFOR(i,a,b) for(int i=(a);i>=(b);--i)
#define TCASE int __T;cin>>__T;FOR(Tc,1,__T)
inline int add(int a,int b, int m=INF){a+=b;if(a>=m)a-=m;return a;}
inline int mul(int a,int b, int m=INF){return (int)(((ll)a*(ll)b)%m);}



int main()
{
    freopen("inp.in","r",stdin);
    freopen("out.txt","w",stdout);
    boost;
    TCASE
    {
        int n;
        cin>>n;
        cout<<"Case #"<<Tc<<": ";
        if(n==0){
            cout<<"INSOMNIA\n";
            continue;
        }
        int ctr=0;vector<bool> a(10);
        int i=2;
        int _n=n;
        while(ctr!=10){
            string s = to_string(_n);
            for(auto it:s){
                if(a[it-'0']==0)
                    {a[it-'0']=1;++ctr;}
            }
            if(ctr==10)break;
            _n+=n;
        }
        cout<<_n<<"\n";

    }
    return 0;
}
