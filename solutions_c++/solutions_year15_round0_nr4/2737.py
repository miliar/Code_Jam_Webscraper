#include <iostream>
#include <string>
#include <vector>
#include <string>
#include <set>
#include <cmath>
#include <map>
#include <list>
#include <algorithm>
#include <utility>

using namespace std;

int main()
{
    unsigned int N;
    cin >> N;
    for(int n = 1; n <= N; ++n)
    {
        unsigned int X, R, C;
        cin >> X >> R >> C;
        bool win = (R * C % X == 0);
        if(win)
        {
            if(X == 3)
            {
                win = ((R >= 3 && C >= 2) || (R>= 2 && C >= 3));
            }
            else if(X == 4)
            {
                win = ((R * C % 4 == 0) && ((R >= 3 && C >= 4) || (R >= 4 && C >= 3)));
            }
        }
        cout << "Case #" << n << ": " << (win? "GABRIEL": "RICHARD") << endl;
    }
    return 0;
}
