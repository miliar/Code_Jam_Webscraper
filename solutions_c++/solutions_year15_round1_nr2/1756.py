#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <utility>

using namespace std;

#define BMAX 1002

typedef struct CUT_INFO
{
    int cut_time;
    int barber_no;
}CUT;

bool cmp (const CUT &a, const CUT &b)
{
    if (a.cut_time == b.cut_time)
    {
        return a.barber_no < b.barber_no;
    }
    else
    {
        return a.cut_time < b.cut_time;
    }
}

int main()
{
    freopen ("B-small-attempt0.in","r",stdin);
    freopen ("B-small-attempt0.out","w",stdout);

    int cas,B,N,M[BMAX],mul[BMAX];
    CUT tmp;
    vector<CUT> cutqueue;

    scanf("%d", &cas);

    for (int c = 1; c <= cas; ++c)
    {
        scanf("%d%d", &B, &N);
        cutqueue.clear();

        for (int i = 0; i < B; ++i)
        {
            scanf("%d", &M[i]);
        }

        for (int i = 0; i < B; ++i)
        {
            mul[i] = 1;
            for (int j = 0; j < B; ++j)
            {
                if (i != j)
                {
                    mul[i] *= M[j];
                }
            }
            for (int j = 0; j < mul[i]; ++j)
            {
                tmp.barber_no = i+1;
                tmp.cut_time = M[i]*j;
                cutqueue.push_back(tmp);
            }
        }

        sort(cutqueue.begin(), cutqueue.end(), cmp);
/*
        for (int i = 0; i < (int)cutqueue.size(); ++i)
        {
            printf("number: %d time:%d\n", cutqueue[i].barber_no, cutqueue[i].cut_time);
        }
*/
        printf("Case #%d: %d\n", c, cutqueue[(N-1)%(int)(cutqueue.size())].barber_no);
    }

    return 0;
}
