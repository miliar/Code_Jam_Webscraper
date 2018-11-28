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

int n;
vi v(1005);

int compa(){
    int ret=0;
    FOR(i,1,n){
        if(v[i]<v[i-1])
            ret+=(v[i-1]-v[i]);
  //      printf("ret=%d\n",ret);
    }
    return ret;
}

int compb(){
    int mn=-1;
    FOR(i,1,n){
        if(v[i]<v[i-1])
            if(v[i-1]-v[i]>mn)
                mn=v[i-1]-v[i];
    }
    if(mn==-1)
        return 0;

    int ret=0;
    FOR(i,0,n-1){
        if(v[i]<mn)
            ret+=v[i];
        else
           ret+=mn;
    }
    return ret;
}

int main() {
//	ios_base::sync_with_stdio(false);
    freopen("A-large.in","r",stdin);
    freopen("output.out","w",stdout);
	int T;
	cin>>T;

	FORI(t,1,T){
        cin>>n;
 //       v.resize(n+1);
        FOR(i,0,n)
            cin>>v[i];
            int a=compa();
        printf("Case #%d: %d %d\n",t,a,compb());
	}

	return 0;
}
