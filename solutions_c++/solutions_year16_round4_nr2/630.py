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

double D[207][207];
vector<double> ludia;
int n,k;

int extra() {
    scanf("%d%d",&n,&k);
    ludia.resize(n);
    For(i, n) scanf("%lf", &(ludia[i]));
    sort(ludia.begin(), ludia.end());

    double best = 0.0;
    For(malych, k+1) {
        vector<double> cast(k);
        For(i, malych) cast[i] = ludia[i];
        For(i, k-malych) cast[k-1-i] = ludia[n-1-i];
        
        For(i, n+5) For(j, k+5) D[i][j] = 0;
        D[0][0] = 1;
        For(i, k) {
            double p = cast[i];
            For(j, k) {
                D[i+1][j+1] += p*D[i][j];
                D[i+1][j] += (1. - p)*D[i][j];
            }
        }
//        printf("%.10lf\n", D[k][k/2]);
        best = max(best, D[k][k/2]);
    }
    printf("%.10lf\n", best);
}

int main(){
    int T;
    scanf("%d",&T);
    For(i,T){
        printf("Case #%d: ",i+1);
        extra();
    }
}
