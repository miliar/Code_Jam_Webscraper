#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <stack>
using namespace std;

#define For(i,n) for(int i=0; i<(n); i++)
#define mp(a,b) make_pair((a),(b))
typedef long long ll;
typedef pair<int,int> pii;

int poc=0;
vector<int> M;

void spracuj(ll x) {
    while(x>0) {
        ll c=x%10;
        if(M[c]==0) {M[c]=1; poc++;}
        x/=10;
    }
}

void solve(int por, int n) {
    printf("Case #%d: ",por);
    if(n==0) {printf("INSOMNIA\n"); return;}
    poc=0; M.clear(); M.resize(10,0);
    int k=1;
    while(1) {
        spracuj((ll)k*(ll)n);
        if(poc==10) {printf("%lld\n",(ll)k*(ll)n); return;}
        k++;
    }
}

int main() {
    int t;
    scanf("%d",&t);
    For(i,t) {
        int n;
        scanf(" %d",&n);
        solve(i+1,n);
    }
}
