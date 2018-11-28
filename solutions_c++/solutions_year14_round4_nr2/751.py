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

int A[1005], P[1005];
int T, N;
map<int,int> M;

int main()
{
    fin >> T;

    f(t,1,T)
    {
        fin >> N;
        set<int> s;

        M.clear();

        f(i,1,N)
        {
            fin >> A[i];
            s.insert(A[i]);
        }

        int c = 1;

        for(int k : s) M[k] = c++;
        f(i,1,N) A[i] = M[A[i]];

        int ans = 0;
        f(i,1,N)
        {
            int p = 0;
            f(x,1,N) if(A[x] >= i) P[A[x]] = ++p;

            ans += min(abs(1-P[i]),abs(N-i+1-P[i]));
        }

        cout << "Case #" << t << ": " << ans << "\n";
        fout << "Case #" << t << ": " << ans << "\n";
    }
}
