#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <map>
#include <sstream>

using namespace std;

const int oo=1001010101;

int mpcnt = 0;
int answer;
int tot = 0;
int st, en, nn;
int a[11111111][3];
int b[18888];
char buff[10101010];
int d[18888], q[18888];
map<string, int> names;
vector<string> lines[222];

void adde(int x, int y, int z)
{
    //cout << x << '-' << y << ' ' << z << endl;
    a[++tot][0] = y; a[tot][1] = z;
    a[tot][2] = b[x]; b[x] = tot;
    a[++tot][0] = x; a[tot][1]=0;
    a[tot][2] = b[y]; b[y]=tot;
}


bool bfs()
{
    int l = 1, r = 1;
    q[1] = st;
    memset(d, 0, sizeof(d));
    d[st] = 1;
    while (l <= r) {
        int x = q[l++];
        for (int i = b[x]; i > 0; i = a[i][2]) {
            int y = a[i][0];
            if (!a[i][1] || d[y])
                continue;
            d[y] = d[x]+1;
            q[++r] = y;
            if (y == en)
                return true;
        }
    }
    return false;
}

int dfs(int x, int flow)
{
    if (x == en) return flow;
    int k = flow;
    for (int i = b[x]; i; i = a[i][2]) {
        int y = a[i][0];
        if (d[y] != d[x] + 1 || !a[i][1])
            continue;
        int t = dfs(y, min(k, a[i][1]));
        k -= t;
        a[i][1] -= t;
        a[i ^ 1][1] += t;
        if (k == 0) break;
    }
    if (k == flow)
        d[x] = -1;
    return(flow - k);
}

int getID(string s) {
    if (names.find(s) == names.end()) 
        names[s] = ++mpcnt;
    return names[s];
}
vector<string> split(char *) {
    istringstream ss(buff);
    vector<string> ret;
    string tmp;
    while (ss >> tmp) ret.push_back(tmp);
    return ret;
}

void readin() {
    names.clear(); mpcnt = 0;
    int n; scanf("%d ", &n);
    for (int i = 0; i < n; ++i) {
        gets(buff);
        lines[i].clear();
        lines[i] = split(buff);
        for (string x : lines[i]) {
            int id = getID(x);
            //cout << x << ' ' << id << endl;
        }
    }
    //building
    nn = mpcnt;
    st = nn * 2 + 1;
    en = st + 1;
    tot = 1;
    memset(a, 0, sizeof a);
    memset(b, 0, sizeof b);
    for (string x : lines[0]) {
        int id = getID(x);
        adde(st, id, oo);
    }
    for (string x : lines[1]) {
        int id = getID(x);
        adde(id + nn, en, oo);
    }
    for (int i = 2; i < n; ++i) {
        for (string x : lines[i]) {
            int idx = getID(x);
            for (string y : lines[i]) {
                int idy = getID(y);
                if (idx != idy) {
                    if (i > 1) adde(idx + nn, idy, oo);
                }
            }
        }
    }
    for (int i = 1; i <= nn; ++i)
        adde(i, i + nn, 1);
    // build fucking graph here
    return;
}

void work() {
    answer = 0;
    //fucking net flow
    while (bfs()) 
        answer += dfs(st, oo);
}

int main() {
    int task; scanf("%d", &task);
    for (int cas = 1; cas <= task; ++cas) {
        readin();
        work();
        printf("Case #%d: ", cas);
        printf("%d\n", answer);
    }
    return 0;
}

