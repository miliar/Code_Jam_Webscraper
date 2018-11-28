#include <vector>
#include <iostream>
using namespace std;

char ch[3] = {'R', 'S', 'P'};
string f(int n, int w) {
    if (!n)
        return string(1, ch[w]);
    string s1 = f(n - 1, w);
    string s2 = f(n - 1, (w + 1) % 3);
    if (s1 < s2)
        return s1 + s2;
    return s2 + s1;
}

int count(string s, char c) {
    int res = 0;
    for (int i = 0; i < s.size(); i ++)
        res += (s[i] == c);
    return res;
}

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t ++) {
        int n, cnt[3];
        cin >> n >> cnt[0] >> cnt[2] >> cnt[1];
        string s[3], ans = "ZZZ";
        for (int i = 0; i < 3; i ++) {
            s[i] = f(n, i);
            if (count(s[i], ch[0]) == cnt[0] && count(s[i], ch[1]) == cnt[1])
                if (s[i] < ans)
                    ans = s[i];
        }
        if (ans == "ZZZ") ans = "IMPOSSIBLE";
        cout << "Case #" << t + 1 << ": " << ans << endl;
    }
    return 0;
}
