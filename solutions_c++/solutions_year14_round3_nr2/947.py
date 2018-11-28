#include <fstream>
#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <cstring>
#include <cstdio>

using namespace std;

char a[1000];
vector<string> v;
int fcv[500];
bool fail[500];
vector<int> indx;

bool ok()
{
    string * aux;
    int i, j;
    char c;
    bool hasSomething;
    for (i = 'a'; i <= 'z'; i++)
        fail[i] = 0;

    for (i = 0; i < v.size(); i++)
    {
        aux = &v[indx[i]];
        if (i > 0)
        if ((*aux)[0] != (c = v[indx[i-1]][(int)v[indx[i-1]].size()-1]))
            fail[c] = 1;
        if (fail[(*aux)[0]])
            return 0;
        for (j = 1; j < (*aux).size(); j++)
        {
            if ((*aux)[j-1] != (*aux)[j])
                fail[(*aux)[j-1]] = 1;
            if (fail[(*aux)[j]])
                return 0;
        }
    }
    return 1;
}
int main()
{
    freopen("second.in", "r", stdin);
    FILE * f = fopen("second.out", "w");

    int t, x;
    int i, j, k;
    char * p;
    int cnt;
    bool isOK;
    scanf("%d\n", &t);
    for (k = 1; k <= t; k++)
    {
        scanf("%d\n", &x);
        gets(a);
        scanf("\n");
        v.clear();
        indx.clear();
        for (i = 'a'; i <= 'z'; i++)
            fcv[i] = fail[i] = 0;

        for (j = 0; a[j]; j++)
            fcv[a[j]]++;

        p = strtok(a, " ");
        while (p)
        {
            v.push_back(string(p));
            indx.push_back(indx.size());
            p = strtok(NULL, " ");
        }

        cnt = 0;
        do
        {
            isOK = ok();
            cnt += isOK;
        } while (next_permutation(indx.begin(), indx.end()));

        fprintf(f, "Case #%d: %d\n", k, cnt);
        printf("%d\n", k);
    }
    return 0;
}
