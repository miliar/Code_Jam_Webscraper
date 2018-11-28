#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<string>
#include<vector>
using namespace std;

const int inf = 100000;

int T;
char s[15];
char in[4005];
int f[4005][5];
int n;
vector<string> DIC[26][26];

void init() {
    FILE* dic = fopen("garbled_email_dictionary.txt", "r");
    int cnt = 0;
    while(fscanf(dic, "%s", s) != EOF) {
        if (strlen(s) != 1) {
            DIC[s[0] - 'a'][s[1] - 'a'].push_back(s);
        } else {
            fprintf(stderr, "%s\n", s);
        }
    }
    fprintf(stderr, "init\n");
}

int dp(int now, int can);

pair<string, int> next[4005][5];

void work(vector<string>& v, int& res, const int& now, const int& can) {
    for (int i = v.size() - 1; i >= 0; --i) {
        int l = v[i].length();
        if (now + l > n) continue;
        int tmp = -inf;
        bool flag = false;
        int mis = 0;
        for (int j = 0; j < l; ++j) {
            if (in[now + j] != v[i][j]) {
                if (j - tmp < 5 || j < can) {
                    flag = true;
                    break;
                }
                tmp = j;
                ++mis;
            }
        }
        if (flag) continue;
        res = min(res, dp(now + l, max(0, max(can - l, tmp + 5 - l))) + mis);
    }
}

int dp(int now, int can) {
    if (now == n) return 0;
    int& res = f[now][can];
    if (res == -1) {
        res = inf;
        int a = in[now];
        int b = in[now + 1];
        if (b == 0) {
            res = (a == 'a' || a == 'i') ? 0 : (can == 0 ? 1 : inf);
        } else {
            if (a == 'a' || a == 'i') {
                res = min(res, dp(now + 1, max(0, can - 1)));
            } else {
                if (can == 0) {
                    res = min(res, dp(now + 1, 4) + 1);
                }
            }
            for (int k = 0; k < 26; ++k) {
                work(DIC[k][b - 'a'], res, now, can);
                work(DIC[a - 'a'][k], res, now, can);
            }
        }
    }
    return res;
}

int main() {
    freopen("C-small-attempt3.in", "r", stdin);
    freopen("C-small.out", "w", stdout);
    init();
    scanf("%d", &T);
    for (int test = 1; test <= T; ++test) {
        memset(f, -1, sizeof(f));
        scanf("%s", in);
        n = strlen(in);
        printf("Case #%d: %d\n", test, dp(0, 0));
/*        int aa = 0, bb = 0;
        while(1) {
            printf("%s ", next[aa][bb].first.c_str());
            int tmp = next[aa][bb].first.length() + aa;
            bb = next[aa][bb].second;
            aa = tmp;
        }*/
    }
    return 0;
}

