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
int a[4][4], b[4][4];
int main(){
    int n, cs = 1, m, c, ans;

    in_T{
        c = 0;
        S(n);
        FOR(i,4)
            FOR(j,4)
                S(a[i][j]);
        S(m);
        FOR(i,4)
            FOR(j,4)
                S(b[i][j]);
        FOR(i,4)
            FOR(j,4)
                if(a[n-1][i] == b[m-1][j]){
                    c++;
                    ans = a[n-1][i];
                    break;
                }
        if(c == 1){
            printf("Case #%d: %d\n",cs++,ans);
        }
        else if(c == 0){
            printf("Case #%d: Volunteer cheated!\n",cs++);
        }
        else{
            printf("Case #%d: Bad magician!\n", cs++);
        }
    }


}