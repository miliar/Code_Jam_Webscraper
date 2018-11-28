#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int,int>;
using pll = pair<ll,ll>;

int T;
int S;
string num;

int main(){
    ios :: sync_with_stdio(false);
    cout << fixed << setprecision(16);


    cin >> T;

    for(int i = 0; i < T; i++){
        int ans = 0;
        cin >> S;
        cin >> num;

        int s = num[0] - '0';
        for(int j = 1; j <= S; j++){
            if((num[j]-'0') > 0 and s < j){
                ans += (j - s);
                s = j;
            }
            s += num[j] - '0';
        }

        cout << "Case #" << (i+1) << ": " << ans << "\n";
    }
    return 0;
}
