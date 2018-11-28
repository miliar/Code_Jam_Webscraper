#include <iostream>

using namespace std;

bool CanFill(int X, int R, int C)
{
    if ((R * C) % X)
        return false;
    
    // Can always do it, if there is enough size
    if (X < 3)
        return true;
    
    int smaller = min(R, C), larger = max(R, C);
    
    if (X == 3)
    {
        return smaller > 1 && larger >= 3;
    }
    
    // X == 4
    return smaller >= 3 && larger >= 4;
}

int main()
{
    int T;
    cin >> T;
    
    for (int t = 1; t <= T; ++t)
    {
        int X, R, C;
        cin >> X >> R >> C;
        
        if (CanFill(X, R, C))
            cout << "Case #" << t << ": GABRIEL\n";
        else
            cout << "Case #" << t << ": RICHARD\n";
    }
}