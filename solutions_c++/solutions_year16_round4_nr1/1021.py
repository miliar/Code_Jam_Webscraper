#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <vector>

const int N = 1e5+3;
const int inf = 1e9;

typedef long long ll;

using namespace std;

bool check(int r, int p, int s, int *ans, int n)
{
    for (int i = 0; i < n; ++i) {
        int x = ans[i];
        if (!x) p--;
        else if (x==1) r--;
        else s--;
    }
    return !r && !p && !s;
}

string SortString(const string &s)
{
    if (s.size() < 3)
        return s;
    
    string ls = SortString(s.substr(0, s.size()/2));
    string rs = SortString(s.substr(s.size()/2, s.size()/2));
    
    return min(ls, rs) + max(ls, rs);
}

int ans[N];
bool solve()
{
    int n,r,p,s;
    scanf("%d%d%d%d", &n,&r,&p,&s);
    
    n = (1<<n);
    
    
    for (int k = 0; k < 3; ++k) {
        ans[1] = k;
        for (int i = 1; i < n; ++i) {
            if (!ans[i]) {
                ans[2*i] = ans[i];
                ans[2*i+1] = 1;
            } else if (ans[i] == 1) {
                ans[2*i] = ans[i];
                ans[2*i+1] = 2;
            } else {
                ans[2*i+1] = ans[i];
                ans[2*i] = 0;
            }
        }
//        for (int j = 1; j < 2*n; ++j) {
//            if (!ans[j]) printf("P");
//            else if (ans[j]==1) printf("R");
//            else printf("S");
//        }
//        puts("");
        if (check(r,p,s,ans+n, n)) {
            string s;
            for (int j = n; j < 2*n; ++j) {
                if (!ans[j]) s+="P";
                else if (ans[j]==1) s+="R";
                else s+="S";
            }
            s = SortString(s);
            puts(s.c_str());
            return 0;
        }
    }
    puts("IMPOSSIBLE");
    return false;
}

int main()
{
        freopen("input.txt","r", stdin);
        freopen("output.txt", "w", stdout);
    int countTests;
    scanf("%d", &countTests);
    for (int curTest = 1; curTest <= countTests; ++curTest) {
        printf("Case #%d: ", curTest);
        solve();
    }
    
    return 0;
}
