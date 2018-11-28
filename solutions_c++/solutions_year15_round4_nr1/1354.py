#include <iostream>
#include <cmath>
#include <cstdio>
#include <algorithm>

using namespace std;

int R , C , ans;
string A[150];

bool check(int i , int j)
{
    if(A[i][j] == '^')
        for(int k = i - 1;k > -1;--k)
            if(A[k][j] != '.')
                return true;

    if(A[i][j] == 'v')
        for(int k = i + 1;k < R;++k)
            if(A[k][j] != '.')
                return true;


    if(A[i][j] == '>')
        for(int k = j + 1;k < C;++k)
            if(A[i][k] != '.')
                return true;

    if(A[i][j] == '<')
        for(int k = j - 1;k > -1;--k)
            if(A[i][k] != '.')
                return true;

    for(int k = i - 1;k > -1;--k)
        if(A[k][j] != '.')
        {
            ++ans;
            return true;
        }

    for(int k = i + 1;k < R;++k)
        if(A[k][j] != '.')
        {
            ++ans;
            return true;
        }


    for(int k = j + 1;k < C;++k)
        if(A[i][k] != '.')
        {
            ++ans;
            return true;
        }

    for(int k = j - 1;k > -1;--k)
        if(A[i][k] != '.')
        {
            ++ans;
            return true;
        }

    return false;
}

int main()
{
    freopen("A-large.in" , "r" , stdin);
    freopen("out.out" , "w" , stdout);

    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int T , c = 0;
    cin >> T;
    while(T--)
    {
        ++c;
        cin >> R >> C;
        for(int i = 0;i < R;++i)
            cin >> A[i];

        ans = 0;
        bool poss = true;
        for(int i = 0;i < R && poss;++i)
            for(int j = 0;j < C;++j)
                if(A[i][j] != '.' && !check(i , j))
                    poss = false;

        if(!poss)
            cout << "Case #" << c << ": IMPOSSIBLE\n";

        else
            cout << "Case #" << c << ": " << ans << "\n";

    }
    return 0;
}
/*. period = no arrow
^ caret = up arrow
> greater than = right arrow
v lowercase v = down arrow
< less*/
