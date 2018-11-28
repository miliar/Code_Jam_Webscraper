#include<bits/stdc++.h>
#define trace1(x)                    cerr << #x << ": " << x << endl;
#define trace2(x, y)                 cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)              cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)           cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
#define trace5(a, b, c, d, e)        cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
#define trace6(a, b, c, d, e, f)     cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;
#define ll long long int
#define MAXN 1002
#define s(i) scanf("%d",&i)
#define sl(i) scanf("%lld",&i)
#define sout(i) printf("%d",i)
#define soutl(i) printf("%lld",i)
#define mp make_pair
#define REP(i,a,n) for(int i=a;i<n;i++)
#define pb push_back
#define pii pair<int,int>
#define vi vector<int>
#define vll vector<ll>

using namespace std;
bool visit[10];
bool check(ll n){
    while(n > 0){
        int rem = n % 10;
        visit[rem] = 1;
        n /= 10;
    }
    for(int i = 0; i < 10; i++)
        if(!visit[i]) return 0;
    return 1;
}
int main(){
freopen("ip.txt", "r", stdin);
freopen("op.txt", "w", stdout);
ll t, n;
cin >> t;
for(int test = 1; test  <= t; test++){
    printf("Case #%d: ", test);
    memset(visit, 0, sizeof(visit));
    cin >> n;
    if(n == 0){
        printf("INSOMNIA\n");
        continue;
    }
    ll m = n;
    while(!check(n)){
        n += m;
    }
    printf("%lld\n", n);
}
return 0;
}
