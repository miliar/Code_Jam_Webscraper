#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>

#include <vector>
#include <algorithm>

using namespace std;

typedef std::vector<int> TIntVector;

int main()
{
    freopen("A-large (1).in", "r", stdin);
    freopen("A-large (1).out", "w", stdout);
    
    int nCase;
    scanf("%d", &nCase);
    for (int iCase = 0; iCase < nCase; ++iCase)
    {
        int n;
        int size;
        scanf("%d%d", &n, &size);

        TIntVector sizes(n);
        for (int i = 0; i < n; ++i)
        {
            scanf("%d", &sizes[i]);
        }

        sort(sizes.begin(), sizes.end());

        int result = 0;
        
        if (size > 0)
        {
            int i = 0;
            int j = sizes.size() - 1;
            while (j >= i)
            {
                if (j > i)
                {
                    if (sizes[j] + sizes[i] <= size)
                    {
                        ++result;
                        --j;
                        ++i;
                    }
                    else
                    {
                        ++result;
                        --j;
                    }
                }
                else
                {
                    --j;
                    ++result;
                }
            }
        }

        printf("Case #%d: %d\n", iCase + 1, result);
    }

    return 0;
}