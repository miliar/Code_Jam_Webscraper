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
        y = 0, z = 0;
        scanf("%d",&n);
        FOR(i,n){
            scanf("%lf",&a[i]);
            a1[i] = a[i];
        }
        FOR(i,n){
            scanf("%lf",&b[i]);
            b1[i] = b[i];
        }
        sort(a, a + n);
        sort(b, b + n);
        sort(b1, b1 + n);
        sort(a1, a1 + n);
        //printf("%ld",(lower_bound(b,b+n,a[0])-b));
        FOR(i,n){
            FOR(j,n){
                if(a[i] > b[j] && b[j] != 0.0){
                    b[j] = 0.0;
                    //printf("%lf\n",a[i]);
                    z++;
                    break;
                }
            }
        }
        FOR(i,n){
            FOR(j,n){
                if(b1[i] > a1[j] && a1[j] != 0.0){
                    a1[j] = 0.0;
                    //printf("%lf\n",a[i]);
                    y++;
                    break;
                }
            }
        }
        
        printf("Case #%d: %d %d\n",cs++,z,n-y);
    }


}