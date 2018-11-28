#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

vector<int> a;

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    cin >> T;
    for (int cas = 1; cas <= T; ++ cas){
        a.clear();
        string s;
        cin >> s;
        for (int i = (int)s.size() - 1; i >= 0; -- i){
            if (s[i] == '+') a.push_back(1);
                        else a.push_back(0);
        }
        int cnt = 0;
        for (int i = 0; i < (int)a.size(); ++ i)
            if ((a[i] + cnt) % 2 != 1) cnt ++;
        printf("Case #%d: %d\n", cas, cnt);
    }
    fclose(stdin);
    fclose(stdout);

    return 0;
}
