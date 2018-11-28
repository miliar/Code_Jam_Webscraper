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

int n;
vector<int> A;

int zrataj(int p) {
    int res=0;
    For(i,A.size()) res+=(A[i]+p-1)/p-1;
    return res;
}

void solve(int cislo) {
    scanf("%d",&n);
    A.resize(n);
    For(i,n) scanf(" %d",&A[i]);
    vector<int> V;
    for(int i=1; i<1005; i++) V.push_back(i+zrataj(i));
    int res=1000000;
    For(i,V.size()) res=min(res,V[i]);
    printf("Case #%d: %d\n",cislo,res);
}

int main() {
    int t;
    scanf("%d",&t);
    For(i,t) solve(i+1);
}
