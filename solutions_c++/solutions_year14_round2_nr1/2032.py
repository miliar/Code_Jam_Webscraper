#include <vector>
#include <iostream>
#include <climits>
#include <string>
#include <cstdio>
#include <iterator>
#include <algorithm>
using namespace std;

void onecase(void)
{
    int N;
    cin >> N;
    vector<string> strs;
    strs.reserve(N);
    vector<string> seqs;
    for(int j = 0; j < N; ++j)
    {
        string buf;
        cin >> buf;
        strs.push_back(buf);

        string seq(buf);
        seq.erase(unique(seq.begin(), seq.end()), seq.end());
        seqs.push_back(seq);
    }

    for(int j = 1; j < N; ++j)
    {
        if (seqs[j] != seqs[j-1])
        {
            printf("Fegla Won\n");
            return;
        }
    }
    int best = INT_MAX;
    for (int j = 0; j < N; ++j)
    {
        int cost = 0;
        // adjust to match strs[j]
        for (int k = 0; k < N; ++k)
        {
            if (k == j) continue;
            char xprev = '\0';
            char yprev = '\0';
            string::const_iterator x = strs[j].begin(), y = strs[k].begin();
            while( x != strs[j].end() && y != strs[k].end() ) {
                if (*x == *y) {
                    xprev = *x;
                    yprev = *y;
                    ++x;
                    ++y;
                    continue;
                }
                if (*x != xprev) // x changed 1st
                {
                    while (y != strs[k].end() && *y != *x)
                    {
                        ++y;
                        ++cost;
                    }
                    xprev = *x;
                    yprev = *y;
                    continue;
                }

                if (*y != yprev) // y changed first
                {
                    while(x != strs[j].end() && *x != *y) {
                        ++x;
                        ++cost;
                    }
                    xprev = *x;
                    yprev = *y;
                    continue;
                }
            }
            cost += (strs[j].end() - x);
            cost += (strs[k].end() - y);
        }
        if (cost < best)
            best = cost;
    }

    printf("%d\n", best);
}

int main(void)
{
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i)
    {
        printf("Case #%d: ", i);
        onecase();
    }
    return 0;

}
