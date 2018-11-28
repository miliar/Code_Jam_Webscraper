#include <fstream>

using namespace std;

string get(int n, int x) {
    if(n == 0)
        return (x == 0? "R" : (x == 1? "P" : "S"));
    string l = get(n - 1, x), r = get(n - 1, (x + 2) % 3);
    if(l < r)
        return l + r;
    else
        return r + l;
}

int main() {
    ifstream in("input.txt");
    ofstream out("output.txt");
    int t;
    in >> t;
    for(int tt = 0; tt < t; tt++) {
        int n, r, p, s;
        in >> n >> r >> p >> s;
        int cnt[3] = {1, 0, 0};
        for(int i = 0; i < n; i++) {
            int cnt0[3] = {0, 0, 0};
            for(int j = 0; j < 3; j++)
                cnt0[(j + 2) % 3] = cnt[j];
            for(int j = 0; j < 3; j++)
                cnt[j] += cnt0[j];
        }
        string ans;
        if(r == cnt[0] && p == cnt[1] && s == cnt[2]) {
            string ans0 = get(n, 0);
            if(ans.empty() || ans0 < ans)
                ans = ans0;
        }
        if(p == cnt[0] && s == cnt[1] && r == cnt[2]) {
            string ans0 = get(n, 1);
            if(ans.empty() || ans0 < ans)
                ans = ans0;
        }
        if(s == cnt[0] && r == cnt[1] && p == cnt[2]) {
            string ans0 = get(n, 2);
            if(ans.empty() || ans0 < ans)
                ans = ans0;
        }
        out << "Case #" << tt + 1 << ": ";
        if(ans.empty())
            out << "IMPOSSIBLE\n";
        else
            out << ans << '\n';
    }
    return  0;
}
