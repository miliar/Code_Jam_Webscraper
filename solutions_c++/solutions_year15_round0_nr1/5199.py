#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <queue>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <stack>
#include <cstring>
#include <iomanip>
#include <cctype>
#include <map>

using namespace std;

void solve(int t) {
    int n; cin>>n;
    vector<int> cnt(n + 1);
    string s; cin>>s;
    for(int i = 0;i <= n;i++) {
        cnt[i] = s[i] - '0';
    }
    int ans = 0;
    int cc = 0;
    for(int i = 0;i <= n;i++) {
        if(cc < i) {
            ans+=(i - cc);
            cc+=(i - cc);
        }
        cc+=cnt[i];
    }
    printf("Case #%d: %d\n",t,ans);
}

int main() {
    freopen("/Users/administrator/Desktop/A-large.in","r",stdin);
    freopen("/Users/administrator/Desktop/gcjoutput.txt","w",stdout);
    int t; cin>>t;
    for(int i = 1;i <= t;i++) {
        solve(i);
    }

}