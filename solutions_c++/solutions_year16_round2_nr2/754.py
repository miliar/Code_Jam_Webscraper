#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef pair<string, string> ret_t;

class Solver {
public:
    ret_t solve(string s, string t) {
        int n = s.size();
        int p10 = 1;
        int best_a = -1;
        int best_b = -1;
        int best_diff = 1000;
        pair<string, string> ret;
        for (int i = 0; i < n; ++i) p10 *= 10;
        for (int a = 0; a < p10; ++a) {
            stringstream ss;
            ss << setw(n) << setfill('0') << a;
            string sa = ss.str();
            bool ok = true;
            for (int i = 0; i < n; ++i) {
                if (s[i] != '?' && sa[i] != s[i]) {
                    ok = false;
                    break;
                }
            }
            if (!ok)
                continue;
            for (int b = 0; b < p10; ++b) {
                stringstream ss;
                ss  << setw(n) << setfill('0')<< b;
                string sb = ss.str();
                bool ok = true;
                for (int i = 0; i < n; ++i) {
                    if (t[i] != '?' && sb[i] != t[i]) {
                        ok = false;
                        break;
                    }
                }
                if (!ok)
                    continue;
                bool better = false;
                int diff = abs(a - b);
                if (diff < best_diff)
                    better = true;
                else if (diff == best_diff && a < best_a)
                    better = true;
                else if (diff == best_diff && a == best_a && b < best_b)
                    better = true;
                if (better) {
                    best_a = a;
                    best_b = b;
                    best_diff = diff;
                    ret = make_pair(sa, sb);
                }
            }
        }
        return ret;
    }
    ret_t solve_old(string s, string t) {
        int n = s.size();
        int ld = n;
        bool lt = false;
        bool gt = false;
        for (int i = 0; i < n; ++i) {
            if (s[i] != '?' && t[i] != '?' && s[i] != t[i]) {
                ld = i;
                if (s[i] < t[i])
                    lt = true;
                else if (s[i] > t[i])
                    gt = true;
                break;
            }
        }
        for (int i = ld + 1; i < n; ++i) {
            if (s[i] == '?') s[i] = (gt ? '0' : '9');
            if (t[i] == '?') t[i] = (gt ? '9' : '0');
        }
        if ((lt || gt) && ld - 1 >= 0 && (s[ld-1] == '?' || t[ld-1] == '?')) {
            bool eq_half = false;
            bool gt_half = false;
            string a, b;
            if (gt)
                a = s, b = t;
            else
                a = t, b = s;
            int diff = a[ld] - b[ld];
            if (diff > 5) {
                gt_half = true;
            }
            else if (diff == 5) {
                eq_half = true;
                for (int i = ld + 1; i < n; ++i) {
                    if (a[i] > b[i]) {
                        eq_half = false;
                        gt_half = true;
                        break;
                    }
                    if (a[i] < b[i]) {
                        eq_half = false;
                        break;
                    }
                }
            }


            if (gt_half || eq_half) {
                // gt_half: always make digits [ld-1] differ by 1;
                // eq_half: sometimes "
                int i = ld - 1;
                if (s[i] != '?' && t[i] == '?') {
                    char nv = s[i];
                    if (gt && nv < '9' && gt_half) ++nv;
                    if (lt && nv > '0') --nv;
                    t[i] = nv;
                }
                else if (s[i] == '?' && t[i] != '?') {
                    char nv = t[i];
                    if (lt && nv < '9' && gt_half) ++nv;
                    if (gt && nv > '0') --nv;
                    s[i] = nv;
                }
                else if (s[i] == '?' && t[i] == '?') {
                    s[i] = t[i] = '0';
                    if (gt_half) {
                        if (lt) s[i] = '1';
                        if (gt) t[i] = '1';
                    }
                }

            }
        }
        for (int i = ld - 1; i >= 0; --i) {
            if (s[i] != '?' && t[i] == '?')
                t[i] = s[i];
            else if (s[i] == '?' && t[i] != '?')
                s[i] = t[i];
            else if (s[i] == '?' && t[i] == '?')
                s[i] = t[i] = '0';
        }
        return make_pair(s, t);
    }
};

int main(int argc, char ** argv) {
    string s;
    int N;
    getline(cin, s);
    {
        stringstream A(s);
        A >> N;
    }
    for (int no = 1; no <= N; ++no) {
        cerr //<< "Case "
            << no << " / " << N << endl;
        Solver solver;
        // *** get input ***
        getline(cin, s);
        string s1, t;
        {
            stringstream A(s);
            A >> s1 >> t;
        }
        ret_t ret = solver.solve(s1, t);

        // *** give output ***
        cout << "Case #" << no << ": " << ret.first << ' ' << ret.second << endl; // one line
        //cout << "Case #" << no << ":"; for (int i = 0; i < ret.size(); ++i) cout << " " << ret[i]; cout << endl; // vector
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
