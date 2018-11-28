#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <stack>
#include <math.h>

using namespace std;

        struct Source {
            double r, c;
        };

/*int findPath(int x, int y, char c, vector <vector <char> >& field, int h, vector <vector <bool> >& b) {
   int n = field.size();
    int m = field.front().size();
    b[x][y] = true;
    if (c == '>') {
        for (int i = y + 1; i < m; ++i) {
            if (b[x][i] == true)
                return 0;
            if (field[x][i] != '.')
                return findPath(x, i, field[x][i], field, h + 1, b);
        
        }
        if (h) {
            field[x][y] = '<';
            return 1;
        }
    }
    if (c == '<') {
        for (int i = y - 1; i >= 0; --i) {
            if (b[x][i] == true)
                return 0;
            if (field[x][i] != '.')
                return findPath(x, i, field[x][i], field, h + 1, b);
        }
        if (h) {
            field[x][y] = '>';
            return 1;
        }
    }
    if (c == 'v') {
        for (int i = x + 1; i < n; ++i) {
            if (b[i][y] == true)
                return 0;
            if (field[i][y] != '.')
                return findPath(i, y, field[i][y], field, h + 1, b);
        }
        if (h) {
            field[x][y] = '^';
            return 1;
        }
    }
    if (c == '^') {
        for (int i = x - 1; i >= 0; --i) {
            if (b[i][y] == true)
                return 0;
            if (field[i][y] != '.')
                return findPath(i, y, field[i][y], field, h + 1, b);
        }
        if (h) {
            field[x][y] = 'v';
            return 1;
        }
    }
    return -1;
}*/

long double stupidSolve(long double v, long double x, const vector <Source>& left) {
    long double t1 = v / left[0].r * (x - left[1].c) / (left[0].c - left[1].c) ;
    long double t2 = v / left[1].r * (x - left[0].c) / (left[1].c - left[0].c);
    long double temp = max(t1, t2);
    return temp;
}

long double solve (long double v, long double x, vector <Source>& ss, vector <Source>& left) {
    int n = left.size();
    long double energy = 0;
    long double sumv = 0;
    for (int i = 0; i < n; ++i) {
        energy += left[i].r * left[i].c;
        sumv += left[i].r;
    }
    long double genergy = 0;
    long double gsumv = 0;
    for (vector<Source>::const_iterator iter = ss.begin(); iter != ss.end(); ++iter) {
        genergy += iter->r * iter->c;
        gsumv += iter->r;
    }
    long double t = v / (sumv + gsumv);
    energy *= t;
    genergy *= t;
    if (fabs(energy + genergy - v * x) <= 1e-06) {
        return t;
    }
    if (left.size() == 1) {
        long double gtemp = genergy / gsumv / t;
        return max(v * (x - gtemp) / (left.back().c - gtemp) / left.back().r, v * (x - left.back().c) / (-left.back().c + gtemp) / gsumv);
    }
    vector <Source> tmp = left;
    left.clear();
    long double temp = (v * x - genergy) / v;
    if (energy + genergy > v * x) {
        for (int i = 0; i < n; ++i) {
            if (tmp[i].c - temp > 1e-06) {
                left.push_back(tmp[i]);
            }
            else {
                ss.push_back(tmp[i]);
            }
        }
    }
    else {
        for (int i = 0; i < n; ++i) {
            if (tmp[i].c -temp < -1e-06) {
                left.push_back(tmp[i]);
            }
            else {
                ss.push_back(tmp[i]);
            }
        }
    }
    return solve (v, x, ss, left);

}

int main(int argc, const char * argv[]) {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int t = 0; t < T; ++t) {/*
        int n, m;
        cin >> n >> m;
        bool imp = false;
        vector <vector <char> > field (n, vector <char> (m));
        vector <vector <bool> > b(n, vector <bool> (m));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                cin >> field[i][j];
            }
        }
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                int a = 0;
                if (field[i][j] != '.') {
                    a = findPath(i, j, field[i][j], field, 0, b);
                }
                if (a == -1) {
                    ans = -1;
                    break;
                }
                else {
                    ans += a;
                }
            }
            if (ans == -1)
                break;
        }*/
        int n;
        double v, x;
        cin >> n >> v >> x;
        bool gr = false, less = false;
        vector <Source> ss(n);
        for (int i = 0; i < n; ++i) {
            double r, c;
            cin >> r >> c;
            ss[i].r = r;
            ss[i].c = c;
            if (c - x <= 1e-012)
                less = true;
            if (c - x >= -1e-12)
                gr = true;
        }
        if (!gr || !less) {
            printf ("Case #%d: IMPOSSIBLE\n", t + 1);
            continue;
        }
        vector<Source> sss;
        //long double ans = solve(v, x, sss, ss);
        long double ans = 0;
        if (ss.size() == 1) 
            ans = v / ss[0].r;
        else if (fabs(ss[0].c - ss[1].c) < 1e-06)
            ans = v / (ss[0].r + ss[1].r);
        else
            ans = stupidSolve(v, x, ss);
        printf ("Case #%d: %0.6f\n", t + 1, ans);
    }
    return 0;
}
