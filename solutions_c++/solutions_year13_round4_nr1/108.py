#include <stdio.h>
#include <map>
#include <vector>
using namespace std;
long long calc(long long n, long long diff) {
    return (n + n - diff+1) * (diff) / 2;
}
int Min(int a, int b) {
    return a<b?a:b;
}
int main() {
    int casN, m;
    scanf("%d", &casN);
    int n, o, e, p;
    long long ans;
    map<int, int> val;
    vector<int> sta;
    for (int casI = 0; casI < casN; casI++) {
        scanf("%d%d", &n, &m);
        ans = 0;
        val.clear();
        sta.clear();
        for (int i=0; i<m; i++) {
            scanf("%d%d%d", &o, &e, &p);
            ans += calc(n, e-o) * p;
            val[o] += p;
            val[e] -= p;
        }
        for (map<int, int>::iterator itr = val.begin(); itr != val.end(); ++itr)
        {
            if (itr->second > 0) {
                sta.push_back(itr->first);
            } else if (itr->second < 0) {
                while (itr->second < 0) {
                    int d = Min(-itr->second, val[sta[sta.size()-1]]);
                    itr->second += d;
                    val[sta[sta.size()-1]] -= d;
                    ans -= calc(n, itr->first - sta[sta.size()-1]) * d;
                    if (val[sta[sta.size()-1]] == 0) sta.pop_back();
                }
            }
        }
        printf("Case #%d: %lld\n", casI+1, ans);
    }
    return 0;
}
