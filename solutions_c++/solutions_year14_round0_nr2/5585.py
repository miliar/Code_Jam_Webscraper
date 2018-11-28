#include <algorithm>
#include <iostream>
#include <string.h>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <map>

#define INF 2147483647
#define LLINF 2000000000000000000
#define ll long long
#define PI 3.1415926535897932384626433832795
#define all(a) a.begin(), a.end()
#define F first
#define S second
#define pb push_back
#define mp make_pair
#define y1 yonigga1
#define y0 yonigga2
#define left lololol
#define right ololololol
#define m0(a) memset(a,0,sizeof(a))
using namespace std;

typedef long double ld;

ld c,f,need;
int T;

void solve(){
    cin>>c>>f>>need;
    ld ans=1e18, prod=2.0, tm=0, cur=0.0;
    for(int i=0;i<=3000000;++i){
        ld will=tm+(need-cur)/prod;
        ans=min(ans,will);
        ld ost=c-cur, delta=ost/prod;
        tm=tm+delta;
        cur=cur+delta*prod-c;
        prod=prod+f;
    }
    cout.precision(9);
    cout<<fixed<<ans;
}


int main(){
    freopen("B-large.in.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin>>T;
    for(int it=1;it<=T;++it){
        cout << "Case #"<<it<<": ";
        solve();
        cout<<'\n';
    }
    
    
    
    return 0;
}
