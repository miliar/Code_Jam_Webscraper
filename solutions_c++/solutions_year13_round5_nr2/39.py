#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#include <cmath>
#include <cassert>
#include <cstdio>
#include <ctime>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <queue>
#include <deque>
#include <algorithm>
#include <stack>

using namespace std;

#define mp make_pair
#define pb push_back
#define all(v) v.begin(), v.end()

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define for1(i, n) for (int i = 1; i <= (int)(n); i++)
#define forv(i, v) forn(i, v.size())

typedef pair<int, int> pii;
typedef long long ll;

const double EPS = 1e-8;

struct Point
{
    int x, y;
};

double det(double x1, double y1, double x2, double y2)
{
    return x1 * y2 - x2 * y1;
}

double dist(Point& a, Point& b)
{
    return sqrt(1.0 * (a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y));
}

bool onSegm(Point& a, Point& b, Point& c)
{
    return fabs(dist(a, c) + dist(b, c) - dist(a, b)) < EPS;
}

bool intersect(Point &p1, Point &p2, Point &q1, Point &q2)
{
    if (onSegm(p1, p2, q1)) return true;
    if (onSegm(p1, p2, q2)) return true;
    if (onSegm(q1, q2, p1)) return true;
    if (onSegm(q1, q2, p2)) return true;
    double d = det(p2.x - p1.x, q2.x - q1.x, p2.y - p1.y, q2.y - q1.y);
    if (abs(d) < EPS)
    {
        return false;
    }
    double t1 = det(q1.x - p1.x, q2.x - q1.x, q1.y - p1.y, q2.y - q1.y) / d;
    double t2 = det(p2.x - p1.x, p1.x - q1.x, p2.y - p1.y, p1.y - q1.y) / d;
    if (t1 < -EPS || t1 > 1 + EPS || t2 < -EPS || t2 > 1 + EPS)
    {
        return false;
    }
    return true;
}

#define NMAX 12

Point a[NMAX];
int p[NMAX];
bool used[NMAX];
double best;
int bp[NMAX];
int n;

bool check(int i1, int i2, int j1, int j2)
{
    return !intersect(a[i1], a[i2], a[j1], a[j2]);
}

bool onSegm(int i, int j, int k)
{
    return onSegm(a[i], a[j], a[k]);
}

double calc_sq()
{
    double ret = 0;
    forn(i, n)
    {
        ret += (a[p[i]].x - a[p[(i + 1) % n]].x) * (a[p[i]].y + a[p[(i + 1) % n]].y);
    }
    return abs(ret) / 2;
}

void rec(int k)
{
    if (k == n)
    {
        bool ok = true;

        forn(i, n - 1)
        {
            if (i == 0)
            {
                if (onSegm(p[0], p[n - 1], p[1]))
                {
                    ok = false;
                    break;
                }
            }
            else
            if (i == n - 2)
            {
                if (onSegm(p[i], p[i + 1], p[0]))
                {
                    ok = false;
                    break;
                }
            }
            else
            if (!check(p[i], p[i + 1], p[n - 1], p[0]))
            {
                ok = false;
                break;
            }
        } 

        if (ok)
        {
            double s = calc_sq();
            if (s > best)
            {
                best = s;
                forn(i, n) bp[i] = p[i];
            }
        }

        return;
    }

    forn(i, n)
    {
        if (used[i]) continue;
        bool ok = true;
		
        forn(j, k - 1)
        {
            if (j + 1 == k - 1)
            {
                if (onSegm(a[p[j]], a[p[j + 1]], a[i]))
                {
                    ok = false;
                    break;
                }
            }
            else
            if (intersect(a[p[j]], a[p[j + 1]], a[p[k - 1]], a[i]))
            {
                ok = false;
                break;
            }
        }

        if (!ok) continue;
        used[i] = true;
        p[k] = i;
        rec(k + 1);
        used[i] = false;
    }     
}

void solve(int tc)
{
    cerr << tc << endl;
    printf("Case #%d:", tc);
    cin >> n;
    forn(i, n) cin >> a[i].x >> a[i].y;
    best = 0;
    forn(i, n) used[i] = false;
    used[0] = true;
    p[0] = 0;
    rec(1);

    forn(i, n) cout << " " << bp[i];
    cout << endl;
}

int main()
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int tc;
    cin >> tc;
    forn(it, tc) solve(it + 1);
    return 0;
}
