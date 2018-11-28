#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<string>
#include<algorithm>
#include<cmath>
#include<vector>
#include<set>
using namespace std;

typedef long long LL;
#define CLR(a,b) memset(a,b,sizeof(a))
const int N = 1000+20;

int n;
double a[N],b[N];
void out(double x[]){
    for(int i = 0; i < n ; i++){
        cout << x[i] << " " ;
    }
    cout << endl;
}
void solve()
{
    int ans = 0;
    int l = 0, r = n - 1;
    for(int i = 0 ; i < n ; i ++){
        if(a[i] < b[l]){
            r -- ;
        }else{
            ans ++;
            l ++;
        }
    }
   // out(a);
   // out(b);
    int fi = ans;
    ans = 0 ;
    l = 0;
    r = n - 1;
    set<double> sb;
    for(int i = 0 ; i< n ;i ++)sb.insert(b[i]);
    set<double>::iterator ite;
    for(int i = 0; i < n ; i ++){
        ite = sb.end();
        double big = *(--ite);
        if(a[i] > big){
            ans ++;
            sb.erase(sb.begin());
        }else{
            ite = sb.upper_bound(a[i]);
            sb.erase(ite);
        }
    }
    int se = ans;
    printf("%d %d\n",fi,se);
}
int main()
{
   // freopen("Dlarge.in","r",stdin);
   // freopen("Dlarge.out","w",stdout);
    int cas = 0;
    int T;
    scanf("%d",&T);
    while(T--){
        cas ++ ;
        printf("Case #%d: ",cas);
        scanf("%d",&n);
        for(int i = 0 ; i < n ; i ++){
            scanf("%lf",&a[i]);
        }
        for(int i = 0 ; i < n ; i ++){
            scanf("%lf",&b[i]);
        }
        sort(a,a+n);
        sort(b,b+n);
        solve();
    }
    return 0;
}
