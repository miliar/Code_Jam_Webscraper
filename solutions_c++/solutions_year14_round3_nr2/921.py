#include <fstream>
#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <cstring>
#include <cstdio>
#define add push_back
using namespace std;

char a[1000];
vector<string> v;
int fcv[500];
bool fail[500];
vector<int> indx;
string aux;

bool ok()
{
    int i;
    bool hasSomething;
    aux = "";
    for (i = 0; i < 500; i++)
        fail[i] = 0;
    for (i = 0; i < v.size(); i++)
        aux += v[indx[i]];
    for (i = 1; i < aux.size(); i++)
    {
        if (aux[i-1] != aux[i])
            fail[aux[i-1]] = 1;
        if (fail[aux[i]])
            return 0;
    }
    return 1;
}
int main()
{
    freopen("2.in", "r", stdin);
    //freopen("2.out", "w", stdout);
    ofstream fout("2.out");

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
        for (i = 0; i < 500; i++)
            fcv[i] = fail[i] = 0;

        for (j = 0; a[j]; j++)
            fcv[a[j]]++;

        p = strtok(a, " ");
        while (p)
        {
            v.add(string(p));
            indx.add(indx.size());
            p = strtok(NULL, " ");
        }

        cnt = 0;
        do
        {
            isOK = ok();
            cnt += isOK;

            //printf("%s (%d)\n", aux.data(), isOK);
        } while (next_permutation(indx.begin(), indx.end()));

        //printf("Case #%d: %d\n", k, cnt);
        fout << "Case #" << k << ": " << cnt << "\n";
        cerr << k << '\n';
    }
    return 0;
}
