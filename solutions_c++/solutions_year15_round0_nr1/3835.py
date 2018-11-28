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


int solve(){
    int n;
    char amtc;
    int amt;

    cin >> n;

    int acc = 0;
    int ans = 0;
    for(int i = 0; i <= n; i++){
        cin >> amtc;
        amt = amtc - '0';


        if(acc < i){
            ans += i - acc;
            acc = i;
        }

        acc += amt;
    }
    return ans;
}

int main()
{
    ios_base::sync_with_stdio(0); cin.tie(0);
    int T;
    cin >> T;

    for(int caso = 1; caso <= T; caso++){
        cout << "Case #" << caso << ": " << solve() << '\n';
    }
}
