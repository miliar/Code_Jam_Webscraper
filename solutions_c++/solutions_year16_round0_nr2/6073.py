#include<bits/stdc++.h>
#define mp(x,y) make_pair(x,y)
#define pii pair<int,int>
#define pb push_back


using namespace std;

typedef long long ll;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    freopen("pan.in", "r",stdin);
    freopen("pan.out", "w",stdout);
    int t, n;
    string pan;
    cin >> t;

    for(int tc = 1; tc <= t; tc ++){
        cin >> pan;
        int ans = 0;
        n = pan.size();
        for(int i = 0; i < pan.size() - 1; i ++){
            if(pan[i] != pan[i + 1])
                ans ++;
        }

        if(pan[n - 1] == '-')
            ans ++;


        cout << "Case #" << tc << ": " << ans << '\n';
    }

    return 0;
}
