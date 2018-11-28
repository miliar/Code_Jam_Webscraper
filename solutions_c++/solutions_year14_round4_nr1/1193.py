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

void solve(int num) {
    int n,x;
    scanf("%d %d",&n,&x);
    multiset<int> S;
    For(i,n) {
        int a;
        scanf("%d",&a);
        S.insert(-a);
    }
    int res=0;
    while(S.size()!=0) {
        res++;
        int a=*S.begin();
        S.erase(S.begin());
        int b=x+a;
        b*=-1;
        set<int>::iterator it=S.lower_bound(b);
        if(it!=S.end()) S.erase(it);
    }
    printf("Case #%d: %d\n",num,res);
}

int main() {
    int t;
    scanf("%d",&t);
    For(i,t) solve(i+1);
return 0;
}
