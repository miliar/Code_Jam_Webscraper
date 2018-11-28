#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstdio>

using namespace std;

int n;
double v, x;
double r[100];
double c[100];
double vv[100];
double eps = 1e-6;

void solve1(int caseno)
{
    if (abs(c[0] - x) < eps) {
        double t = v / r[0];
        //if (abs(c[0] - x) > eps)
        //    printf("n %d v %f x %f c0 %f c1 %f s %f\n", n, v, x, c[0], c[1], abs(x - c[0]));
        printf("Case #%d: %.9f\n", caseno, t);
    } else {
       // printf("n %d v %f x %f c0 %f c1 %f\n", n, v, x, c[0], c[1]);
        printf("Case #%d: IMPOSSIBLE\n", caseno);
    }
}

void solve2(int caseno)
{
    if ((c[0] - x > 0 && c[1] - x > 0) || (c[0] - x < 0 && c[1] - x < 0)) {
        //printf("n1 %d v %f x %f c0 %f c1 %f\n", n, v, x, c[0], c[1]);
        printf("Case #%d: IMPOSSIBLE\n", caseno);
    } else if (abs(c[0] - c[1]) < eps) {
        double t = v / (r[0] + r[1]);
        printf("Case #%d: %.9f\n", caseno, t);
    } else {
        vv[0] = v * (x - c[1]) / (c[0] - c[1]);
        vv[1] = v - vv[0];
        double t = max(vv[0] / r[0], vv[1] / r[1]);
        double ans = (c[0] * vv[0] + c[1] * vv[1]) / v - x;
        if (abs(ans) > eps)
            printf("n3 %d v %f x %f c0 %f c1 %f s %f\n", n, v, x, c[0], c[1], abs(ans));
        printf("Case #%d: %.9f\n", caseno, t);
    }
}

void work(ifstream & fin, int caseno)
{
    fin >> n >> v >> x;
    for (int i = 0; i < n; ++i) {
        fin >> r[i] >> c[i];
    }
    if (n == 1)
        solve1(caseno);
    else if (n == 2)
        solve2(caseno);
    else {
        printf("NULL\n");
    }
}


int main()
{
    ifstream fin;
    fin.open("input");
    int t;
    fin >> t;
    for (int i = 0; i < t; ++i) {
        work(fin, i + 1);    
    }
    fin.close();
    return 0;
}
