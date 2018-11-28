#include<iostream>
using namespace std;
int main()
{
    unsigned short T;
    cin >> T;
    for ( int i = 0; i < T; i++ )
    {
        int row, temp, a[4], b[4];
        cin >> row;
        row--;
        for ( int j = 0; j < 16; j++ )
        {
            cin >> temp;
            if ( j / 4 == row )
                a[j % 4] = temp;
        }
        cin >> row;
        row--;
        for ( int j = 0; j < 16; j++ )
        {
            cin >> temp;
            if ( j / 4 == row )
                b[j % 4] = temp;
        }
        unsigned short count = 0;
        short ans = -1;
        for ( int j = 0; j < 16 && count < 2; j++ )
        {
            if ( a[j % 4] == b[j / 4] )
            {
                count++;
                ans = a[j % 4];
            }
        }
        if ( count == 2 )
            cout << "Case #" << i + 1 << ": Bad magician!\n";
        else if ( count == 1 )
            cout << "Case #" << i + 1 << ": " << ans << "\n";
        else
            cout << "Case #" << i + 1 << ": Volunteer cheated!\n";
    }
}