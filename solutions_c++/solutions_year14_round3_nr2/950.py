#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <string.h>
#include <stdio.h>

using namespace std;

char a[1000];
vector<string> v;
int frecv[500];
int fail[500];
vector<int> vec;

void form()
{
    char *p;
    for (int j = 0; a[j]; j++)
        frecv[a[j]]++;

    p = strtok(a, " ");
    while (p)
    {
        v.push_back((string(p)));
        vec.push_back((vec.size()));
        p = strtok(0, " ");
    }
}

int ok()
{
    string * aux;
    char c;
    for (int i = 'a'; i <= 'z'; i++)
        fail[i] = 0;

    for (int i = 0; i < v.size(); i++)
    {
        aux = &v[vec[i]];
        if (i > 0)
        if ((*aux)[0] != (c = v[vec[i-1]][(int)v[vec[i-1]].size()-1]))
            fail[c] = 1;
        if (fail[(*aux)[0]])
            return 0;
        for (int j = 1; j < (*aux).size(); j++)
        {
            if ((*aux)[j-1] != (*aux)[j])
                fail[(*aux)[j-1]] = 1;
            if (fail[(*aux)[j]])
                return 0;
        }
    }
    return 1;
}

void reset()
{
    v.clear();
    vec.clear();
    for (int i = 'a'; i <= 'z'; i++)
        frecv[i] = fail[i] = 0;
}

int main()
{
    freopen("train.in", "r", stdin);
    FILE * f = fopen("train.out", "w");
    int t, x;
    int nrrr;
    int e_ok;
    scanf("%d\n", &t);
    for (int k = 1; k <= t; k++)
    {
        scanf("%d\n", &x);
        gets(a);
        scanf("\n");
        reset();
        form();
        nrrr = 0;
        do
        {
            e_ok = ok();
            nrrr += e_ok;
        } while (next_permutation(vec.begin(), vec.end()));
        fprintf(f, "Case #%d: %d\n", k, nrrr);
        printf("%d\n", k);
    }
    return 0;
}
