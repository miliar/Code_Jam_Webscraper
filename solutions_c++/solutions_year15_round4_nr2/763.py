#include <bits/stdc++.h>
using namespace std;


int god;
int N;
double V, X;

double r[1000];
double x[1000];
double minx, maxx;

int main(){
    freopen("input2.txt", "r", stdin);
    freopen("out3.txt", "w", stdout);
    scanf("%d", &god);
    for(int cc = 1; cc <=god; cc++){
        printf("Case #%d: ", cc);

        cin >> N >> V >> X;
        minx = 99999999;
        maxx = -1;
        for (int i = 0; i<N; i++){
            cin >> r[i] >> x[i];
            minx = min(minx, x[i]);
            maxx = max(maxx, x[i]);
        }

        if (minx > X || maxx < X){
            cout << "IMPOSSIBLE" << endl;
            continue;
        }

        if (N == 1 ) cout << V / r[0] << endl;

        if (N == 2){

            if (x[0] == x[1]){
                double val = V / (r[0] + r[1]);
                printf("%.12f\n", val);
                continue;
            }
            double v2 = (X*V - V*x[0]) / (x[1] - x[0]);
            double v1 = V - v2;

            double t1 = 1.0 * v1 / r[0];
            double t2 = 1.0 * v2 / r[1];
            double ans = max(t1, t2);
            printf("%.12f\n", ans);

        }


    }

}
