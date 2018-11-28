#include <iostream>
#include <cstdio>
using namespace std;

int main() {
freopen("A-small-attempt0.in", "r", stdin);
freopen("A-small-attempt0.out", "w", stdout);
    int t; cin >> t;
    for(int tst = 1; tst <= t; ++tst){
        int arr[4][4], arr2[4][4], x, y, cnt = 0, ans;
        cin >> x;
        for(int i = 0; i < 4; ++i) for(int j = 0; j < 4; cin >> arr[i][j++]);
        cin >> y;
        for(int i = 0; i < 4; ++i) for(int j = 0; j < 4; cin >> arr2[i][j++]);
        for(int i = 0; i < 4; ++i){
            for(int j = 0; j < 4; ++j){
                if(arr[x - 1][i] == arr2[y - 1][j]){
                    cnt++; ans = arr[x - 1][i];
                }
            }
        }
        if(cnt > 1) cout << "Case #" << tst << ": " << "Bad magician!\n";
        else if(cnt == 0) cout << "Case #" << tst << ": " << "Volunteer cheated!\n";
        else cout << "Case #" << tst << ": " << ans << endl;
    }
	return 0;
}

