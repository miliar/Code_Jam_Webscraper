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
typedef vector<int> vi;


int extra() {
    int n;
    scanf("%d", &n);
    if (n == 0) {
        printf("INSOMNIA\n");
        return 0;
    }
    ll k = n;
    set<int> S;
    while(S.size() < 10) {
        ll a = k;
        while(a > 0) {
            S.insert(a%10);
            a/=10;
        }
        if (S.size() >= 10) break;
        k += n;
    }
    printf("%lld\n", k);
}

int main(){
    int T;
    scanf("%d",&T);
    For(i,T){
        printf("Case #%d: ",i+1);
        extra();
    }
}
