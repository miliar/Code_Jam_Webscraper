#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <cstring>
#include <vector>
using namespace std;
int cnt[2504];
int main(){
    int t, N, x;
    cin >> t;
    for(int test = 1; test <= t; test++){
        cin >> N;
        memset(cnt, 0, sizeof(cnt) );

        for(int i = 0; i < N * (2 * N - 1); i++){
            cin >> x;
            cnt[x]++;
        }
        vector<int> ans;
        for(int i = 1; i <= 2500; i++){
            if(cnt[i] % 2)
                ans.push_back(i);
        }
        sort(ans.begin(), ans.end() );
        cout << "Case #" << test << ":";
        for(int i = 0; i < N; i++)
            cout << " " << ans[i];
        cout << endl;
    }
    return 0;
}
