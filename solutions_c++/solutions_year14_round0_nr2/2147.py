#include<iostream>
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<stack>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<iomanip>

#define sd(x) scanf("%lld",&x)
#define MP make_pair
#define PB push_back
#define MOD 100000007
#define INF 100000007
#define M 1000000
#define F first
#define S second
#define ll long long
#define LL long long

using namespace std;
long double b[100001], a[100001], c, f, x;

int solve(){
    cin>>c>>f>>x;
    int i;
    a[0] = 0;
    for(i = 1; i <= 100000; i++){
        a[i] = a[i-1] + c/(2+f*(i-1));
    }
    for(i = 0; i <= 100000; i++){
        b[i] = x/(2+f*i);
    }
    long double ans = x;
    for(i = 0; i <= 100000; i++){
        ans = min(ans, a[i] + b[i]);
    }
    cout<<setprecision(7)<<fixed;
    cout<<ans<<endl;
    return 0;
}
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int test, op = 1;
    cin>>test;
    while(test--){
        cout<<"Case #"<<op<<": ";

        solve();
        op++;
    }
}

