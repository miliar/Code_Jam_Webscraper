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
#define SIZE(X) int(X.size())

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int n;
vi A;

int extra(){
    scanf("%d",&n);
    A.resize(n);
    For(i, n) scanf("%d", &(A[i]));
    int swaps = 0;
    while(SIZE(A)){
        int p = 0;
        For(i, SIZE(A)) if (A[i]<A[p]) p = i;
        swaps+=min(p, SIZE(A)-p-1);
        A.erase(A.begin()+p);
    }
    printf("%d\n",swaps);
}

int main(){
    int T;
    scanf("%d",&T);
    For(i,T){
        printf("Case #%d: ",i+1);
        extra();
    }
}
