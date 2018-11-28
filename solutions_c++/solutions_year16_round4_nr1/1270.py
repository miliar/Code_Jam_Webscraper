#include <cstdio>
#include <vector>

using namespace std;
char ans[1 << 13], tmp[1 << 13];

/*
P -> PR
R -> RS
S -> SP
*/


void sortLine(char* str, int p, int len)
{
    if (len == 1)
    {
        return;
    }
    if (len == 2)
    {
        if (str[p] > str[p + 1]) {
            swap(str[p], str[p + 1]);
        }

        return;
    }

    int halflen = len >> 1;
    sortLine(str, p, halflen);
    sortLine(str, p + halflen, halflen);

    if (strncmp(str + p, str + p + halflen, halflen) > 0)
    {
        strncpy(tmp, str + p, halflen);
        strncpy(str + p, str + p + halflen, halflen);
        strncpy(str + p + halflen, tmp, halflen);
    }
}
void getAns(int n, char init)
{
    string curr, next;
    curr.reserve(1 << n);
    next.reserve(1 << n);
    curr.push_back(init);
    for (int i = 0; i < n; ++i)
    {
        next.clear();
        for (auto ch : curr)
        {
            switch (ch)
            {
            case 'R':
                next.push_back('R');
                next.push_back('S');
                break;
            case 'P':
                next.push_back('P');
                next.push_back('R');
                break;
            case 'S':
                next.push_back('P');
                next.push_back('S');
                break;
            }
        }

        next.swap(curr);
    }

    strncpy(ans, curr.c_str(), curr.size());
    ans[curr.size()] = '\0';
    sortLine(ans, 0, curr.size());
}




bool isValidBegin(int n, int r, int p, int s, int nr, int np, int ns)
{
    for (int i = 0; i < n; ++i)
    {
        int tr = 0, tp = 0, ts = 0;
        tr += np + nr;
        ts += ns + nr;
        tp += np + ns;
        nr = tr;
        np = tp;
        ns = ts;
    }

    return (nr == r && ns == s && np == p);
}

int main()
{
    int Cases = 0;
    scanf("%d", &Cases);
    for (int c = 1; c <= Cases; ++c)
    {
        int n, r, p, s;
        scanf("%d%d%d%d", &n, &r, &p, &s);
        if (isValidBegin(n, r, p, s, 0, 0, 1))
        {
            getAns(n, 'S');
            printf("Case #%d: %s\n", c, ans);
            continue;
        }

        if (isValidBegin(n, r, p, s, 0, 1, 0))
        {
            getAns(n, 'P');
            printf("Case #%d: %s\n", c, ans);
            continue;
        }

        if (isValidBegin(n, r, p, s, 1, 0, 0))
        {
            getAns(n, 'R');
            printf("Case #%d: %s\n", c, ans);
            continue;
        }

        printf("Case #%d: IMPOSSIBLE\n", c);
    }

    return 0;
}

