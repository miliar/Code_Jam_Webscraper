#include <stdio.h>
#include <iostream>
using namespace std;
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T, casno, Sm, stand, borrow, i;
    char man[1010];
    scanf("%d", &T);
    for(casno = 1; casno <= T; casno++)
    {
        cin >> Sm >> man;
        stand = 0;
        borrow = 0;
        for(i = 0; i <= Sm; i++)
        {
            if(stand >= i)
            {
                stand = stand + (man[i] - 48);
            }
            else
            {
                borrow += (i - stand);
                stand += (i-stand);
                stand += (man[i] - 48);
            }
        }
        cout << "Case #" << casno << ": ";
        cout << borrow << endl;
    }
    return 0;
}
