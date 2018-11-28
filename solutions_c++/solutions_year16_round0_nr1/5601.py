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

int a[10];

void update(ll x){

    while(x){
        a[x%10] = 1;
        x /= 10;
    }

}

bool check(){
    int f = 1;
    for(int i=0; i<10; i++){
        if(a[i]==0){
            f = 0;
            break;
        }
    }
    return f;
}

int main(void){

    ios_base::sync_with_stdio(false);

    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);

    int t;
    cin>>t;

    ll n;

    for(int cc=1; cc<=t; cc++){

        cin>>n;

        clr(a, 0);

        int f = 0;
        ll res;
        for(int i=1; i<=10000; i++){
           update(i*n);
           if(check()){
                f = 1;
                res = i*n;
                break;
           }
        }

        cout<<"Case #"<<cc<<": ";

        if(f){
            cout<<res<<"\n";
        }else{
            cout<<"INSOMNIA\n";
        }

    }

    return 0;
}
