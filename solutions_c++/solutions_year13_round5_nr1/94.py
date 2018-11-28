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

ll r,n,x;
ll A[47], B[47];

int extra(){
    n = 37;
    scanf("%lld %lld",&r, &x);
    For(i,n) A[i] = 0;
    For(i,x) scanf("%lld", A+i);
    sort(A, A+n);
    /*int poc = 0;
    while(poc<n && A[poc]==A[0]) poc++;*/

    double best = 0.0;
    For(cool,n){
        ll b = A[0]-1, e = A[0]+r+10, m;
        while(e-b>1){
            m = (b+e)/2;
            ll p = 0;
            For(i,n) {
                p+=max(0LL, m-A[i]+(i>cool));
            }
            if (p>r) e = m;
            else b = m;
        }
        double win = 0;
        ll poc = 0;
        For(i,n) {
            if(i<=cool && b>=A[i]) poc++;
        }
        if (poc<=0) continue;
        For(i,n) {
            win-=max(0LL,b-A[i]+(i>cool));
            if(i<=cool && b>=A[i]) {
                win+=(b-A[i])*36.0/double(poc);
            }
        }
//        printf("*%lf %lld %lld*\n", win, poc,b );
        best = max(best, win);
        
    }
    printf("%.10lf\n",best);

}

int main(){
    int T;
    scanf("%d",&T);
    For(i,T){
        printf("Case #%d: ",i+1);
        extra();
    }
}
