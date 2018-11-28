//Przemysław Jakub Kozłowski
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#define FI first
#define SE second
#define MP(a,b) make_pair(a,b)
using namespace std;
typedef long long LL;
const int MOD = 1000002013, M = 1003;

/*bool cmp(const pair<int, int> &a, const pair<int, int> &b)
{
    if(a.FI == b.FI) return a.SE > b.SE;
    else return a.FI < b.FI;
}*/

LL PRZED(LL x);

int t;
int n, m, k;
pair<int, int> otw[M];
pair<int, int> zam[M];
vector<pair<int,int> > S;

int main()
{
    scanf("%d", &t);

    for(int ti = 1;ti <= t;ti++)
    {
        scanf("%d%d", &n, &m);

        LL wpocz = 0;
        S.clear();
        k = 0;

        for(int i = 1;i <= m;i++)
        {
            int a,b,c;
            scanf("%d%d%d", &a, &b, &c);
            wpocz += (LL)c*PRZED(b-a)%MOD;
            ++k;
            otw[k] = MP(a,c);
            zam[k] = MP(b,c);
        }

        sort(otw+1,otw+k+1);
        sort(zam+1,zam+k+1);

        LL wyn = 0;

        for(int i = 1, j = 0;i <= k;i++)
        {
            while(j < k && otw[j+1].FI <= zam[i].FI) S.push_back(otw[++j]);

            //cerr << "I: " << i << endl;
            //cerr << "S.size(): " << S.size() << " S: ";
            //for(int l = 0;l < S.size();l++) cerr << "(" << S[l].FI << " " << S[l].SE << "),  ";
            //cerr << endl;

            int zost = zam[i].SE;
            while(zost > 0)
            {
                int roz = min(S.back().SE, zost);
                S.back().SE -= roz;
                zost -= roz;
                //cerr << "ROZ: " << roz << " przed: " << zam[i].FI-S.back().FI << endl;
                wyn += (LL)roz*PRZED(zam[i].FI-S.back().FI)%MOD;
                if(S.back().SE == 0) S.pop_back();
            }
        }

        printf("Case #%d: %d\n", ti, (wpocz-wyn)%MOD);
    }

    return 0;
}

LL PRZED(LL x)
{
    return (x*n-x*(x-1)/2)%MOD;
}