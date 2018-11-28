#include <algorithm>
#include <iostream>
#include <sstream>
#include <string.h>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <ctime>
#include <cctype>
#include <list>

#define INF 2000000000
#define ll long long
#define PI 3.1415926535897932384626433832795
#define all(a) a.begin(), a.end()
#define F first
#define S second
#define pb push_back
#define mp make_pair
#define y1 olololo1
#define y0 olololo2
#define m0(a) memset(a,0,sizeof(a))

using namespace std;
const long long LLINF = 9223372036854775806;
const long double eps = 1e-9;


int t, n, a[201], cur;
int f[201][1201][201], s;


void solve(){
    for (int i=0;i<=n;++i)for(int j=0;j<=1000;++j)for(int k=0;k<=101;++k)f[i][j][k]=-INF;
    f[0][0][0]=cur;
    for (int i=0;i<n;++i)
        for (int j=0;j<=n;++j)
            for (int k=0;k<=n;++k){
                if (f[i][j][k]==-INF) continue;
                f[i][j+1][k]=max(f[i][j+1][k],f[i][j][k]*2-1);
                if (f[i][j][k]*2-1 > a[i+1]) f[i+1][j+1][k]=max(f[i+1][j+1][k],f[i][j][k]*2-1);
                f[i+1][j][k+1]=max(f[i+1][j][k+1],f[i][j][k]);
                if (f[i][j][k]>a[i+1]) f[i+1][j][k]=max(f[i+1][j][k],f[i][j][k]+a[i+1]);
            }
    int res=INF;
    for (int j=0;j<=1000;++j)
        for (int k=0;k<=101;++k)
            if (f[n][j][k]!=-INF)res=min(res,j+k);
    cout << res << endl;
            
}

int main(){
    freopen("A-large-1.in.txt","r",stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin >> t;
    for (int it=0;it<t;++it){
        cin >> cur >> n;
        s=0;
        for (int i=1;i<=n;++i)
            cin >> a[i], s+=a[i];
        sort(a+1,a+n+1);
        cout << "Case #"<<it+1 << ": ";
        solve();
    }
    
    return 0;
    
}