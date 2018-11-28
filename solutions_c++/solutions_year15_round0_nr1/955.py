#include <iostream>
#include <cstdio>
#define f cin
#define g cout

using namespace std;

int N;
string S;

int main ()
{
    /*
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    /* */

    int T;
    f >> T;

    for (int t=1; t<=T; t++)
    {
        g << "Case #" << t << ": ";


        f >> N;
        f >> S;

        int cnt = 0;
        int ans = 0;

        for (int i=0; i<S.size(); i++)
            if (S[i] != '0')
            {
                if (cnt < i)
                {
                    ans += i - cnt;
                    cnt = i;
                }
                cnt += S[i] - '0';
            }

        g << ans << '\n';
    }

    return 0;
}
