#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;

#define mo (1000000007)

int T, n, m;

string a[10];
int b[10];
bool flag[10];
int node[1000][30];
int NN;

void build(string p)
{
    int i = 0;

   // cout << p.length() << endl;
    for (int j = 0;j < p.length();++j )
    {
       // cout << j << ' ' <<
        if (node[i][p[j]-'A'] == 0)
        {
            ++NN;
            for (int k = 0;k < 26;++k)
                node[NN][k] = 0;
            node[i][p[j]-'A'] = NN;
            i = NN;
        }
        else i = node[i][p[j]-'A'];
    }
}

int chuli(int k)
{
    NN = 0;
    for (int i = 0;i < 26;++i)
        node[0][i] = 0;
    for (int i = 0;i < m;++i)
        if (b[i] == k)
        {

            build(a[i]);
        //    cout << a[i] << ' ' <<  NN << endl;
        }
    return NN+1;
}

void doit()
{
    int ans, s;
    int k;
    bool ff;

    ans = 0;
    scanf("%d%d", &m, &n);
    k = 1;
    for (int i = 0;i < m;++i)
    {
        cin >> a[i];
        k = k * n;
    }

    for (int i = 0;i < k;++i)
    {
        for (int j = 0;j < n;++j)
        flag[j] = false;
        int tmp = i;
        for (int j = 0;j < m;++j)
        {
            b[j] = tmp % n;
            flag[b[j]] = true;
            tmp /= n;
        }
        ff = true;
        for (int j = 0;j < n;++j)
            if (flag[j] == false)
            {
                ff = false; break;
            }
        if (!ff) continue;

        tmp = 0;
        for (int j = 0;j < n;++j)
        {
            tmp += chuli(j);
        //    printf("t%d %d\n", i,tmp);
        }
        if (tmp == ans) s++;
        else if (tmp > ans)
           {
               ans = tmp; s = 1;
           }
    }
    printf("%d %d\n", ans, s);
}

int main()
{
    freopen("D-small.in","r",stdin);
    freopen("D.out","w", stdout);
    scanf("%d", &T);
    for (int q = 1;q <= T;++q)
    {
        printf("Case #%d: ", q);
        doit();
    }
}
