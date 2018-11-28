#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

int k, c, s;

int main(){
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);
    int T;
    cin >> T;
    for (int cas = 1; cas <= T; ++ cas){
        scanf("%d%d%d", &k, &c, &s);
        printf("Case #%d:", cas);
        for (int i = 1; i <= k; ++ i)
            cout << ' ' << i;
        cout << endl;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
