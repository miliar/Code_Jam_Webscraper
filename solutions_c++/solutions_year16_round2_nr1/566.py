#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>

using namespace std;

const string num[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
const char fea[10] = {'Z', 'O', 'W', 'H', 'U', 'F', 'X', 'V', 'G', 'I'};
const int id[10] = {1, 7, 2, 5, 6, 8, 3, 10, 4, 9};
int h[1000], ans[10];

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    cin >> T;
    for (int cas = 1; cas <= T; ++ cas){
        string s;
        cin >> s;
        memset(h, 0, sizeof(h));
        for (int i = 0; i < s.size(); ++ i)
            h[s[i]] ++;
        for (int k = 1; k <= 10; ++ k)
            for (int i = 0; i < 10; ++ i)
                if (id[i] == k){
                    ans[i] = h[fea[i]];
                    //cout << i << ' ' << ans[i] << endl;
                    for (int j = 0; j < num[i].size(); ++ j)
                        h[num[i][j]] -= ans[i];
                }
        for (int i = 'A'; i <= 'Z'; ++ i)
            if (h[i] != 0) {
                cout << s << endl;
                cout << char(i) << ' ' << h[i] << endl;
                return -1;
            }
        printf("Case #%d: ", cas);
        for (int i = 0; i < 10; ++ i)
            for (int j = 0; j < ans[i]; ++ j)
                cout << i;
        cout << endl;
    }
    fclose(stdin);
    fclose(stdout);

    return 0;
}
