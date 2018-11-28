#include <iostream>
#include <vector>
#include <stack>
#include <fstream>
#include <algorithm>
using namespace std;

#define ff first
#define ss second

ofstream fout("a-large-output.txt");

bool evac(vector<pair<int, char>>v, string ans, int total) {
    sort(v.rbegin(), v.rend());
    if (v[0].ff > total/2) return false;
    if (total == 0) {
        fout << ans << endl;
        return true;
    }
    auto v1 = v; v1[0].ff -= 1;
    auto v2 = v; v2[0].ff -= 2;
    auto v3 = v; v3[0].ff -= 1; v3[1].ff -= 1;
    string s1 = " "; s1 += v[0].ss;
    string s2 = " "; s2 += v[0].ss; s2 += v[0].ss;
    string s3 = " "; s3 += v[0].ss; s3 += v[1].ss;
    if (evac(v1, ans + s1, total - 1)) return true;
    if (evac(v2, ans + s2, total - 2)) return true;
    if (evac(v3, ans + s3, total - 2)) return true;
    return false;
}

int main() {
//    ofstream fout("a-small-output.txt");
    int T;
    cin >> T;
    for (int cs = 1; cs <= T; cs++) {
        int n, total = 0;
        cin >> n;
        vector<pair<int, char>> v(n);
        for (int i = 0; i < n; i++) {
            cin >> v[i].first;
            v[i].second = 'A' + i;
            total += v[i].ff;
        }
        fout << "Case #" << cs << ":";
        evac(v, "", total);
    }
}
