#include <bits/stdc++.h>

using namespace std;

const double EPS = 1e-9;

double c, f, x;
double speed = 2.0;
int T;

void solve(){
    double ans = 0;
    speed = 2.0;
    while(1){
        if(x / speed < (c / speed) + (x / (speed + f))){
            ans += (x / speed);
            break;
        }
        else {
            ans += (c / speed);
            speed += f;
        }
    }
    cout << fixed << setprecision(7) << ans << endl;
}

int main(){
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    cin >> T;
    for(int i = 1; i <= T; ++i){
        cin >> c >> f >> x;
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
