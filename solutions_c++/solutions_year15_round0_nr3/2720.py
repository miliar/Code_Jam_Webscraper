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

#define MAXL 10002

pair<int, char> Dijkstra(char a, char b)
{
    if (a == '1' && b == '1')   return make_pair(1, '1');
    if (a == '1' && b == 'i')   return make_pair(1, 'i');
    if (a == '1' && b == 'j')   return make_pair(1, 'j');
    if (a == '1' && b == 'k')   return make_pair(1, 'k');

    if (a == 'i' && b == '1')   return make_pair(1, 'i');
    if (a == 'i' && b == 'i')   return make_pair(0, '1');
    if (a == 'i' && b == 'j')   return make_pair(1, 'k');
    if (a == 'i' && b == 'k')   return make_pair(0, 'j');

    if (a == 'j' && b == '1')   return make_pair(1, 'j');
    if (a == 'j' && b == 'i')   return make_pair(0, 'k');
    if (a == 'j' && b == 'j')   return make_pair(0, '1');
    if (a == 'j' && b == 'k')   return make_pair(1, 'i');

    if (a == 'k' && b == '1')   return make_pair(1, 'k');
    if (a == 'k' && b == 'i')   return make_pair(1, 'j');
    if (a == 'k' && b == 'j')   return make_pair(0, 'i');
    if (a == 'k' && b == 'k')   return make_pair(0, '1');

    return make_pair(-1, -1);
}

/*int FindX(int L, long long int X)
{
    int findval = 1;
    for (int i = 2; i <= X && L*i <= MAXL; ++i)
    {
        if (X % i == 0 && X / i % 2 == 0)
        {
            findval = i;
        }
    }

    return findval;
}*/

int main()
{
    freopen ("C-small-attempt2.in","r",stdin);
    freopen ("C-small-attempt2.out","w",stdout);

    long long int X;
    int cas, L, X_times, firstI_index, firstK_index, copy_times;
    bool firstI, firstK;
    char str[MAXL];
    pair<int, char> ans, retval;

    scanf("%d", &cas);

    for (int c = 1; c <= cas; ++c)
    {
        scanf("%d%lld%s", &L, &X, str);

        //X_times = FindX(L, X);

        //for (copy_times = 1; copy_times < X_times && L <= MAXL; ++copy_times)
        for (copy_times = 1; copy_times < X; ++copy_times)
        {
            strncat(str, str, L);
        }
        L += ((copy_times-1)*L);
        //printf("%d%s\n", L, str);

        ans = make_pair(1, str[0]);
        firstI_index = L;
        firstI = false;
        if (str[0] == 'i')
        {
            firstI_index = 0;
            firstI = true;
        }

        for (int i = 1; i < L; ++i)
        {
            retval = Dijkstra(ans.second, str[i]);
            ans.second = retval.second;
            ans.first = !(ans.first ^ retval.first);
            //printf("%d %c\n", ans.first, ans.second);
            if (ans.first == 1 && ans.second == 'i' && !firstI)
            {
                firstI_index = i;
                firstI = true;
            }
        }

        ans = make_pair(1, str[L-1]);
        firstK_index = -1;
        firstK = false;
        if (str[L-1] == 'k')
        {
            firstK_index = L-1;
            firstK = true;
        }

        for (int i = L-2; i >= 0; --i)
        {
            retval = Dijkstra(str[i], ans.second);
            ans.second = retval.second;
            ans.first = !(ans.first ^ retval.first);
            if (ans.first == 1 && ans.second == 'k' && !firstK)
            {
                firstK_index = i;
                firstK = true;
            }
        }

        //printf("%d %c %d %d\n", ans.first, ans.second, firstI_index, firstK_index);
        if (ans.first == 0 && ans.second == '1' && firstK_index > firstI_index+1)
        {
            printf("Case #%d: YES\n", c);
        }
        else
        {
            printf("Case #%d: NO\n", c);
        }
    }

    return 0;
}
