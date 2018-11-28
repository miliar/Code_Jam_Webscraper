#include <bits/stdc++.h>
#include <fcntl.h>
#include <unistd.h>

using namespace std;

/*** START OF TEMPLATE CODE ***/

typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;
typedef complex<double> pnt;
typedef pair<int, int> pii;

#define RA(x) begin(x), end(x)
#define FE(i, x) for (auto i = begin(x); i != end(x); ++i)
#define SZ(x) ((int) (x).size())

template<class T>
vector<T> splitstr(const string &s)
{
    istringstream in(s);
    vector<T> out;
    copy(istream_iterator<T>(in), istream_iterator<T>(), back_inserter(out));
    return out;
}

template<class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }

static void redirect(int argc, const char **argv)
{
    if (argc > 1)
    {
        int fd = open(argv[1], O_RDONLY);
        if (fd == -1) { perror(argv[1]); exit(1); }
        if (-1 == dup2(fd, 0)) { perror(argv[1]); exit(1); }
        if (-1 == close(fd)) { perror(argv[1]); exit(1); }
    }

    if (argc > 2)
    {
        int fd = open(argv[2], O_WRONLY | O_CREAT, 0666);
        if (fd == -1) { perror(argv[2]); exit(1); }
        if (-1 == dup2(fd, 1)) { perror(argv[2]); exit(1); }
        if (-1 == close(fd)) { perror(argv[2]); exit(1); }
    }

    ios::sync_with_stdio(false);
    cin.exceptions(ios::failbit | ios::badbit);
}

/*** END OF TEMPLATE CODE ***/

struct monster
{
    int h;
    int g;
    int prep = 0;
    int t[2];
};

static int divup(int a, int b)
{
    return (a + b - 1) / b;
}

int main(int argc, const char **argv)
{
    redirect(argc, argv);

    int cases;
    cin >> cases;
    for (int cas = 0; cas < cases; cas++)
    {
        int P, Q, N;
        cin >> P >> Q >> N;
        vector<monster> m(N);
        for (int i = 0; i < N; i++)
        {
            cin >> m[i].h >> m[i].g;
            if (P < Q)
            {
                int rem = m[i].h;
                while ((rem >= Q && rem % Q == 0) || rem % Q > P)
                {
                    rem -= P;
                    m[i].prep++;
                }
            }
            m[i].t[0] = divup(m[i].h, Q);
            m[i].t[1] = max(0, (m[i].h - m[i].prep * P - 1) / Q);
            assert(m[i].t[0] > 0);
            assert(m[i].t[1] * Q + m[i].prep * P + P >= m[i].h);
        }

        constexpr int H = 150;
        int dp[H + 1][2];
        memset(dp, 0, sizeof(dp));
        for (int i = N - 1; i >= 0; i--)
        {
            int dp2[H + 1][2];
            memset(dp2, 0, sizeof(dp2));
            const auto &x = m[i];
            int u = divup(x.h, P);
            for (int s = 0; s <= H; s++)
                for (int t = 0; t < 2; t++)
                {
                    // Let tower take it
                    dp2[s][t] = max(dp2[s][t], dp[min(s + x.t[0] - t, H)][0]);
                    // Kill it with help from the tower
                    if (x.t[1] >= t)
                    {
                        int s2 = min(s + x.t[1] - t - x.prep, H);
                        if (s2 >= 0)
                            dp2[s][t] = max(dp2[s][t], dp[s2][1] + x.g);
                    }
                    // Kill it early
                    if (u <= s)
                        dp2[s][t] = max(dp2[s][t], dp[s - u][t] + x.g);
                }
            memcpy(dp, dp2, sizeof(dp));
        }
        cout << "Case #" << cas + 1 << ": " << dp[0][0] << "\n";
    }
    return 0;
}
