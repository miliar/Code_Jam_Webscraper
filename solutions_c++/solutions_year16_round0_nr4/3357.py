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

void solve(int por) {
    int k,c,s;
    scanf(" %d %d %d",&k,&c,&s);
    ll p=1;
    For(i,c-1) p*=k;
    printf("Case #%d:",por);
    For(i,s) printf(" %lld",i*p+1); printf("\n");
}

int main() {
    int t;
    scanf("%d",&t);
    For(i,t) solve(i+1);
}
