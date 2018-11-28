#include <bits/stdc++.h>
using namespace std;
int test;

bool b[12][(1<<12)+5][(1<<12)+5];


void sol(){
    int n,k;
    cin>>n>>k;
    vector <double> a(n+2);
    auto b=a;

    double ans=0;

    for (int i=1;i<=n;i++) cin>>a[i];
    for (int B=0;B<(1<<(n+1));B+=2)
    if (__builtin_popcount(B)==k){
        vector <vector <double> > v(n+2,b);
        v[0][0]=1;
        for (int i=1;i<=n;i++)
        for (int j=0;j<=k/2;j++)
        v[i][j] = ((B&(1<<i)) && j>0 ? a[i]:0.0)*v[i-1][j-1] + ((B&(1<<i)) ? 1.0 - a[i]:1.0)*v[i-1][j];
        ans=max(ans,v[n][k/2]);
    }
    cout<<"Case #"<<++test<<": ";
    printf("%.9lf\n",ans);
}

int main() {
    freopen("B.in","r",stdin);
    freopen("B.txt","w",stdout);
    int t;
    cin>>t;
    while (t--){
        sol();
    }
    return 0;
}
