//Fruit of Light
//FoL CC
//Apple Strawberry

#include<cstdio>
#include<algorithm>
#include<vector>

using namespace std;

#define For(i, n) for(int i = 0; i<(n); ++i)
#define ForEach(it, i) for(typeof i.begin() it = i.begin(); it!=i.end(); ++it)
#define eps 1e-9

typedef long long ll;
typedef pair<int, int> pii;

int r,s;
int a[200][200];
int xr[200];
int xs[200];

int extra(){
    scanf("%d%d",&r,&s);
    For(i, 200) xr[i] = xs[i] = 0;
    For(i, r) For(j, s) {
        scanf("%d", a[i]+j);
        xr[i] = max(xr[i], a[i][j]);
        xs[j] = max(xs[j], a[i][j]);
    }
    For(i, r) For(j, s) {
        if ((xr[i] > a[i][j]) && (xs[j] > a[i][j])){
            //printf("%d %d\n", i, j);
            printf("NO\n");
            return 0;
        }
    }
    printf("YES\n");
}

int main(){
    int T;
    scanf("%d",&T);
    For(i,T){
        printf("Case #%d: ",i+1);
        extra();
    }
}
