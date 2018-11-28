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

string s;
int T,n;
int ans;

void rev(int ind){
    int l=0,r=ind,temp;
    while(l<=r){
        temp=s[r];
        s[r]=(s[l]=='+'?'-':'+');
        s[l]=(temp=='+'?'-':'+');
        ++l;
        --r;
    }
}

void solve(int ind){
    if(s[0]=='-'){
        rev(ind);
        ++ans;
        return;
    }
    int l=0;
    while(l<ind && s[l]==s[l+1])
        l++;
    rev(l);
    rev(ind);
    ans+=2;
}

void sol(){
    ans=1;
    FOR(i,1,n)
        if(s[i]!=s[i-1])
            ++ans;
    ans-=(int)(s[n-1]=='+');
}

int main() {
	ios_base::sync_with_stdio(false);
	freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>T;
    FORI(t,1,T){
        cin>>s;
        n=SZ(s);
        sol();
    /*
        for(int i=n-1;i>=0;i--)
            if(s[i]=='-'){

                solve(i);
            }
    */
        cout<<"Case #"<<t<<": "<<ans<<endl;
    }

	return 0;
}
