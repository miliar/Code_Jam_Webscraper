//Fruit of Light
//FoL CC
//Apple Strawberry

#include<cstdio>
#include<algorithm>
#include<vector>
#include<iostream>
#include<set>
#include<map>
#include<queue>
#include<cmath>
#include<cstring>

using namespace std;

#define For(i, n) for(int i = 0; i<(n); ++i)
#define INF 1023456789
#define eps 1e-9

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<ll> vll;

string to_bs(int x) {
    string res = "";
    while(x>0) {
        res+='0'+x%2;
        x/=2;
    }
    reverse(res.begin(), res.end());
    return res;
}

int is_nprime(ll x) {
    for(int i = 2; i<=1000; ++i)
        if (x % i == 0) return i;
    return 0;
}

vll check(ll x) {
    vll res;
    for(int i = 2; i<=10; ++i) {
        ll a = stoll(to_bs(x),0,i);
        ll b = is_nprime(a);
        if (b==0) return {};
        res.push_back(b);
    }
    return res;
}   

int extra() {
    int n, k;
    vector<vll> res;
    scanf("%d %d", &n, &k);

    ll a = (1ll<<(n-1))+1;
    while(res.size() < k) {
        auto x = check(a);
        if (x.size()) {
            x.push_back(a);
            res.push_back(x);
            printf("%s", to_bs(x.back()).c_str());
            For(i, int(x.size())-1) printf(" %lld", x[i]);
            printf("\n");
        }
        a+=2;
    }
    /*for(auto x : res) {
        printf("%s", to_bs(x.back()));
        For(i, int(x.size())-1) printf(" %lld", x[i]);
        printf("\n");
    }*/
}

int main() {
    int T;
    scanf("%d",&T);
    For(i,T){
        printf("Case #%d:\n",i+1);
        extra();
    }
}
