#include <string.h>
#include <assert.h>

#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>

using namespace std;

const int UU = 1, DD = 2, LL = 4, RR = 8;

int char_to_dir(char c)
{
    switch(c)
    {
        case '^': return UU;
        case '>': return RR;
        case 'v': return DD;
        case '<': return LL;
        case '.': return 0;
        default: assert(0);
    }
}

void solve(const int t)
{
    int R, C;
    vector<string> M;
    vector<vector<int> > flags;
    assert(cin >> R >> C);
    M.resize(R);
    flags.resize(R);
    for(int i = 0; i < R; ++i)
    {
        assert(cin >> M[i]);
        flags[i].assign(C, 0);
    }
    for(int i = 0; i < R; ++i)
    {
        int j;
        for(j = 0; j < C && M[i][j] == '.'; ++j);
        if(j < C)
            flags[i][j] |= LL;
        for(j = C - 1; j >= 0 && M[i][j] == '.'; --j);
        if(j >= 0)
            flags[i][j] |= RR;
    }
    for(int j = 0; j < C; ++j)
    {
        int i;
        for(i = 0; i < R && M[i][j] == '.'; ++i);
        if(i < R)
            flags[i][j] |= UU;
        for(i = R - 1; i >= 0 && M[i][j] == '.'; --i);
        if(i >= 0)
            flags[i][j] |= DD;
    }
    int res = 0;
    for(int i = 0; i < R; ++i)
        for(int j = 0; j < C; ++j)
        {
            //cerr << i << " " << j << " " << flags[i][j] << "\n";
            if(flags[i][j] == (UU | DD | LL | RR))
            {
                cout << "Case #" << t << ": IMPOSSIBLE\n";
                return;
            }
            if(flags[i][j] & char_to_dir(M[i][j]))
                ++res;
        }
    cout << "Case #" << t << ": " << res << "\n";
}

int main()
{
    int T;
    
    cin >> T;
    for(int t = 1; t <= T; ++t)
    {
        cerr << "Solving #" << t << "\n";
        solve(t);
    }
    return 0;
}
