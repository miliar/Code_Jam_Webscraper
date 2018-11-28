#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define all(x) (x).begin(), (x).end()
#define x first
#define y second

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef int itn;
typedef pair<int, int> PII;
#define double __float128
const double eps = 1e-11;

struct InputData {
    int n;
    double v, t;
    vector<pair<double, double> > a;
};

struct OutputData {
    string ans;
    void print();
};

InputData readInputData();
OutputData solve(InputData);

int main() {
    freopen( "input.txt", "r", stdin );
    freopen("output.txt", "w", stdout);

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    srand(3242322);

    ld cl0 = clock();

    int t;
    cin >> t;
    future<OutputData> fu[t];

    cerr << "Reading input..." << endl;
    for (int i = 0; i < t; ++i) {
        InputData inputData = readInputData();
        fu[i] = async(launch::async, solve, inputData);
    }

    OutputData res[t];
    cerr << "Waiting for threads..." << endl;
    for (int i = 0; i < t; ++i) {
        res[i] = fu[i].get();
    }


    cerr << "Printing results..." << endl;
    for (int i = 0; i < t; ++i) {
        cout << "Case #" << i + 1 << ": ";
        res[i].print();
        cout << endl;
    }


    cerr << setprecision(3) << fixed;
    cerr << "Time: " << (clock() - cl0) / (CLOCKS_PER_SEC) << " sec." << endl;
    return 0;
}


pair<int, int> dir(char c) {
    if (c == 'v') {
        return mp(1, 0);
    }
    if (c == '>') {
        return mp(0, 1);
    }
    if (c == '<') {
        return mp(0, -1);
    }
    if (c == '^') {
        return mp(-1, 0);
    }
    return mp(0, 0);
}

bool check1(vector<double> V, vector<double> T, int n, double v, double t) {
    double sumV = 0;
    for (int i = 0; i < n; ++i) {
        sumV += V[i];
    }
    if (sumV < v) {
        return false;
    }
    vector<double> a(n);
    for (int i = 0; i < n; ++i) {
        a[i] = 1.0;
    }
    for (int i = 0; i < n && sumV > v + eps; ++i) {
        double delta = min(V[i], sumV - v);
        sumV -= delta;
        a[i] = (V[i] - delta) / V[i];
    }
    vector<int> le;
    vector<int> ri;
    for (int i = 0; i < n; ++i) {
        if (T[i] < t - eps) {
            le.push_back(i);
        } else {
            ri.push_back(i);
        }
    }
    double curT = 0;
    for (int i = 0; i < n; ++i) {
        curT += a[i] * V[i] * T[i];
    }
    curT /= v;
    while (!le.empty() && !ri.empty()) {
        if (fabsl(curT - t) < eps) {
            return true;
        }
        if (curT > t) {
            while (!le.empty() && a[le.back()] > 1.0 - eps) {
                le.pop_back();
            }
            if (le.empty()) {
                return false;
            }
            while (!ri.empty() && a[ri.back()] < eps) {
                ri.pop_back();
            }
            if (ri.empty()) {
                return false;
            }

            int i1 = le.back();
            int i2 = ri.back();
            double vx = a[i1] * V[i1] + a[i2] * V[i2];

            double le = a[i1], ri = min(__float128(1.0L), vx / V[i1]);
            int it = 400;
            double tt = curT - (a[i1] * V[i1] * T[i1] + a[i2] * V[i2] * T[i2]) / v;
            while (it--) {
                double mid = (le + ri) / 2.0;
                double na1 = mid;
                double na2 = (vx - na1 * V[i1]) / V[i2];
                double wT = tt + (na1 * V[i1] * T[i1] + na2 * V[i2] * T[i2]) / v;
                if (wT > t) {
                    le = mid;
                } else {
                    ri = mid;
                }
            }
            double na1 = le;
            double na2 = (vx - na1 * V[i1]) / V[i2];
            a[i1] = na1;
            a[i2] = na2;
            curT = tt + (na1 * V[i1] * T[i1] + na2 * V[i2] * T[i2]) / v;

        } else {
            while (!le.empty() && a[le.back()] < eps) {
                le.pop_back();
            }
            if (le.empty()) {
                return false;
            }
            while (!ri.empty() && a[ri.back()] > 1.0 - eps) {
                ri.pop_back();
            }
            if (ri.empty()) {
                return false;
            }

            int i1 = le.back();
            int i2 = ri.back();
            double vx = a[i1] * V[i1] + a[i2] * V[i2];

            double le = max(__float128(0.0L), (vx - V[i2]) / V[i1]), ri = a[i1];
            int it = 400;
            double tt = curT - (a[i1] * V[i1] * T[i1] + a[i2] * V[i2] * T[i2]) / v;
            while (it--) {
                double mid = (le + ri) / 2.0;
                double na1 = mid;
                double na2 = (vx - na1 * V[i1]) / V[i2];
                double wT = tt + (na1 * V[i1] * T[i1] + na2 * V[i2] * T[i2]) / v;
                if (wT > t) {
                    le = mid;
                } else {
                    ri = mid;
                }
            }
            double na1 = le;
            double na2 = (vx - na1 * V[i1]) / V[i2];
            a[i1] = na1;
            a[i2] = na2;
            curT = tt + (na1 * V[i1] * T[i1] + na2 * V[i2] * T[i2]) / v;
        }
    }
    return fabsl(curT - t) < eps;
}

bool check2(vector<double> V, vector<double> T, int n, double v, double t) {
    double sumV = 0;
    for (int i = 0; i < n; ++i) {
        sumV += V[i];
    }
    if (sumV < v) {
        return false;
    }
    vector<double> a(n);
    for (int i = 0; i < n; ++i) {
        a[i] = 1.0;
    }
    for (int i = 0; i < n && sumV > v + eps; ++i) {
        double delta = min(V[i], sumV - v);
        sumV -= delta;
        a[i] = (V[i] - delta) / V[i];
    }
    vector<int> le;
    vector<int> ri;
    for (int i = 0; i < n; ++i) {
        if (T[i] < t + eps) {
            le.push_back(i);
        } else {
            ri.push_back(i);
        }
    }
    double curT = 0;
    for (int i = 0; i < n; ++i) {
        curT += a[i] * V[i] * T[i];
    }
    curT /= v;
    while (!le.empty() && !ri.empty()) {
        if (fabsl(curT - t) < eps) {
            return true;
        }
        if (curT > t) {
            while (!le.empty() && a[le.back()] > 1.0 - eps) {
                le.pop_back();
            }
            if (le.empty()) {
                return false;
            }
            while (!ri.empty() && a[ri.back()] < eps) {
                ri.pop_back();
            }
            if (ri.empty()) {
                return false;
            }

            int i1 = le.back();
            int i2 = ri.back();
            double vx = a[i1] * V[i1] + a[i2] * V[i2];

            double le = a[i1], ri = min(__float128(1.0L), vx / V[i1]);
            int it = 400;
            double tt = curT - (a[i1] * V[i1] * T[i1] + a[i2] * V[i2] * T[i2]) / v;
            while (it--) {
                double mid = (le + ri) / 2.0;
                double na1 = mid;
                double na2 = (vx - na1 * V[i1]) / V[i2];
                double wT = tt + (na1 * V[i1] * T[i1] + na2 * V[i2] * T[i2]) / v;
                if (wT > t) {
                    le = mid;
                } else {
                    ri = mid;
                }
            }
            double na1 = le;
            double na2 = (vx - na1 * V[i1]) / V[i2];
            a[i1] = na1;
            a[i2] = na2;
            curT = tt + (na1 * V[i1] * T[i1] + na2 * V[i2] * T[i2]) / v;

        } else {
            while (!le.empty() && a[le.back()] < eps) {
                le.pop_back();
            }
            if (le.empty()) {
                return false;
            }
            while (!ri.empty() && a[ri.back()] > 1.0 - eps) {
                ri.pop_back();
            }
            if (ri.empty()) {
                return false;
            }

            int i1 = le.back();
            int i2 = ri.back();
            double vx = a[i1] * V[i1] + a[i2] * V[i2];

            double le = max(__float128(0.0L), (vx - V[i2]) / V[i1]), ri = a[i1];
            int it = 400;
            double tt = curT - (a[i1] * V[i1] * T[i1] + a[i2] * V[i2] * T[i2]) / v;
            while (it--) {
                double mid = (le + ri) / 2.0;
                double na1 = mid;
                double na2 = (vx - na1 * V[i1]) / V[i2];
                double wT = tt + (na1 * V[i1] * T[i1] + na2 * V[i2] * T[i2]) / v;
                if (wT > t) {
                    le = mid;
                } else {
                    ri = mid;
                }
            }
            double na1 = le;
            double na2 = (vx - na1 * V[i1]) / V[i2];
            a[i1] = na1;
            a[i2] = na2;
            curT = tt + (na1 * V[i1] * T[i1] + na2 * V[i2] * T[i2]) / v;
        }
    }
    return fabsl(curT - t) < eps;
}

OutputData solve(InputData in) {
    OutputData out;
    int n = in.n;
    double v = in.v;
    double t = in.t;
    vector<pair<double, double> > a = in.a;
    double minT = 1e9;
    double Rmi = -1;
    double maxT = -10;
    double Rma = -1;
    for (int i = 0; i < n; ++i) {
        if (minT > a[i].y) {
            minT = a[i].y;
            Rmi = a[i].x;
        }
        if (maxT < a[i].y) {
            maxT = a[i].y;
            Rma = a[i].x;
        }
    }
    if (t < minT - 100 * eps || t > maxT + 100 * eps) {
        out.ans = "IMPOSSIBLE";
        return out;
    }
    double ans = 0;
    if (fabsl(maxT - minT) < eps) {
        double rate = 0;
        for (int i = 0; i < n; ++i) {
            rate += a[i].x;
        }
        ans = v / rate;
    } else {
        double Time = max((t - minT) * v / Rma / (maxT - minT), (maxT - t) * v / Rmi / (maxT - minT));
        ans = Time;

        double l = 0, r = 2 * Time;
        int it = 400;
        while (it--) {
            double m = (l + r) / 2.0;
            vector<double> V(n);
            vector<double> T(n);
            for (int i = 0; i < n; ++i) {
                V[i] = a[i].x * m;
                T[i] = a[i].y;
            }
            if (check1(V, T, n, v, t) || check2(V, T, n, v, t)) {
                r = m;
            } else {
                l = m;
            }
        }
        ans = l;
    }
    stringstream ss;
    ss << setprecision(10) << fixed;
    ss << (ld)ans;
    out.ans = ss.str();
    return out;
}

InputData readInputData() {
    InputData inp;
    cin >> inp.n;
    ld v, t;
    cin >> v >> t;
    inp.v = v; inp.t = t;

    inp.a.resize(inp.n);
    for (int i = 0; i < inp.n; ++i) {
        ld x, y;
        cin >> x >> y;
        inp.a[i].x = x; inp.a[i].y = y;
    }
    return inp;
}

void OutputData::print() {
    cout << ans;
}