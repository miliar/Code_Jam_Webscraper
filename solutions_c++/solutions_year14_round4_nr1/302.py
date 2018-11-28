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
#define ForEach(it, i) for(typeof i.begin() it = i.begin(); it!=i.end(); ++it)
#define INF 1023456789
#define eps 1e-9

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int n, x, a;
multiset<int> S;

int extra(){
    scanf("%d %d",&n, &x);
    For(i, n) {
        scanf("%d", &a);
        S.insert(-a);
    }
    int pocet = 0;
    while(S.size()){
        pocet++;
        int este = -x-*(S.begin());
        S.erase(S.begin());
        auto it = S.lower_bound(este);
        if (it != S.end()) S.erase(it);
    }
    printf("%d\n", pocet);
}

int main(){
    int T;
    scanf("%d",&T);
    For(i,T){
        printf("Case #%d: ",i+1);
        extra();
    }
}
