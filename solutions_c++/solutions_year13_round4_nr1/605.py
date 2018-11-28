#include <cstdio>
#include <map>
#include <vector>
#include <algorithm>
#include <cmath>

#define MAX 10005
#define MOD 1000002013
using namespace std;

int counter[MAX];
int n;

long long dis(int a, int b)
{
    int k = abs(a - b);
    return (1LL * k * (n + n+1 - k) / 2)%MOD;
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int Ti = 0; Ti < T; ++Ti)
    {
        map<int, int> in, out;
        vector<int> ary;

        int m;
        scanf("%d %d", &n, &m);
        long long ans = 0;
        for(int i = 0; i < m; ++i)
        {
            int a, b, p;
            scanf("%d %d %d", &a, &b, &p);

            in[a] += p;
            out[b] += p;

            ary.push_back(a);
            ary.push_back(b);

            //ans += dis(a, b)*p;
            ans = (ans + dis(a, b) * p)%MOD;
        }

        sort(ary.begin(), ary.end());
        int N = unique(ary.begin(), ary.end()) - ary.begin();

        for (int i = 0; i < N; ++i)
        {
            int idx = ary[i];

            counter[i] = in[idx];

            int o = out[idx];
            for (int j = i; j >= 0 && o > 0; --j)
            {
                int ct = min(o, counter[j]);
                
                ans = (ans - (dis(ary[i], ary[j]) * ct)%MOD + MOD)%MOD;
                counter[j] -= ct;
                o -= ct;
            }
        }
        printf("Case #%d: %lld\n", Ti+1, ans);
    }
}
