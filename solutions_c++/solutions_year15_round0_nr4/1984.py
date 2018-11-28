#include <iostream>
using namespace std;
int T, a, b, c;
int main()
{
    scanf("%d", &T);
    for (int I = 1; I <= T; ++I)
    {
        scanf("%d%d%d", &a, &b, &c);
        if (a >= 7 || (b * c) % a != 0 || (a >= b+c-2 && a > 3) || (a > 2 && (a+1)/2 > min(b, c)))
            cout << "Case #" << I << ": RICHARD" << endl;
        else 
            cout << "Case #" << I << ": GABRIEL" << endl;
    }
}
