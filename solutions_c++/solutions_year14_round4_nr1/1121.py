#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <set>

using namespace std;

int N,M;
multiset<int, greater<int> > truc;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T;
    scanf("%d", &T);

    for(int t = 1; t <= T; t++)
    {
        scanf("%d%d", &N, &M);

        for(int i = 0; i < N; i++)
        {
            int val;
            scanf("%d", &val);
            truc.insert(val);
        }

        int tt = 0;
        while(!truc.empty())
        {
            multiset<int>::iterator itr = truc.begin();
            int val = *itr;
            truc.erase(itr);
            multiset<int>::iterator bidule = truc.lower_bound(M-val);
            if(bidule!=truc.end())
                truc.erase(bidule);
            tt++;
        }

        printf("Case #%d: %d\n",t, tt);
    }

    return 0;
}
