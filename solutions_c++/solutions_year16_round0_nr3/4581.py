#include <bits/stdc++.h>
#define all(v) v.begin(), v.end()
#define sz(v) (int)(v.size())
#define clr(v, d) memset(v, d, sizeof(v))
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define MAX 110


using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector< vector<int> > vvi;
typedef pair<int, int> ii;
typedef vector<ii> vii;

const int OO = (int)1e9+7;
const int MX = (int)1e3+7;
const int mod = (int)1e9+7;

ll N, J, cnt, dvs[11];

ll getDiv(ll n){

    for(ll i=2; i*i<=n; i++){
        if(n%i==0){
            return i;
        }
    }

    return -1;
}

ll pwr(ll x, ll y){

    ll ret = 1;

    for(ll i=0; i<y; i++){
        ret *= x;
    }

    return ret;
}

bool consider(string s){

    ll val[11];
    clr(val, 0);

    for(int j=2; j<=10; j++){
        for(int i=N-1, z=0; i>=0; i--, z++){
            val[j] += (s[i]=='1'? pwr(j, z) : 0);
        }
    }

    for(int i=2; i<=10; i++){
        ll dv = getDiv(val[i]);
        if(dv==-1){
            return false;
        }else{
            dvs[i] = dv;
        }
    }

    return true;
}


void gen(int i, string cur){

    if(i==N){
        if(cnt<J){
            if(consider(cur)){
                cnt++;
                cout<<cur<<" ";
                for(int k=2; k<=10; k++){
                    cout<<dvs[k]<<" ";
                }
                cout<<"\n";

            }
        }
        return;
    }

    if(i!=0 && i!=N-1){
        gen(i+1, cur+"0");
    }
    gen(i+1, cur+"1");

}

int main(void){

    ios_base::sync_with_stdio(false);

    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);

    int t;
    cin>>t;

    for(int cc=1; cc<=t; cc++){

        cnt = 0;
        cin>>N>>J;
        cout<<"Case #"<<cc<<":\n";

        gen(0, "");

    }

    return 0;
}
