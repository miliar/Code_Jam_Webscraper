#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <ctime>
#include <climits>
#include <cassert>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <utility>
#include <algorithm>

#define forn(i, n) for (int i = 0; i < int(n); i++)

typedef long long   li;
typedef long double ld;

const int N = 1000000000;
const int INF = 1000000000;

using namespace std;

const double EPS = 1E-9;

struct pt {
	double x, y;

	pt(){}

	pt(double x, double y): x(x), y(y) {}

    bool operator < (const pt &a) const {
		if (fabs(x - a.x) > EPS) return x < a.x;
		return y + EPS < a.y;
	}
    
    bool operator == (const pt &a) const {
    	if (fabs(x - a.x) > EPS) return false;
    	if (fabs(y - a.y) > EPS) return false;
		return true;
	}
};

double det(double a, double b, double c, double d){
	return a*d - b*c;
}

bool in(double l, double r, double x){
	return min(l, r) - EPS <= x && x - EPS <= max(l, r);
}

int sign(double A, double B, double C, double x, double y)
{
    double result = A * x + B * y + C;
    if (result < -EPS)
        return -1;
    if (result > EPS)
        return 1;
    return 0;
}

int intersect_seg(pt a1, pt b1, pt a2, pt b2, pt &res1, pt &res2){
	if (max(a1.x, b1.x) + EPS < min(a2.x, b2.x)) return 0;
	if (max(a1.y, b1.y) + EPS < min(a2.y, b2.y)) return 0;
	if (max(a2.x, b2.x) + EPS < min(a1.x, b1.x)) return 0;
	if (max(a2.y, b2.y) + EPS < min(a1.y, b1.y)) return 0;

	double A1 = a1.y - b1.y;
	double B1 = b1.x - a1.x;
	double C1 = - (A1 * a1.x + B1 * a1.y);

	double A2 = a2.y - b2.y;
	double B2 = b2.x - a2.x;
	double C2 = - (A2 * a2.x + B2 * a2.y);

    if (sign(A1, B1, C1, a2.x, a2.y) * sign(A1, B1, C1, b2.x, b2.y) > 0)
        return 0;

    if (sign(A2, B2, C2, a1.x, a1.y) * sign(A2, B2, C2, b1.x, b1.y) > 0)
        return 0;

	double d = det(A1, B1, A2, B2);
	double d1 = det(C1, B1, C2, B2);
	double d2 = det(A1, C1, A2, C2);

	if (fabs(d) < EPS){
		res1 = max(min(a1, b1), min(a2, b2));
		res2 = min(max(a1, b1), max(a2, b2));
		if (res1 < res2) return 2;
		return 1;
	}
	else {
		res1.x = res2.x = -d1 / d;
		res1.y = res2.y = -d2 / d;
		return 1;
	}
}

double area(vector<pt>& p)
{
    double result = 0;
    int n = p.size();

    forn(i, n)
    {
        int ni = (i + 1) % n;
        result += (p[ni].x - p[i].x) * (p[ni].y + p[i].y) / 2.0;
    }

    return abs(result);
}

int main(int argc, char* argv[])
{
    // freopen("input.txt", "rt", stdin);

    int testCases;
    cin >> testCases;

    forn(testCase, testCases)
    {
        int n;
        cin >> n;
        vector<pt> p(n);
        forn(i, n)
            cin >> p[i].x >> p[i].y;
        vector<pt> pp(p);
        sort(p.begin(), p.end());

        double maxArea = -1E20;
        vector<pt> q;

        int tt = 0;

        do
        {
            bool ok = true;

            forn(i, p.size())
                forn(j, p.size())
                    if (i != j)
                     {
                        int ni = (i + 1) % n;
                        int nj = (j + 1) % n;
                        pt a, b;
                        int r = intersect_seg(p[i], p[ni], p[j], p[nj], a, b);
                        if (r != 0 && abs(i - j) != 1 && abs(i - j) != n - 1)
                        {
                            ok = false;
                        }
                        if (r > 1)
                            ok = false;
                     }

            if (ok)
            {
                tt++;
                double aa = area(p);
                if (aa > maxArea)
                {
                    maxArea = aa;
                    q = p;
                }
            }
        }
        while (next_permutation(p.begin() + 1, p.end()));

        //forn(i, n)
        //    cout << q[i].x << " " << q[i].y << endl;

        //cerr << tt << endl;
        //cerr << maxArea << endl;
        cout << "Case #" << testCase + 1 << ":";

        forn(i, n)
            forn(j, n)
                if (q[i] == pp[j])
                    cout << " " << j;
        cout << endl;
    }

    return 0;
}
