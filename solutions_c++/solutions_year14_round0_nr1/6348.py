#include<iostream>
#include<algorithm>
#include<vector>
#include<cstdio>

using namespace std;

int main(){
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small.out", "w", stdout);
    int T, r1, r2, dump;
    int a[4], b[4];

    cin >> T;
    for(int t = 1; t <= T; ++t){
        cin >> r1;
        for(int i = 1; i <= 4; ++i){
            if(i == r1){
                for(int j = 0; j < 4; ++j){
                    cin >> a[j];
                }
            } else {
                for(int j = 0; j < 4; ++j) cin >> dump;
            }
        }

        cin >> r2;
        for(int i = 1; i <= 4; ++i){
            if(i == r2){
                for(int j = 0; j < 4; ++j){
                    cin >> b[j];
                }
            } else{
                for(int j = 0; j < 4; ++j){
                    cin >> dump;
                }
            }
        }

        vector<int> ans(4);
        sort(a, a+4);
        sort(b, b+4);
        auto it = set_intersection(a, a+4, b, b+4, ans.begin());
        ans.resize(it - ans.begin());
        cout << "Case #" << t << ": ";
        if(ans.size() == 0) cout << "Volunteer cheated!";
        else if(ans.size() == 1) cout << ans[0];
        else cout << "Bad magician!";
        if(t < T) cout << "\n";
    }
    return 0;
}
