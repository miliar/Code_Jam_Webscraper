#include<bits/stdc++.h>
using namespace std;

#define sin(x) scanf("%d",&x)
#define sin2(x,y) scanf("%d%d",&x,&y)
#define sin3(x,y,z) scanf("%d%d%d",&x,&y,&z)

#define pb push_back
#define mp make_pair
#define y1 asdnqw
#define next mdamdamda
#define right praviy
#define x first
#define y second
#define endl "\n"
const int N=120007;
int t,n,x;
int w,ans;
const int TL=1e8;
int timer;
inline int f(vector<int> v,int x,int gl){

    int res=1e9;
    ++timer;
    if(timer>TL)return res;
    int ok=1;
    int ll=0;
    sort(v.begin(),v.end());
    reverse(v.begin(),v.end());
    for(int i=0;i<v.size();++i){
        if(v[i]>x)ok=0;
        ll=max(ll,v[i]);
        }
   // cout<<x<<' '<<gl<<' '<<ok<<endl;
    if(ok)return 0;
    if(gl==5)return ll-x;
    res=min(res,f(v,x+1,gl+1)+1);

    vector<int> q=v;
    for(int j=1;j<v[0];++j){
        q[0]-=j;
        q.pb(j);
        res=min(res,f(q,x,gl+1)+1);
        q.pop_back();
        q[0]+=j;
    }

    return res;
}
vector<int> v;
main(){
    //cin.tie(0);ios_base::sync_with_stdio(0);
   freopen("1.txt","r",stdin);freopen("2.txt","w",stdout);
    cin>>t;
    for(int qq=1;qq<=t;++qq){
    cin>>n;
    v.clear();
    for(int i=1;i<=n;++i){
        cin>>x;v.pb(x);
    }
    cout<<"Case #"<<qq<<": "<<f(v,0,0)<<endl;
    }

}
