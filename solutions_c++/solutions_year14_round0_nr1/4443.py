#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

#define FOR(i, a, b) for (int i = int(a); i < int(b); i++)
#define REP(i, a) for (int i = 0; i < int(a); i++)
#define INF 1000000000
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
typedef vector<bool> vb;


set<int> posibles;
int casos;

void solve(int actual)
{
    int a[5], fila;
    int encontrado = 0;
    int res = 0;

    posibles.clear();

    cin >> fila;

    REP(i, 4)
    {
        cin >> a[0] >> a[1] >> a[2] >> a[3];
        if(i+1 == fila)
        {
            posibles.insert(a[0]);
            posibles.insert(a[1]);
            posibles.insert(a[2]);
            posibles.insert(a[3]);
        }
    }

    cin >> fila;

    REP(i, 4)
    {
        cin >> a[0] >> a[1] >> a[2] >> a[3];
        if(i+1 == fila)
            REP(j, 4)
            {
                if(posibles.find(a[j]) != posibles.end())
                {
                    if(encontrado == 0)
                    {
                        encontrado = 1;
                        res = a[j];
                    }
                    else if(encontrado >= 1)
                    {
                        encontrado = 2;
                    }
                }
            }
    }
    if(encontrado == 1)
        printf("Case #%d: %d\n", actual,  res);
    else if(encontrado == 2)
        printf("Case #%d: Bad magician!\n", actual);
    else
        printf("Case #%d: Volunteer cheated!\n", actual);

}

int main()
{
    freopen("MagicTrick.out", "w", stdout);
    freopen("MagicTrick.in", "r", stdin);
    cin >> casos;

    REP(i, casos)
        solve(i+1);
    return 0;
}
