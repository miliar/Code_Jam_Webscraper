#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;

int n;

string gen (string start) {
    string res = start;
    for (int i = 0; i < n; ++i) {
        string nov;
        for (int j = 0; j < res.size(); ++j) {
            if (res[j] == 'S') nov += "PS";
            else if (res[j] == 'P') nov += "PR";
            else nov += "SR";
        }
        res = nov;
    }
    return res;
}

bool can (string ss, int r, int p, int s) {
    for (int i = 0; i < ss.size(); ++i) {
        if (ss[i] == 'R') {
            if (r == 0) return false;
            r--;
        } else if (ss[i] == 'P') {
            if (p == 0) return false;
            p--;
        } else {
            if (s == 0) return false;
            s--;
        }
    }
    return true;
}

string sort_f (string s, int n) {
    int m = (1<<n);
    for (int i = 0; i < n; ++i) {
        vector <string> ss;
        for (int j = 0; j < m; j += (1<<i)) {
            string r;
            for (int k = 0; k < (1<<i); ++k) {
                r += s[j+k];
            }
            ss.push_back (r);
        }
        for (int i = 0; i < ss.size(); i += 2) {
            if (ss[i] > ss[i+1]) swap (ss[i], ss[i+1]);
        }
        s = "";
        for (int i = 0; i < ss.size(); ++i) s += ss[i];
    }
    return s;
}

int main (void) {
    int t;
    scanf ("%d",  &t);
    for (int c = 1; c <= t; ++c) {
        printf ("Case #%d: ", c);
        int r, p, s;
        scanf ("%d %d %d %d", &n, &r, &p, &s);
        string r1, r2, r3;
        r1 = gen ("S");
        r2 = gen ("P");
        r3 = gen ("R");
        string ans;
        if (can (r1, r, p, s)) {
            ans = r1;
        }
        if ( can (r2, r, p , s)) {
            ans = r2;
        }
        if ( can (r3, r, p, s)) {
            ans = r3;
        } 
        if (ans == "") cout << "IMPOSSIBLE\n";
        else {
            ans = sort_f ( ans, n );
            cout << ans << endl;
        }
    }
    return 0;
}
