#include <iostream>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <queue>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>
#include <bitset>

using namespace std;

#define fr first
#define sc second
#define mp make_pair
#define pb push_back
#define epr(...) fprintf(stderr, __VA_ARGS__)
#define db(x) cerr << #x << " = " << x << endl
#define db2(x, y) cerr << "(" << #x << ", " << #y << ") = (" << x << ", " << y << ")\n"; 
#define db3(x, y, z) cerr << "(" << #x << ", " << #y << ", " << #z << ") = (" << x << ", " << y << ", " << z << ")\n"
#define all(a) (a).begin(), (a).end()

#define equal equalll
#define less lesss
const int N = 33;
const long long INF = 1e9 + 19;

struct rect {
    int a, b, cnt;
    rect(int a, int b, int cnt): a(a), b(b), cnt(cnt) { }
};

int n;
int a[N][N];
char s[N][N];
bool use[N];
bool useM[N];

void read() {
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
        scanf("%s", s[i]);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            a[i][j] = s[i][j] - '0';
}
vector < int > aa;
vector < int > bb;

void dfs(int v) {
    use[v] = 1; 
    aa.pb(v);
    //db2("add A: ", v);
    for (int i = 0; i < n; i++)
        if (a[v][i] == 1 && useM[i] == 0) {
            useM[i] = 1;
            bb.pb(i);
            //db2("add B: ", i);
            for (int j = 0; j < n; j++)
                if (a[j][i] == 1 && !use[j])
                    dfs(j);
        }

}

vector < rect > d;
map < vector < int >, int > q;
int g[N];


int rec(vector < int > st);

void rec2(const vector < int > & data, int pos, int sx, int sy, int & answer) {
    if (pos == (int)data.size()) {
        if (sx == sy && sx > 0) {
            vector < int > tmp(data.size());
            for (int i = 0; i < (int)data.size(); i++) {
                tmp[i] = data[i] - g[i];
                assert(tmp[i] >= 0);
            }
            answer = min(answer, rec(tmp) + sx * sx);
        }
        return;
    }
    for (int i = 0; i <= data[pos]; i++) {
        g[pos] = i;
        rec2(data, pos + 1, sx + i * d[pos].a, sy + i * d[pos].b, answer);
    }
}


int rec(vector < int > st) {
    bool flag = 1;
    for (auto x: st)
        flag &= x == 0;
    if (flag)
        return 0;
        
    if (q.count(st) == 0) {
        int answer = INF;
        rec2(st, 0, 0, 0, answer);
        q[st] = answer;
    } 
    return q[st];
}

int solve() {
    memset(use, 0, sizeof(use));
    memset(useM, 0, sizeof(useM)); 
    vector < pair < int, int > > c;
    q.clear();
    d.clear();
    int answer = 0;
    //cerr << endl;
    //for (int i = 0; i < n; i++, cerr << endl)
        //for (int j = 0; j < n; j++)
            //cerr << a[i][j] << " ";
    for (int i = 0; i < n; i++)
        if (!use[i]) {
            aa.clear();
            bb.clear();
            dfs(i);
            for (auto x: aa)
                for (auto y: bb)
                    if (a[x][y])
                        answer--;
            //db2(aa.size(), bb.size());
            if (aa.size() != bb.size())
                c.pb(mp(aa.size(), bb.size()));
            else
                answer += aa.size() * aa.size();
        }
    for (int i = 0; i < n; i++) {
        bool flag = 1;
        for (int j = 0; j < n; j++)
            flag &= a[j][i] == 0;
        if (flag)
            c.pb(mp(0, 1));
    }

    sort(c.begin(), c.end());     
    for (int i = 0; i < (int)c.size(); ) {
        int j = i;
        for (; i < (int)c.size() && c[i] == c[j]; i++);
        d.pb(rect(c[j].fr, c[j].sc, i - j));
    }
    //db(answer);
    //db(d.size());
    //for (auto x: d)
        //db3(x.a, x.b, x.cnt);

    vector < int > st;
    for (auto x: d)
        st.pb(x.cnt);
    answer += rec(st);

    return answer;
}

void stress() {

}


int stupid() {
    int answer = INF;
    vector < vector < int > > c(n, vector < int > (n, 0));
    for (int mask = 0; mask < (1 << (n * n)); mask++) {
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) {
                c[i][j] = ((mask >> (i * n + j)) & 1);
            }
        bool flag = 1;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                flag &= c[i][j] >= a[i][j];

        if (!flag)continue;

        for (int i = 0; i < n; i++) {
            vector < int > pos;
            for (int j = 0; j < n; j++)
                if (c[i][j])
                    pos.pb(j);
            for (auto y: pos){
                int cc = 0;
                for (int j = 0; j < n; j++) {
                    if (c[j][y]) {
                        cc++;
                        for (int k = 0; k < n; k++)
                            flag &= c[j][k] == c[i][k];
                    }
                }
                flag &= cc == (int)pos.size();
            }
        }
        for (int i = 0; i < n; i++) {
            bool ff = 0;
            for (int j = 0; j < n; j++)
                ff |= c[i][j];
            flag &= ff;
        }

        if (!flag)continue;

        int r = __builtin_popcount(mask);
        if (r < answer) {
            answer = r;
            //cerr << "res: " << answer << endl;
            //for (int i = 0; i < n; i++, cerr << endl)
                //for (int j = 0; j < n; j++)
                    //cerr << c[i][j] << " ";
        }
    }
    int sum = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            sum += a[i][j];

    return answer - sum;
}


int main(){
#ifdef MY_DEBUG
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
#endif
    if (1) {
        int k = 1;
        scanf("%d", &k);
        for (int tt = 0; tt < k; tt++) {
            //db(tt);
            printf("Case #%d: ", tt + 1);
            read();
            int r1 = solve();
            cout << r1 << endl;
            //int r2 = stupid();
            //db2(r1, r2);
            //assert(r1 == r2);
        }
    }
    else {
        stress();
    }

    return 0;
}

