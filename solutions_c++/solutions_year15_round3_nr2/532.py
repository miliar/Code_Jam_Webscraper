#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

vector<string> words;
const int N = 10;

char Stack[N];
int size;
void gen(string& al, int s) {
    if (size == s) {
        string ex(Stack, size);
        words.push_back(ex);
        return;
    }

    for (int i = 0; i < al.size(); i++) {
        Stack[size++] = al[i];
        gen(al, s);
        size--;
    }
}

void solve() {
    int k, l, s;
    scanf("%d %d %d\n", &k, &l, &s);

    string alpha, tar;
    cin >> alpha >> tar;

    gen(alpha, s);

    ll all, sum = 0;

    vector<int> need;
    int max_need = 0;

    need.reserve(100000);

    for (auto& it: words) {
        int cur_sum = 0;
        for (int j = 0; j + l - 1 < it.size(); j++) {
            bool flag = true;
            for (int shift = 0; flag && shift < l; shift++) {
                if (it[j + shift] != tar[shift])
                    flag = false;
            }

            cur_sum += flag;
        }

        need.push_back(cur_sum);
        max_need = max(max_need, cur_sum);
    }

    for (int i = 0; i < need.size(); i++) {
        int residue = max_need - need[i];
        sum += residue;
    }

    all = 1;
    for (int i = 0; i < s; i++)
        all *= k;

    printf("%.8lf\n", (sum + .0) / all);
    words.clear();
}

int main() {

    words.reserve(10000000);

    int t;
    scanf("%d", &t);

    for (int i = 0; i < t; i++) {
        printf("Case #%d: ", i + 1);
        solve();
    }
}
