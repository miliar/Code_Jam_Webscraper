#include <iostream>
#include <cstdio>
using namespace std;


int n,k;
double p[205];
double sol[205][205];
bool in [205];
bool want [205];
double best = 0.0;
double current = 0.0;


double getSmallest() {
    double ans = 2;
    int j = 0;
    for (int i = 1; i<=n; i++) {
        if (p[i] > 2) continue;
        if (ans > p[i]) { ans = p[i]; j=i; }
    }
    p[j] = 10;
    return ans;
}

double getLargest() {
    double ans = 0;
    int j = 0;
    for (int i = 1; i<=n; i++) {
        if (p[i] > 2) continue;
        if (ans < p[i]) { ans = p[i]; j=i; }
    }
    p[j] = 10;
    return ans;
}


void check (int l, int truthCount) {
    if (truthCount > k/2) return;
    if (l == n+1) {
        if (truthCount != k/2) return;
        double val = 1.0;
        for (int i = 1; i<=n; i++) {
            if (!in[i]) continue;
            val *= want[i] ? p[i] : 1.0-p[i];
        }
        //printf(" add %.10f\n", val);
        current+=val;
        return;
    }
    if (!in[l]) { check(l+1, truthCount); return; }

    want[l] = true; check(l+1, truthCount+1);
    want[l] = false; check(l+1, truthCount);
}

void f (int l, int truthCount) {
    if (truthCount > k) return;
    if (l == n+1) {
        if (truthCount != k) return;
        current = 0.0;
        //printf("start now\n");
        check(1, 0);
        if (current > best) best = current;
        return;
    }

    in[l] = true; f(l+1, truthCount+1);
    in[l] = false; f(l+1, truthCount);
}

double calc() {
    f(1,0);
    return best;
}

double calc2() {
    sol[0][0] = 1.0;
    for (int i = 1; i<=n; i++) sol[0][i]=0.0;


    for (int i = 1; i<=k/2; i++) {
        double pn = getLargest(); double qn = 1.0-pn;
        //cout << pn << endl;

        sol[i][0] = qn*sol[i-1][0];
        for (int j = 1; j<=i; j++) {
            sol[i][j] = pn*sol[i-1][j-1] + qn*sol[i-1][j];
        }
    }

    for (int i = k/2+1; i<=k; i++) {
        double pn = getSmallest(); double qn = 1.0-pn;
        //cout << pn << endl;

        sol[i][0] = qn*sol[i-1][0];
        for (int j = 1; j<=i; j++) {
            sol[i][j] = pn*sol[i-1][j-1] + qn*sol[i-1][j];
        }
    }

    return sol[k][k/2];
}




int main()
{
    int t; cin >> t;
    for (int cnt = 1; cnt <= t; cnt++) {
        cin >> n; cin >> k;
        for (int i = 1; i<=n; i++) cin >> p[i];
        best = 0.0;
        double sol = calc();
        //if (sol == 1.0) cout << "Case #" << cnt << ": 1.0" << endl;
        //else if (sol == 0.0) cout << "Case #" << cnt << ": 0.0" << endl;
        //else cout << "Case #" << cnt << ": " << sol << endl;

        printf("Case #%d: %.10f\n", cnt, sol);

    }
    return 0;
}
