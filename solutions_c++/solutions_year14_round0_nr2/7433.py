#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

const double EPS = 0.00000001;

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n;
    scanf("%d", &n);

    for (int t = 1; t <= n; t++){
        cout << "Case #" << t << ": ";
        double c, f, x;
        cin >> c >> f >> x;

        double res = x / 2;
        double tmp = 0;
        int cnt = -1;
        while (tmp < res){
            cnt = cnt + 1;
            tmp = tmp + c / (2 + cnt * f);
            if (tmp + x / (2 + cnt * f + f) < res)
                res = tmp + x / (2 + cnt * f + f);

            //if (abs(c / (2 + cnt * f)) < EPS) break;
        }

        printf("%.7lf", res);

        if (t != n) cout << "\n";
    }

    return 0;
}
