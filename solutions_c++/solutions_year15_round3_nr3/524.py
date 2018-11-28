#include <bits/stdc++.h>
using namespace std;

const int SIZE = 10;
const int N = 40;
vector<int> elem;

vector<vector<int>> comb[N][N];

int mark[N];
bool check(int v, vector<int>& elems, bool fl = false) {
    fill(mark, mark + v + 1, 0);

    set<int> sums;
    sums.insert(0);
    for (int i = 0; i < elems.size(); i++) {
        vector<int> add;
        for (auto it : sums) {
            if (it + elems[i] > v)
                continue;

            if (fl)
                cerr << it << " " <<  elems[i] << "\n";
            mark[it + elems[i]] = true;
            add.push_back(it + elems[i]);
        }

        for (auto it : add)
            sums.insert(it);
    }

    bool res = true;
    for (int i = 1; i <= v; i++) {
        res &= mark[i];
        if (fl)
            cerr << mark[i] << " ";
    }

    if (fl)
        cerr << "\n";

    return res;
}

bool check2(vector<int> a, vector<int> b) {
    set<int> s(a.begin(), a.end());
    for (auto it : b) {
        if (s.find(it) != s.end())
            return false;
    }

    return true;
}

void print_vector(vector<int>& a) {
    for (auto it : a)
        cerr << it << " ";
    cerr << "\n";
}

void solve() {
    int c, d, v;
    scanf("%d %d %d", &c, &d, &v);
    for (int i = 0; i < d; i++) {
        int t;
        scanf("%d", &t);
        elem.push_back(t);
    }

    int ans = v;

    if (check(v, elem))
        ans = 0;

    for (int p = 1; ans != 0 && p <= 7; p++) {
        for (auto& it : comb[v][p]) {
            if (!check2(elem, it))
                continue;

            vector<int> elems(elem.begin(), elem.end());
            for (auto& it2 : it)
                elems.push_back(it2);
            sort(elems.begin(), elems.end());


            if (check(v, elems)) {
                ans = min(ans, p);
                p = 10;
                break;
            }
        }
    }

    elem.clear();
    printf("%d\n", ans); 
}

int Stack[N], size;
void gen(int i, int n, int k) {
    if (k == 0) {
        vector<int> tmp;
        for (int j = 0; j < size; j++)
            tmp.push_back(Stack[j]);
        comb[n][size].push_back(tmp);
        return;
    }

    for (int j = i; j <= n; j++) {
        Stack[size++] = j;
        gen(j + 1, n, k - 1);
        size--;
    }
}

int main() {

    for (int i = 1; i <= 30; i++) {
        for (int j = 1; j <= i && j <= 7; j++) {
            gen(1, i, j);
        }
    }

    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        printf("Case #%d: ", i + 1);
        solve();
    }
}
