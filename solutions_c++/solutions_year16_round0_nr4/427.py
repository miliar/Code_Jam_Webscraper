// vim:set sw=4 et smarttab:
// Qualification Round 2016

#include <cstdio>
#include <vector>

int k, c, s;

void solve(std::vector<long long> &answer)
{
    if (c * s < k)
        return;
    for (int i = 0; i < k; i += c)
    {
        long long v = 0;
        for (int j = i; j < k && j < i + c; ++j)
        {
            v *= k;
            v += j;
        }
        answer.push_back(v + 1);
    }
}

int main()
{
    int ntc;
    scanf("%d", &ntc);
    for (int tc = 1; tc <= ntc; ++tc)
    {
        scanf("%d%d%d", &k, &c, &s);
        std::vector<long long> answer;
        solve(answer);
        printf("Case #%d:", tc);
        if (answer.empty())
            printf(" IMPOSSIBLE");
        else
            for (auto i : answer)
                printf(" %lld", i);
        printf("\n");
    }
}
