#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <utility>
#include <set>
#include <string>

using namespace std;

int BFF[1001];
int perm[1001];

int maxRep = 0;
bool found;
int N;

void gen(int posPerm, int prev, int maxi)
{
    if (found || prev >= N)
        return;
    if (posPerm == maxi+1)
    {
        //cout << "lal" << endl;
        do
        {
            perm[0] = perm[maxi];
            perm[maxi+1] = perm[0];
            bool ok = true;
            for (int i = 1; i <= maxi; i++)
            {

                if (perm[i-1] != BFF[perm[i]] && perm[i+1] != BFF[perm[i]])
                {
                    ok = false;
                    break;
                }
            }
            if (ok)
            {
                maxRep = maxi;
                found = true;
                return;
            }
        }
        while (next_permutation(perm+1, perm+maxi+1));

    }


    else
    {
        //cout << posPerm << endl;
        perm[posPerm] = prev+1;
        gen(posPerm+1, prev+1, maxi);
        gen(posPerm, prev+1, maxi);

    }
}

int main()
{
    //cin.tie(0);
    //ios::sync_with_stdio(false);
    freopen("t.in", "r", stdin);
    freopen("t.out", "w", stdout);


    int nbT;
    cin >> nbT;



    for (int t = 1; t <= nbT; t++)
    {
        cin >> N;
        for (int i = 0; i < N; i++)
        {
            cin >> BFF[i];
            BFF[i]--;
        }
        maxRep = 0;
        found = false;
        for (int len = N; len >= 2; len--)
        {
            //cout << "lol" << endl;
            for (int i = 0; i < N; i++)
                perm[i] = i;
            gen(1, -1, len);
            if (found)
            {
                break;
            }

        }


        cout << "Case #" << t << ": " << maxRep << '\n';
    }


    return 0;
}
