#include<bits/stdc++.h>
#define mp(x,y) make_pair(x,y)
#define pii pair<int,int>
#define pb push_back


using namespace std;

typedef long long ll;

void counter(int n, int& cur){

    while(n != 0){
        int dig = n % 10;
        n /= 10;
        cur |= (1 << dig);
    }
}
int main(){
    freopen("sheep.in", "r", stdin);
    freopen("sheep.out", "w", stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int t, n, ans;

    cin >> t;

    for(int tc = 1; tc <= t; tc ++){

        cin >> n;

        if(n == 0){
            cout << "Case #" << tc << ": INSOMNIA" << "\n";
            continue;
        }
        int r = 0;
        for(int i = 1; ; i ++){
            counter(n * i, r);
            if(r == (1<<10) - 1){
                ans = n * i;
                break;
            }
        }
        cout << "Case #" << tc << ": " << ans << "\n";
    }

    return 0;
}
