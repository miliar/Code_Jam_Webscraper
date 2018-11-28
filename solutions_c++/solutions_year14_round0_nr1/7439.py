#include <cstdio>
#include <iostream>

using namespace std;

int n;

int main(){
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    scanf("%d", &n);

    for (int t = 1; t <= n; t++){
        int trace[20] = {0};
        int a[20][20], x;

        scanf("%d", &x);
        for (int i = 1; i <= 4; i++)
            for (int j = 1; j <= 4; j++){
                scanf("%d", &a[i][j]);
                if (i == x) trace[a[i][j]]++;
            }

        scanf("%d", &x);
        int res;
        int cnt = 0;
        for (int i = 1; i <= 4; i++)
            for (int j = 1; j <= 4; j++){
                scanf("%d", &a[i][j]);
                if (i == x) trace[a[i][j]]++;
                if (trace[a[i][j]] == 2){
                    res = a[i][j];
                    cnt++;
                }
            }

        cout << "Case #" << t << ": ";

        if (cnt > 1) cout << "Bad magician!";
        if (cnt == 0) cout << "Volunteer cheated!";
        if (cnt == 1) cout << res;

        if (t != n) cout << endl;
    }

    return 0;
}
