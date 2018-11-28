#include <cstdio>
#include <vector>
using std::vector;
#include <algorithm>

bool cmp(const int& a, const int& b)
{
    return a > b;
}
int main()
{
    int T;
    scanf("%d", &T);
    for(int t = 1;t <= T;++t)
    {
        vector<int> sizes;
        int n, disc;
        scanf("%d%d", &n, &disc);
        for(int i = 0;i < n;++i)
        {
            int file;
            scanf("%d", &file);
            sizes.push_back(file);
        }
        int cost = 0;
        std::sort(sizes.begin(), sizes.end(), cmp);
        for(int i = 0;i < sizes.size();++i)
        {
            if(sizes[i] + sizes.back() <= disc)
            {
                sizes.pop_back();
            }
            ++cost;
        }
        printf("Case #%d: %d\n", t, cost);
    }
}
