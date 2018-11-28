#include <bits/stdc++.h>

#define ff first
#define ss second
#define pb push_back
#define sz size

using namespace std;
typedef long long L;
typedef double D;
typedef vector<L> vi;
typedef vector<vi> vvi;
typedef pair<L,L> ii;
typedef list<int>::iterator lit;

int amtp[5000];

int solve(){
    int d;
    cin >> d;
    memset(amtp, 0, sizeof amtp);
    int x;
    int T = 0;
    for(int i = 0; i < d; ++i){
        cin >> x;
        amtp[x]++;
        T = max(T, x);
    }

    for(int ma = 1; ma < T; ma++){
        int acc = 0;

        for(int i = ma + 1; i <= 3000; i++){
            acc += amtp[i] * (i/ma - !(i%ma));
        }

        T = min(T, acc + ma);
    }
    
    return T;
}

int main()
{
    ios_base::sync_with_stdio(0); cin.tie(0);
#ifdef DEBUG
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int T;
    cin >> T;

    for(int caso = 1; caso <= T; caso++){
        cout << "Case #" << caso << ": " << solve() << '\n';
    }
}
