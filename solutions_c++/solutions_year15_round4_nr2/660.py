#include <bits/stdc++.h>
using namespace std;

const double eps = 1e-7;

bool equal(double x, double y) {
    return fabs(x - y) < eps;
}

bool lesser(string a, string b) {
    if(a.size() < b.size())
        return true;
    if(a.size() > b.size())
        return false;
    return a < b;
}

vector<string> cString, rString;
string xString;

long double solveSmall(int n, double v, double x, vector<double> r, vector<double> c) {

    for(int i = 0; i < n; ++i) {
        r[i] = atof(rString[i].c_str());
        c[i] = atof(cString[i].c_str());
    }

    if(n == 1) {
        if(cString[0] != xString)
            return -10;
        return v / r[0];
    }

    if(cString[0] == cString[1]) {
        if(cString[0] != xString)
            return -10;
        if(lesser(rString[0], rString[1])) 
            swap(r[0], r[1]);
        return v / (r[0] + r[1]);
    }

    if(lesser(cString[0], xString) && lesser(cString[1], xString))
        return -10;
    if(lesser(xString, cString[0]) && lesser(xString, cString[1]))
        return -10;
    
    long double v2 = (x * v - v * c[0]) / (c[1] - c[0]);
    long double v1 = v - v2;

    cerr << (v1 * c[0] + v2 * c[1]) / (v1 + v2) << " " << x << "\n";
    
    if(v1 < 0 - eps || v2 < 0 - eps) {
        return -10;
    }

    return max(v2 / r[1], v1 / r[0]);
}

int main() {
     
    ifstream cin("testB.in");
    ofstream cout("testB.out");

    int t; cin >> t;
    for(int t_case = 1; t_case <= t; ++t_case) {
        cout << "Case #" << t_case << ": ";
        int n; cin >> n;
        vector<double> r(n, 0.0), c(n, 0.0);
        rString = vector<string> (n);
        cString = vector<string> (n);
        xString = "";
        
        string vString = "";
        double v, x; cin >> vString >> xString;
        v = atof(vString.c_str());
        x = atof(xString.c_str());

        for(int i = 0; i < n; ++i)
            cin >> rString[i] >> cString[i];

        long double ans = solveSmall(n, v, x, r, c);

        cout.precision(20);
        if(ans < -1)
            cout << "IMPOSSIBLE\n";
        else
            cout << ans << "\n";
    }
}
