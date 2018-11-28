//Przemysław Jakub Kozłowski
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#define FI first
#define SE second
#define MP make_pair
using namespace std;
typedef long long LL;
const int W = 10, M = 8;

void uluz(int x);

int t;
int m,n;
char S[W+7];
vector<int> tab[M+7];

int ulozenie[M+7];

pair<int,int> wyn;

int main()
{
    scanf("%d", &t);
    for(int ti = 1;ti <= t;ti++)
    {
        scanf("%d%d", &m, &n);

        for(int i = 1;i <= m;i++)
            tab[i].clear();

        for(int i = 1;i <= m;i++)
        {
            scanf(" ");
            int k;
            scanf("%s%n", S+1, &k);
            LL hash = 0;
            for(int j = 1;j <= k;j++)
            {
                hash = hash*27+(S[j]-'A'+1);
                tab[i].push_back(hash);
            }
        }

        wyn = MP(0,0);
        uluz(1);

        printf("Case #%d: %d %d\n", ti, wyn.FI, wyn.SE);
    }

    return 0;
}

void oblicz()
{
    /*cerr << "Ulozenie: ";
    for(int i = 1;i <= m;i++)
        cerr << ulozenie[i] << " ";
    cerr << endl;*/

    int twyn = 0;
    for(int i = 1;i <= n;i++)
    {
        typedef set<LL> S_;
        S_ S;

        for(int j = 1;j <= m;j++)
            if(ulozenie[j] == i)
            {
                S.insert(0);
                for(int l = 0;l < tab[j].size();l++)
                    S.insert(tab[j][l]);
            }

        twyn += S.size();
    }
    //cerr << "Twyn: " << twyn << endl;
    if(twyn > wyn.FI) wyn = MP(twyn, 1);
    else if(twyn == wyn.FI) wyn.SE++;
}

void uluz(int x)
{
    if(x == m+1)
    {
        oblicz();
        return;
    }
    for(int i = 1;i <= n;i++)
    {
        ulozenie[x] = i;
        uluz(x+1);
    }
}
