using namespace std;

#include <bits/stdc++.h>

#define ll long long int
#define S(a) scanf("%d",&(a))
#define SL(a) scanf("%lld", &(a))
#define P(a) printf("%d",(a))
#define PL(a) printf("%lld",(a))
#define STR(a) scanf("%s",(a))
#define SP printf(" ")
#define NL printf("\n")
#define pb push_back
#define mp make_pair
#define FOR(i,a) for(int (i)=0;(i)<(a);i++)
#define in_T int tc; S(tc); FOR(i,tc)
#define inarr(arr,n) {FOR(i,n) S(arr[i]);}
#define in2arr(arr,n,m) {FOR(i,n) FOR(j,m) S(arr[i][j]);}
#define P2D(arr,n,m) {FOR(i,n){FOR(j,m)printf("%d ",arr[i][j]);NL;}}
#define P1D(arr,n) {FOR(i,n)printf("%d ",arr[i]);NL;}

//int dx[] = {1,0,0,-1};
//int dy[] = {0,1,-1,0};
//int dx[] = {1,0,0,1,1,1,-1,-1};
//int dy[] = {0,1,-1,0,1,-1,1,-1};
template<class T>
T gcd(T a, T b){
    T temp;
    while(b){
        temp = a;
        a = b;
        b = temp % b;
    }
    return a;
}
template<class T>
T power(T n, T r){
    T ret = 1;
    while(r){
        if( r & 1)
            ret = ret * n;
        n = n * n;
        r/=2;
    }
    return ret;
}
double a[1001], b[1001], b1[1001], a1[1001];
int y, z;
int main(){
    int  cs = 1, n;
    double c, f, x;
    in_T{
        scanf("%lf %lf %lf",&c, &f, &x);
        double ans = 0.0;
        double curr = 2.0;
        /*if(c >= x){
            printf("%0.6lf\n",x/2.0);
        }*/
        while(1){
            double temp = double(double(c) / double(curr)) + double(x / double((curr + f)));
            if(temp >= double(x / curr)){
                ans += double(x / curr);
                break;
            }
            else{
                ans += double(double(c) / double(curr));
                curr += f;
            }

        }
        printf("Case #%d: %0.7lf\n",cs++,ans);
    }


}