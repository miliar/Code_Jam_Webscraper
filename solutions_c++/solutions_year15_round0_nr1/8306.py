#include <iostream>
#include <vector>
using namespace std;

int get_all_stand(const vector<int> &a) {
    int cnt = a[0], res = 0;
    for (int i = 1; i < a.size(); i++) {
        if (a[i] > 0) {
            res += max(0, i - cnt);
            cnt += res + a[i];
        }
    }
    return res;
}

/* bool can_all_stand(const vector<int> &a) { */
/*     int cnt = a[0]; */
/*     for (int i = 1; i < a.size(); i++) { */
/*         if (a[i] > 0 && cnt < i) { */
/*             return false; */
/*         } */
/*         cnt += a[i]; */
/*     } */
/*     return true; */
/* } */

/* int get_all_stand1(vector<int> &a) { */
/*     int init = a[0]; */
/*     int i; */
/*     for (i = 0; i < 9999; i++) { */
/*         a[0] = init + i; */
/*         if (can_all_stand(a)) { */
/*             break; */
/*         } */
/*     } */
/*     return i; */
/* } */

int main() {
    int t = 0;
    cin >> t;

    for (int n = 1; n <= t; n++) {
        int smax = 0;
        string buf;
        cin >> smax >> buf;
        vector<int> s;
        for (int i = 0; i < buf.size(); i++) {
            s.push_back(buf[i] - '0');
        }
        cout << "Case #" << n << ": " << get_all_stand(s) << endl;
    }
    return 0;
}
