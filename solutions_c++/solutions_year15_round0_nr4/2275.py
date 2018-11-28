#include <iostream>

using namespace std;
int main()
{
    int round;
    cin >> round;
    for (int i=1; i<=round; i++)
    {
        int X, R, C;
        cin >> X >> R >> C;

        string ans;
        if (X == 1)
        {
            ans = "GABRIEL";
        }
        else if (X == 2)
        {
            if (R == 3 && C == 3||
                R == 1 && C == 3||
                R == 3 && C == 1||
                R == 1 && C == 1)
                ans = "RICHARD";
            else
                ans = "GABRIEL";              
        }
        else if (X == 3)
        {
            if (R == 2 && C == 3 ||
                R == 3 && C == 2 ||
                R == 4 && C == 3 ||
                R == 3 && C == 4 ||
                R == 3 && C == 3)
                ans = "GABRIEL";              
            else
                ans = "RICHARD";
        }
        else if (X == 4)
        {
            if (R == 3 && C == 4 ||
                R == 4 && C == 3 ||
                R == 4 && C == 4)
                ans = "GABRIEL";
            else
                ans = "RICHARD";              
        }
        cout << "Case #" << i << ": " << ans << endl;
    }
}
