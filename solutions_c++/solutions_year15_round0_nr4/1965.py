#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    int T;
    cin >> T;
    for (int qq = 1; qq <= T; qq++)
    {
        int X, R, C; cin >> X >> R >> C;
        bool richard = false;
   

        if (R*C % X != 0) richard = true;
        
        if (X == 3 && R*C == 3) richard = true;
        if (X == 4 && R*C == 4) richard = true;

        if (X == 4 && (R*C == 8) )
        {
            richard = true;
        }

        cout << "Case #" << qq << ": " << (richard? "RICHARD" : "GABRIEL") << endl;
                
    }
    return 0;
}
