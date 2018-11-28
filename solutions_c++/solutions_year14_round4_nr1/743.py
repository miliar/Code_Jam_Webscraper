#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>

#define f(i,a,b) for(int i = (a); i <= (b); i++)
#define fd(i,a,b) for(int i = (a); i >= (b); i--)

typedef long long ll;
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

bool U[10005];
int N, X, T;
multiset<int> S;

int main()
{
    fin >> T;

    f(t,1,T)
    {
        fin >> N >> X;

        f(i,0,N-1)
        {
            int x;
            fin >> x;
            S.insert(x);
        }

        int ans = 0;

        while(!S.empty())
        {
            ans++;
            int sz = *S.begin();

            auto it = S.upper_bound(X - sz);

            if(it == S.begin())
            {
                S.erase(S.begin());
                continue;
            }

            it--;

            if(it == S.begin())
            {
                S.erase(S.begin());
                continue;
            }

            S.erase(S.begin());
            S.erase(it);
        }

        cout << "Case #" << t << ": " << ans << "\n";
        fout << "Case #" << t << ": " << ans << "\n";
    }
}
