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


int T;
int n, h[20], need;

void solve(){
    need=0;
    memset(h,0,sizeof(h));
    for(int it=1;it<=2;++it){
        int row;
        cin>>row;
        need=need*10+row;
        for(int i=1;i<=4;++i)
            for(int j=1;j<=4;++j){
                int x;
                cin>>x;
                h[x]=h[x]*10+i;
            }
    }
    vector<int> canBe;
    for(int i=1;i<=16;++i)
        if (h[i]==need)canBe.pb(i);
    if (canBe.size()==0) cout<<"Volunteer cheated!";
    if (canBe.size()==1)cout<<canBe[0];
    if (canBe.size()>1) cout<<"Bad magician!";
}

int main(){
    freopen("A-small-attempt0.in.txt", "r", stdin);
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
