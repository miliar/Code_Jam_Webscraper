#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <bitset>

using namespace std;

#define MP make_pair

int main() {
    freopen("in.txt","r",stdin);
    freopen("out.txt", "w", stdout);
    ios_base::sync_with_stdio(false);

    int n; cin >> n;
    queue<string> q;
    map<string, int> dist;

    string str = "";
    for (int i = 0; i < 10; i++) {
        str += "+";
        q.push(str);
        dist.insert(MP(str, 0));
    }

    while (!q.empty()) {
        str = q.front(); q.pop();
        int strlen = str.length();
        for (int to = 0; to < strlen; to++) {
            string newstr = str;
            for (int from = 0; from <= to; from++) {
                if (newstr[from] == '+') newstr[from] = '-';
                else newstr[from] = '+';
            }
            if (dist.count(newstr) == 1) continue;
            q.push(newstr);
            dist.insert(MP(newstr, dist[str] + 1));
        }
    }

    int casenum = 1;
    while(n--) {
        cin >> str;
        printf("Case #%d: %d\n", casenum++, dist[str]);
    }//end while
    return 0;
} //end main
