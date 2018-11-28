#include <iostream>
#include <vector>
#include <cstring>
#include <cstdio>
#include <map>
#include <deque>
#include <set>
#include <algorithm>
#include <numeric>
#include <functional>
#include <unordered_map>
#include <thread>

using namespace std;

#define ll long long

string S;
int mem[20000][20000];

int best(int s, int e) {
    int &ans = mem[s][e];
    if (ans != -1) return ans;

    if (s >= e) return ans = 0;

    ans = best(s+1, e-1) + (S[s] == S[e] ? 10 : 5);

    for (int i = s+1; i<e; i+=2) {
        int cur = best(s, i) + best(i+1, e);
        ans = max(ans, cur);
    }

    return ans;
}

int main() {
    int T;
    cin>>T;
    for (int t=1;t<=T;++t) {
        cin>>S;

        memset(mem,-1,sizeof(mem));
        int ans = best(0, S.size() - 1);

        printf("Case #%d: %d\n", t, ans);
    }
}
