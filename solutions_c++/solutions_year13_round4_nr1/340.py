#include <cstdio>
#include <map>
#include <stack>
using namespace std;
const int mod = 1000002013;
long long calc(long long len, long long num)
{
    return (((long long) len * num - (long long) len * (len - 1) / 2) % mod + mod) % mod;
}
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int cas = 1; cas <= t; ++ cas)
    {
        int n, m;
        scanf("%d%d", &n, &m);
        long long now = 0;
        map <long long, long long> peo;
        for (int i = 0; i < m; ++ i)
        {
            long long o, e, p;
            scanf("%I64d%I64d%I64d", &o, &e, &p);
            now += p * ((long long) (e - o) * n % mod - (long long) (e - o) * (e - o - 1) / 2 % mod + mod) % mod;
            now %= mod;
            peo[o] += p;
            peo[e] -= p;
        }
        long long mins = 0;
        stack <pair <long long, long long> > st;
        for (map <long long, long long> :: iterator it = peo.begin(); it != peo.end(); ++ it)
        {
            if (it -> second > 0)
                st.push(*it);//make_pair(it -> first, it -> second));
            else if (it -> second < 0)
            {
                long long pos = st.top().first;
                long long num = st.top().second;
                while (num < - it -> second)
                {
                    mins += calc(it -> first - pos, n) * num % mod;
                    mins %= mod;
                    it -> second += num;
                    st.pop();
                    pos = st.top().first;
                    num = st.top().second;
                }
                mins += calc(it -> first - pos, n) * ((- it -> second) % mod) % mod;
                mins %= mod;
                st.top().second += it -> second;
            }
        }
        printf("Case #%d: %I64d\n", cas, (now - mins + mod) % mod);

    }
    return 0;
}

