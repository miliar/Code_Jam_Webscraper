#include <cstdio>
#include <iostream>
#include <map>
#include <sstream>
#include <utility>
#include <vector>
using namespace std;

string basic(string s) {
    char ch = '\0';
    ostringstream oss;
    for (string::iterator it = s.begin(); it != s.end(); ++it) {
        if (*it != ch) {
            oss << *it;
            ch = *it;
        }
    }
    return oss.str();
}

bool ident(vector<string> b) {
    string s = b[0];
    for (int i = 1; i < b.size(); i++)
        if (b[i] != s) return false;
    return true;
}

int conv_cost(string a, string b) {
    vector<int> ra;
    char ch = '\0';
    int c = 0;
    for (string::iterator it = a.begin(); it != a.end(); ++it)
        if (*it != ch) {
            ra.push_back(c);
            c = 0;
            ch = *it;
        } else {
            c++;
        }
    ra.push_back(c);

    vector<int> rb;
    ch = '\0';
    c = 0;
    for (string::iterator it = b.begin(); it != b.end(); ++it) {
        if (*it != ch) {
            rb.push_back(c);
            c = 0;
            ch = *it;
        } else {
            c++;
        }
    }
    rb.push_back(c);

    int s = 0;
    for (int i = 0; i < ra.size(); ++i) {
        s += abs(ra[i] - rb[i]);
    }
    return s;
}

int main(void) {
    int t;
    cin >> t;
    for (int _t = 0; _t < t; _t++) {
        int n;
        cin >> n;
        vector<string> v(n);
        vector<string> b(n);
        for (int _n = 0; _n < n; _n++) {
            cin >> v[_n];
            b[_n] = basic(v[_n]);
        }

        if (!ident(b)) {
            printf("Case #%d: Fegla won\n", _t + 1);
        } else {
            int min_s = 12345678;
            for (vector<string>::iterator from = v.begin(); from != v.end(); ++from) {
                int s = 0;
                for (vector<string>::iterator to = v.begin(); to != v.end(); ++to) {
                    s += conv_cost(*from, *to);
                    // printf("%s %s %d\n", from->c_str(), to->c_str(), conv_cost(*from, *to));
                }
                if (s < min_s)
                    min_s = s;
            }
            int s = 0;
            for (vector<string>::iterator from = v.begin(); from != v.end(); ++from) {
                s += conv_cost(*from, b[0]);
            }
            if (s < min_s)
                min_s = s;
            printf("Case #%d: %d\n", _t + 1, min_s);
        }
    }
}
