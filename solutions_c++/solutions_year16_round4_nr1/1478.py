/*
 *
 * Tag: Implementation
 * Time: O(n)
 * Space: O(n)
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <string>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <unordered_map>
#include <unordered_set>
using namespace std;
const int N = 50;
const int M = 30110;
const long long MOD = 1000000007;
const double eps = 1e-10;
int n, p, r, s;
string res;

string dfs(char ch, int tot){
    string res = "";
    if(tot==1){
        res+=ch;
        return res;
    }
    string tmp;
    switch (ch) {
        case 'R':
            tmp = "RS";
            break;
        case 'P':
            tmp = "PR";
            break;
        case 'S':
            tmp = "PS";
        default:
            break;
    }
    int l = tot/2+(tot%2);
    int r = tot-l;
    string ls=dfs(tmp[0],l), rs=dfs(tmp[1],r);
    if(ls>rs)
        swap(ls,rs);
    res = ls + rs;
    return res;
}

bool check(){
    int cntr = r, cntp = p, cnts = s;
    for (int i = 0; i < res.length(); ++ i) {
        if (res[i] == 'R') {
            -- cntr;
        } else if (res[i] == 'P') {
            -- cntp;
        } else {
            -- cnts;
        }
    }
    return !cntr&&!cntp&&!cnts;
}


int main() {
    freopen("/Users/ybc/Project/CCPP/ACM/A-small-attempt0.in.txt", "r", stdin);
    freopen("/Users/ybc/Project/CCPP/ACM/out.txt", "w", stdout);
    int T;
    scanf("%d",&T);
    for (int cas = 1; cas <= T; ++ cas) {
        printf("Case #%d: ",cas);
        scanf("%d%d%d%d",&n,&r,&p,&s);
        string ans = "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ";
        res = dfs('R', (1<<n));
    //    cout<<res<<endl;
        if (check()) {
            ans = min(ans, res);
        }
        res = dfs('P', (1<<n));
     //   cout<<res<<endl;
        if (check()) {
            ans = min(ans, res);
        }
        res = dfs('S', (1<<n));
     //   cout<<res<<endl;
        if (check()) {
            ans = min(ans, res);
        }
        if (ans == "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ") {
            puts("IMPOSSIBLE");
        } else {
            cout<<ans<<endl;
        }
    }
    return 0;
}
