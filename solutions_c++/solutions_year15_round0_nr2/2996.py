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

int extra(){
    int n, best = 0;
    vi V;
    scanf("%d", &n);
    For(i, n) {
        int a;
        scanf("%d", &a);
        V.push_back(a);
        best = max(best, a);
    }
    int b = 0, e = best, m;
    while(e-b > 1) {
        m = (b+e)/2;
        bool ok = 0;
        For(pauz, m) {
            int zvysok = m-pauz;
            int p = 0;
            For(i, V.size()) {
                p+=(V[i]-1)/zvysok;
            }
            if (p<=pauz) ok = 1;
            //if (p<=pauz) printf("   %d %d\n", pauz, p);
        }
        //printf("%d %d\n", m, ok);
        if (ok) e = m;
        else b = m;
    }
    printf("%d\n", e);
}

int main(){
    int T;
    scanf("%d",&T);
    For(i,T){
        printf("Case #%d: ",i+1);
        extra();
    }
}
