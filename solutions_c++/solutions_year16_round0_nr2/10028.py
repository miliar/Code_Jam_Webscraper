#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#include <map>

#define loop(i, n) for(int i = 0; i < n; i++)
#define FOR(i, x, n) for(int i = x; i <= n; i++)
#define mem(x, y) memset(x, y, sizeof(x))

using namespace std;

map<string, int> mp;

struct node {

    string s; int c;
    node() {}

    node(string ss, int cc) {
        s = ss; c = cc;
    }
};

string changeState(string str, int x) {

    string tmp = str;

    int p = 0;
    int len = str.length();

    for(int i = x; i >= 0; i--) {
        tmp[p++] = (str[i] == '+') ? '-' : '+';
    }

    for(int i = p; i < len; i++) {
        tmp[i] = str[i];
    }

    return tmp;
}

int countHappy(string ss) {

    int len = ss.length();
    int cnt = 0;

    for(int i = 0; i < len; i++) {
        if(ss[i] == '+') cnt++;
    }

    return cnt;
}


int bfs(string ss) {

    queue<node> q;

    int len = ss.length();
    node nod = node(ss, 0), u;

    q.push(nod); mp[ss] = 1;

    while(!q.empty()) {

        u = q.front(); q.pop();

        if(countHappy(u.s) == len) {
            break;
        }

        for(int i = 0; i < len; i++) {
            string sn = changeState(u.s, i);
            if(!mp[sn]) {
                q.push(node(sn, u.c+1));
                mp[sn] = 1;
            }
        }
    }

    return u.c;
}

int main() {

    //freopen("/home/redwan/inn.in", "r", stdin);
    //freopen("/home/redwan/inn.out", "w", stdout);

    int t, cntt = 0; scanf("%d", &t);

    while(true) {
        mp.clear();
        string str; cin >> str;
        int res = bfs(str);

        printf("Case #%d: %d\n", ++cntt, res);

        if(cntt == t) break;
    }

    return 0;
}
