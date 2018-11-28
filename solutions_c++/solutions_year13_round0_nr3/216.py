#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

typedef vector<int> bigint;

vector<string> ans;

string bigintToString(const bigint& n) {
    string s = "";
    for (int i = 0; i < (int)n.size(); ++i) {
        s += n[i] + '0';
    }
    return s;
}

bool add(bigint& square, bigint& root, int pos, int times) {
    //printf("add [%s] [%s] %d %d\n", bigintToString(square).c_str(), bigintToString(root).c_str(), pos, times);
    bool ret = true;
    for (int i = 0; i < (int)root.size(); ++i) {
        if ((square[pos + i] += root[i] * times) >= 10) {
            ret = false;
        }
    }
    root[pos] += times;
    for (int i = 0; i < (int)root.size(); ++i) {
        if ((square[pos + i] += root[i] * times) >= 10) {
            ret = false;
        }
    }
    return ret;
}

void dfs(int l, int r, int len, bigint& root, bigint& square) {
    //printf("dfs %d %d %d [%s] [%s]\n", l, r, len, bigintToString(root).c_str(), bigintToString(square).c_str());
    if (l > r) {
        string s = "";
        for (int i = 0; i < (int)square.size(); ++i) {
            s += square[i] + '0';
        }
        int st = 0, ed = (int)s.length();
        for (; st < ed && s[st] == '0'; ++st, --ed);
        if (st < ed) {
            s = s.substr(st, ed - st);
            ans.push_back(s);
        }
    } else if (l == r) {
        do {
            dfs(l + 1, r - 1, len, root, square);
        } while (add(square, root, l, 1));
        add(square, root, l, -root[l]);
    } else {
        do {
            dfs(l + 1, r - 1, len, root, square);
        } while (add(square, root, l, 1) && add(square, root, r, 1));
        add(square, root, l, -root[l]);
        add(square, root, r, -root[r]);
    }
}

void init() {
    static const int ns[] = {51, 52};
    for (int i = 0; i < 2; ++i) {
        int t = ns[i];
        bigint root(t, 0);
        bigint square(t * 2 - 1, 0);
        dfs(0, t - 1, t, root, square);
    }
}

int T;
char A[1001], B[1001];

class Cmp {
public:
    bool operator()(const string& lhs, const string& rhs) {
        if (lhs.length() != rhs.length()) {
            return lhs.length() < rhs.length();
        } else {
            return lhs < rhs;
        }
    }
} cmp;

int gao(string s, bool minus) {
    if (minus) {
        s[s.length() - 1] -= 1;
        for (int i = (int)s.length() - 1; s[i] < '0'; --i) {
            s[i] += 10;
            s[i - 1] -= 1;
        }
        if (s[0] == '0') {
            // this will produce the correct result even if s == "0"
            s.erase(s.begin());
        }
    }
    //printf("[%s] %d\n", s.c_str(), upper_bound(ans.begin(), ans.end(), s, cmp) - ans.begin());
    return upper_bound(ans.begin(), ans.end(), s, cmp) - ans.begin();
}

int main() {
    init();
    sort(ans.begin(), ans.end(), cmp);
    /*
    printf("%d\n", (int)ans.size());
    for (int i = 0; i < (int)ans.size(); ++i) {
        printf("%s\n", ans[i].c_str());
    }
    //*/
    scanf("%d", &T);
    for (int caseNum = 1; caseNum <= T; ++caseNum) {
        scanf("%s%s", A, B);
        printf("Case #%d: %d\n", caseNum, gao(B, false) - gao(A, true));
    }
    return 0;
}
