#include<iostream>
#include<stack>
#include<queue>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<string>
#include<cstring>
#include<map>
#include<numeric>
#include<sstream>
#include<cmath>
using namespace std;
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define pb push_back
#define f(i,x,y) for(int i = x; i<y; i++ )
#define FORV(it,A) for(vector<int>::iterator it = A.begin(); it!= A.end(); it++)
#define FORS(it,A) for(set<int>::iterator it = A.begin(); it!= A.end(); it++)
#define quad(x) (x) * (x)
#define mp make_pair
#define clr(x, y) memset(x, y, sizeof x)
#define fst first
#define snd second
typedef pair<int, int> pii;
typedef long long ll;
typedef long double ld;


vector <ll> v;
int d[20];
bool pal (ll x){
    int topo = 0;
    while (x){
        d[topo++] = x%10;
        x /= 10;
    }
    for (int i = topo-1, j = 0; i > j; i--, j++){
        if (d[i] != d[j]) return 0;
    }
    return 1;
}



void pre (){
    for (ll i = 1; i <= 10000000;i++){
        if (pal (i) && pal(i*i)) v.pb(i*i);
    }
}



int main (){
    int t;
    pre();
    cin >> t;
    f (tt, 1, t+1){
        printf("Case #%d: ", tt);
        ll a, b;
        cin >> a >> b;
        int ans = 0;
        f (i, 0, v.size()) if (v[i] >= a && v[i] <= b) ans++;
        cout << ans << endl;
    }
    return 0;
}
