#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <set>
using namespace std;

#define CLR(a,b) memset(a,b,sizeof(a))
const double eps = 1e-8;
const int N = 100 + 5;
int n,m;
double x,v;
double c[N],r[N];
bool solve()
{
    if(n == 1){
        if(c[0] != x){
            return 0;
        }else{
            printf("%.12f\n", v / r[0]);
            return 1;
        }
    }
    if(c[1] == c[0]){
        if(c[1] == x){
            printf("%.12f\n",v / (r[1] + r[0]));
            return 1;
        }else{
            return 0;
        }
    }
    double a2 = v * (x - c[0]) / (r[1] * (c[1] - c[0]));
    double a1 = (v - a2 * r[1]) / r[0];
    //printf("%.6f %.6f\n", a1, a2);
    if(a1 + eps < 0 || a2 + eps < 0)return 0;
    //if(a1 < 0 || a2 < 0)return 0;
    //printf("fuck\n");
    printf("%.12f\n",max(a1,a2));
    return 1;
}
int main()
{
    freopen("/Users/lizhen/Documents/Project/Cpp/cpp/cpp/input.txt", "r", stdin);
    freopen("/Users/lizhen/Documents/Project/Cpp/cpp/cpp/output.txt", "w", stdout);
    int T, cas = 0;
    scanf("%d",&T);
    while(T--){
        cas ++;
        printf("Case #%d: ",cas);
        scanf("%d",&n);
        scanf("%lf%lf",&v,&x);
        for(int i = 0 ; i < n ; i ++){
            scanf("%lf %lf",&r[i],&c[i]);
        }
        if(!solve()){
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}