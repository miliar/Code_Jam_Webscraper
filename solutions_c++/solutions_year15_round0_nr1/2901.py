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

void solve(int cislo) {
    int n;
    scanf(" %d",&n);
    vector<int> A;
    For(i,n+1) {
        char c;
        scanf(" %c",&c);
        A.push_back(c-'0');
    }
    int clap=0;
    int res=0;
    For(i,A.size()) {
        if(A[i]==0) continue;
        if(clap>=i) {clap+=A[i]; continue;}
        res+=i-clap;
        clap=i+A[i];
    }
    printf("Case #%d: %d\n",cislo,res);
}

int main() {
    int t;
    scanf("%d",&t);
    For(i,t) solve(i+1);
}
