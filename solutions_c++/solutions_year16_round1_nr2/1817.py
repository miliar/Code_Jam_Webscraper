#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <bitset>
using namespace std;
#define N 111111
#define M 222222
#define md 1000000007
#define ll long long

int main(){
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int s=1;s<=t;s++){
        int n, m, a, p[3333];
        memset(p, 0, sizeof p);
        scanf("%d",&n);
        m = 2*n - 1;
        for(int i=0;i<m;i++) for(int j=0;j<n;j++) scanf("%d",&a), p[a] ^= 1;
        printf("Case #%d:",s);
        for(int i=0;i<3333;i++) if(p[i]) printf(" %d",i);
        printf("\n");
    }
}