#include <cstdio>
#include <vector>
#include <algorithm>
#include <functional>
#include <map>
#include <set>

using namespace std;

map<vector<int>, int> mem;

int go(int n, vector <int> cakes)
{
    if (mem.find(cakes) != mem.end())
        return mem[cakes];
    
    while (cakes.size() && cakes.back() == 0)
    {
        cakes.pop_back();
    }
    if (n == 0)
    {
        mem[cakes] = 0;
        return 0;
    }
    if (n == 1)
    {
        mem[cakes] = 1;
        return 1;
    }
    else
    {
        vector <int> changed;
        for (int i = 0; i < cakes.size(); ++i)
        {
            --cakes[i];
            --n;
            changed.push_back(i);
        }
        int answer = go(n, cakes);
        for (int i = 0; i < changed.size(); ++i)
        {
            ++cakes[changed[i]];
            ++n;
        }
        for (int i = 0; i < cakes.size(); ++i)
        {
            for (int j = 1; j < cakes[i]; ++j)
            {
                vector <int> c2 = cakes;   
                c2.push_back(j);           
                c2[i] = (c2[i] - j);
                sort(c2.begin(), c2.end(), greater<int>());
                while (c2.size() && c2.back() == 0)
                {
                    c2.pop_back();
                }
                answer = min(answer, go(n, c2));
            }
        }
        mem[cakes] = answer + 1;
        return answer + 1;
    }
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int z = 1; z <= T; ++z)
    {
        printf("Case #%d: ", z);
        int d;
        multiset<int, greater<int> > q;
        vector <int> c;
        scanf("%d", &d);
        int maximum = 0;
        int secondMax = 0;
        for (int i = 0; i < d; ++i)
        {
            int m;
            scanf("%d", &m);
            maximum += m;
            c.push_back(m);
            q.insert(m);
            
        }
        sort(c.begin(), c.end(), greater<int>());
        printf("%d\n", go(maximum, c));
//         int answer = *q.begin();
//         int steps = 0;
//         while (*q.begin() > 1)
//         {
//             ++steps;
//             int x = *q.begin();
//             q.erase(q.begin());
//             q.insert(x / 2);
//             q.insert((x + 1) / 2);
//             answer = min(answer, steps + *q.begin());
//         }
//         printf("%d\n", answer);
    }
    return 0;
}