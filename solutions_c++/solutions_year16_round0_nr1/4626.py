#include <bits/stdc++.h>

using namespace std;

const long double INF = INFINITY;
typedef long long ll;
typedef long double ld;

#define s second
#define f first
#define L first
#define R second
#define m0(x) memset(x,0,sizeof(x))
#define pb push_back

#define TASK "problem"

ll n;
char ch;
int c[10];
set<int> s;


void to_s(ll n){
    while(n){
        s.insert(n%10);
        n/=10;
    }
}

int solve(int q){
    s.clear();
    /*int i = 0;
    while(cin>>ch){
        c[i] = ch - 48;
        s.insert(c[i]);
        ++i;
    }

    int k = 2;

    while(s.size()<10){
        for(int j=0;j<i;j++){
            int a = c[i] * k;
            to_s(a);
        }
    }*/
    cin>>n;
    //n = rand()%1000001;
    if(n==0) return cout<<"Case #"<<q<<": INSOMNIA"<<endl,0;
    ll k = 2;
    to_s(n);
    while(s.size()<10){
        ll a = n * k;
        to_s(a);
        ++k;
    }
    --k;
    cout<<"Case #"<<q<<": "<<k*n<<endl;
    return 0;
}

int main(){
    srand(time(0));
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    freopen(TASK".in","r",stdin);
    freopen(TASK".out","w",stdout);
    int t;
    cin>>t;
    //t = rand()%150;
    for(int i=0;i<t;i++)
        solve(i+1);

    return 0;
}
