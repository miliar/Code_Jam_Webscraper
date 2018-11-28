#include <bits/stdc++.h>
#define X first
#define Y second
#define psb push_back
#define pob pop_back
#define mp make_pair
#define ll long long
#define scand(n) scanf("%d",&n)
#define scanld(n) scanf("%lld",&n)
#define printd(n) printf("%d\n",n)
#define printld(n) printf("%lld\n",n)
#define all(x) x.begin(),x.end()
#define SET( arr, val) memset(arr,val,sizeof(arr))
#define ITR iterator
#define SZ(arr) arr.size()
#define FOR( i, L, U ) for(int i=(int)L ; i<(int)U ; ++i )
#define FORI( i, L, U ) for(int i=(int)L ; i<=(int)U ; ++i )
#define FORD( i, U, L ) for(int i=(int)U ; i>=(int)L ; --i )
#define Tcases(t) int t;cin>>t;while(t--)

using namespace std;

typedef vector<int> vi;
typedef pair<int,int> pii;

int T,n,cnt;
vector<bool> vis(10);

void chk(int num){
    int dig;
    while(num){
        dig=num%10;
        num/=10;
        if(!vis[dig])
            vis[dig]=1,cnt-=1;
    }
}

void solve(){
    fill(all(vis),0);
    int num=0;
    cnt=10;
    do{
        num+=n;
        chk(num);
    }while(cnt);
    cout<<num<<endl;
}

int main() {
	ios_base::sync_with_stdio(false);
	freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>T;
    FORI(t,1,T){
        cin>>n;
        cout<<"Case #"<<t<<": ";
        if(n==0)
            cout<<"INSOMNIA\n";
        else
            solve();
    }

	return 0;
}
