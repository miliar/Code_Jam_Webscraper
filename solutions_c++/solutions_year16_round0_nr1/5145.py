/// http://www.spoj.com/problems/BLOPER/
#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define ld long double
#define pii pair<int,int>
#define V(x) vector<x>
#define pb push_back
#define mp make_pair
#define mt make_tuple
#define eb emplace_back

#define SORT(ls) sort(ls.begin(), ls.end())
#define DESC(ls) sort(ls.rbegin(), ls.rend());

#define FORLL(i,a,n) for(long long int i=(a); i<(n); ++i)
#define FORDLL(i,a,n) for(long long int i=(a);i>=(n);--i)
#define FOR(c, f, t) for(int c=f;c<t;c++)
#define FORD(c, f, t) for(int c=f;c>=t;c--)
#define rep(i, begin, end) for (__typeof(end) i = (begin) - ((begin) > (end)); i != (end) - ((begin) > (end)); i += 1 - 2 * ((begin) > (end)))

#define memo(a,v) memset(a,v,sizeof(a))
#define CLR(a) memo(a,0)
#define SET(a) memo(a,-1)
#define M 1000000007
#define isactive(x,k) (x&(1<<k))

#define OIN(x) cin>>x
#define DIN(x, y) cin>>x>>y
#define TIN(x, y, z) cin>>x>>y>>z
#define FIN(w, x, y, z) cin>>w>>x>>y>>z

#define SOP(x) cout<<x<<"\n"
#define DOP(x, y) cout<<x<<" "<<y<<"\n"
#define TOP(x, y, z) cout<<x<<" "<<y<<" "<<z<<"\n"
#define FOP(w, x, y, z) cout<<w<<" "<<x<<" "<<y<<" "<<z<<"\n"

#define PRESENT(container, x) container.find(x) != container.end()
#define fi first
#define se second
#define FASTER ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define endl "\n"
#define MAX INT_MAX
#define MIN INT_MIN
#define N 210005
#define MAXN 1000000010
#define DEBUG cout<<"hello\n";
const int dx[] = {-1, 0, 1, 0};
const int dy[] = {0, 1, 0, -1};
int cnt;
bool check(ll int num,int coll[10])
{
    int val;
    while(num>0){
        val=num%10;
        if(!coll[val]){
            coll[val]=1;
            cnt++;
            if(cnt==10)
                return true;
        }
        num=num/10;
    }
    return false;
}
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    OIN(t);
    int t1=t;
    while(t--){
        cnt=0;
        int coll[10]={0};
        ll int num,tmp;
        OIN(num);
        if(num==0){
            cout<<"Case #"<<t1-t<<": "<<"INSOMNIA\n";
            continue;
        }
        tmp=num;
        while(1){
            if(check(tmp,coll)){
                cout<<"Case #"<<t1-t<<": "<<tmp<<endl;
                break;
            }
            tmp+=num;
        }
    }
    return 0;
}
