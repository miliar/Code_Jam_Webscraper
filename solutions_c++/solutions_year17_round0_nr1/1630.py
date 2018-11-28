#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define forab(i,a,b) for( int i = (a); i < (b); i++ )
#define forn(i,n) forab(i,0,n)
#define pii pair<int,int>
#define pdd pair<double,double>
#define pll pair<ll,ll>

const int MXA = 10001;

int cnt [MXA];
int bts [MXA*4];

void flip(char &c) {
    if (c=='-') {
        c = '+';
    }
    else {
        c = '-';
    }
}

void solve() {
    string s;
    int k;
    cin >> s >> k;
    int n = s.size();
    int ans = 0;
    for (int i = 0; i < n;) {
        if (s[i] == '+') {
            i++;
        }
        else {
            if (i + k > n) {
                printf("IMPOSSIBLE");
                return;
            }
            else {
                ans++;
                forn(j,k) {
                    flip(s[i+j]);
                }
            }
        }
    }
    printf("%d", ans);
}


int main(){
    freopen("input.txt", "r", stdin);    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    forn(i,T){
        printf("Case #%d: ", i+1);
        solve();
        printf("\n");
    }
}