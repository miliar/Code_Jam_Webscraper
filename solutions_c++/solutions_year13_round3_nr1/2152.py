#include <cmath>
#include<cstdio>
#include <iostream>
#include<cstring>

#define eps 1e-8

#define MAXN 100

using namespace std;



int n;

bool mtx[MAXN * 2 + 10][MAXN * 2 + 10], visited[MAXN * 2 + 10];

struct Point {

    double x, y;

    Point() : x(0), y(0) {}

    Point(double x_, double y_) : x(x_), y(y_) {}

} ps[MAXN * 2 + 10];



int dblcmp(double d)

{

    return fabs(d) < eps ? 0 : d > 0 ? 1 : -1;

}



int xycmp(double p, double mini, double maxi)

{

    return dblcmp(p - mini) * dblcmp(p - maxi);

}



int betweenCmp(Point &O, Point &A, Point &B)

{

    if (fabs(A.x - B.x) > fabs(A.y - B.y))     //选择跨度大的那一维

        return xycmp(O.x, min(A.x, B.x), max(A.x, B.x));

    else return xycmp(O.y, min(A.y, B.y), max(A.y, B.y));

}



double det(double x1, double y1, double x2, double y2)

{

    return x1 * y2 - x2 * y1;

}



int xmul(Point &O, Point &A, Point &B)

{

    return dblcmp(det(A.x - O.x, A.y - O.y, B.x - O.x, B.y - O.y));

}



bool SegCross(Point &A, Point &B, Point &C, Point &D) {

    int d1, d2, d3, d4;

    d1 = xmul(A, C, D);

    d2 = xmul(B, C, D);

    d3 = xmul(C, A, B);

    d4 = xmul(D, A, B);

    if ((d1 ^ d2) == -2 && (d3 ^ d4) == -2) return true;

    if (d1 == 0 && betweenCmp(A, C, D) <= 0 ||

        d2 == 0 && betweenCmp(B, C, D) <= 0 ||

        d3 == 0 && betweenCmp(C, A, B) <= 0 ||

        d4 == 0 && betweenCmp(D, A, B) <= 0) return true;

    return false;

}



bool readin()

{

    int i, j, k;

    double dx, dy;



    cin >> n;

    if (n == 0) return false;



    for (i = 0; i < n; ++i) {

        cin >> ps[i*2].x >> ps[i*2].y >> ps[i*2+1].x >> ps[i*2+1].y;

        dx = ps[i*2].x - ps[i*2+1].x; dy = ps[i*2].y - ps[i*2+1].y;

        ps[i*2].x += dx * 1e-6; ps[i*2+1].x -= dx * 1e-6;

        ps[i*2].y += dy * 1e-6; ps[i*2+1].y -= dy * 1e-6;

    }

    ps[n*2] = Point(0, 0);

    ps[n*2+1] = Point(9999, 9999);



    for (i = 0; i < n * 2 + 2; ++i) {

        for (j = i + 1; j < n * 2 + 2; ++j) {

            mtx[i][j] = true;

            for (k = 0; k < n; ++k) {

                if (i/2 != k && j/2 != k) {

                    mtx[i][j] &= !SegCross(ps[i], ps[j], ps[k*2], ps[k*2+1]);

                }

            }

            mtx[j][i] = mtx[i][j];

        }

    }

    return true;

}



bool dfs(int u)

{

    visited[u] = true;

    if (u == n*2+1) return true;

    for (int v = 0; v < n * 2 + 2; ++v) {

        if (mtx[u][v] && !visited[v])

            if (dfs(v)) return true;

    }

    return false;

}



int main()

{       freopen("in.txt","r",stdin);
    freopen("out2.txt","w",stdout);

    while (readin()) {

        memset(visited, 0, sizeof(visited));

        if (dfs(n*2)) cout << "no" << endl;

        else cout << "yes" << endl;

    }

    return 0;

}
