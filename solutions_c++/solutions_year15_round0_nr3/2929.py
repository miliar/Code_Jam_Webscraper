#include <bits/stdc++.h>
using namespace std;

char q[128][128];
char s[10000];
int l, x;

void init()
{
    q['i']['i'] = q['j']['j'] = q['k']['k'] = q['I']['I'] = q['J']['J'] = q['K']['K'] = q['1']['n'] = q['n']['1'] = 'n';

    q['i']['I'] = q['I']['i'] = q['j']['J'] = q['J']['j'] = q['k']['K'] = q['K']['k'] = q['1']['1'] = q['n']['n'] = '1';

    q['i']['1'] = q['1']['i'] = q['I']['n'] = q['n']['I'] = 'i';
    q['i']['n'] = q['n']['i'] = q['I']['1'] = q['1']['I'] = 'I';

    q['j']['1'] = q['1']['j'] = q['J']['n'] = q['n']['J'] = 'j';
    q['j']['n'] = q['n']['j'] = q['J']['1'] = q['1']['J'] = 'J';

    q['k']['1'] = q['1']['k'] = q['K']['n'] = q['n']['K'] = 'k';
    q['k']['n'] = q['n']['k'] = q['K']['1'] = q['1']['K'] = 'K';

    q['i']['j'] = q['I']['J'] = q['j']['I'] = q['J']['i'] = 'k';
    q['i']['J'] = q['I']['j'] = q['j']['i'] = q['J']['I'] = 'K';

    q['j']['k'] = q['J']['K'] = q['k']['J'] = q['K']['j'] = 'i';
    q['j']['K'] = q['J']['k'] = q['k']['j'] = q['K']['J'] = 'I';

    q['k']['i'] = q['K']['I'] = q['i']['K'] = q['I']['k'] = 'j';
    q['k']['I'] = q['K']['i'] = q['i']['k'] = q['I']['K'] = 'J';
}

bool tc()
{
    int n = l * x;
    unordered_set<int> p2;
    char c = '1';
    for (int i = n - 1; i >= 2; i--)
        if ((c = q[s[i % l]][c]) == 'k')
            p2.insert(i);
    c = '1';
    for (int i = 0; i < n - 2; i++)
        if ((c = q[c][s[i % l]]) == 'i') {
            char c2 = '1';
            for (int j = i + 1; j < n - 1; j++)
                if ((c2 = q[c2][s[j % l]]) == 'j' &&
                    p2.find(j + 1) != p2.end())
                    return true;
        }
    return false;
}

int main()
{
    init();
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++) {
        scanf("%d %d %s", &l, &x, s);
        printf("Case #%d: %s\n", i, (tc() ? "YES" : "NO"));
    }
}
