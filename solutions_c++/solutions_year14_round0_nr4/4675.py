#include <iostream>
#include <algorithm>
#include <set>
#include <cstring>
#include <cstdio>

using namespace std;

const int MaxN = 10000;
const double eps = 1e-6;

int sig(double x)
{
    if(x < -eps) return -1;
    else if(x > eps) return 1;
    else return 0;
}

int N;

double nw[MaxN], kw[MaxN];

int main()
{
    int T;
    cin >> T;

    for(int c=0; c<T; c++)
    {
        cin >> N;

        for(int i=0; i<N; i++)
            cin >> nw[i];
        for(int i=0; i<N; i++)
            cin >> kw[i];

        sort(nw, nw+N);
        sort(kw, kw+N);
        
        
        // deceiful war

        int dwscore = 0;
        int r = 0;
        int p = 0, q = N-1;

        while(r < N)
        {
            if(sig(nw[r] - kw[p]) > 0)  // eat small
                dwscore++,
                r++, p++;
            else if(sig(nw[r] - kw[q]) < 0)  // cheat big
                r++, q--;
            else break;
        }

        dwscore += N - r;

        // normal war
       
        int score = 0;
        set<double> kwtree;
        for(int i=0; i<N; i++)
            kwtree.insert(kw[i]); 

        for(int i=0; i<N; i++)
        {
            auto it = kwtree.upper_bound(nw[i]);
            if(it == kwtree.end())
            {
                kwtree.erase(kwtree.begin());
                score++;
            }
            else
            {
                kwtree.erase(it);
            }
        }

    
        printf("Case #%d: %d %d\n", c+1, dwscore, score);
    }

    return 0;
}
