#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>

#include <string>
#include <set>
#include <vector>

using namespace std;

typedef vector<string> TStringVector;
typedef vector<int> TIntVector;
typedef set<string> TStringSet;

typedef vector<TStringSet> TDistribution;

void Simulate(const TStringVector& strings, int n, int index, const TDistribution& distribution, int* max, int* ways)
{
    if (index == strings.size())
    {
        int size = 0;
        for (int i = 0; i < n; ++i)
        {
            size += distribution[i].size();
        }
        if (size > *max)
        {
            *ways = 1;
            *max = size;
        } 
        else if (size == *max)
        {
            ++(*ways);
        }
    }
    else
    {
        for (int i = 0; i < n; ++i)
        {
            TDistribution updatedDistribution = distribution;
            for (size_t j = 0; j <= strings[index].size(); ++j)
            {
                updatedDistribution[i].insert( strings[index].substr(0, j) );
            }
            Simulate(strings, n, index + 1, updatedDistribution, max, ways);
        }
    }
}

int main()
{
    freopen("D-small-attempt0 (1).in", "r", stdin);
    freopen("D-small-attempt0 (1).out", "w", stdout);
    
    int nTests;
    scanf("%d", &nTests);
    for (int iTest = 0; iTest < nTests; ++iTest)
    {
        int m;
        int n;
        scanf("%d%d", &m, &n);
        
        TStringVector strings(m);
        for (int i = 0; i < m; ++i)
        {
            char buffer[1000];
            scanf("%s", buffer);
            strings[i] = buffer;
        }

        int max = -1;
        int ways = 0;
        TDistribution distribution(n);
        Simulate(strings, n, 0, distribution, &max, &ways);
        printf("Case #%d: %d %d\n", iTest + 1, max, ways);
    }

    return 0;
}