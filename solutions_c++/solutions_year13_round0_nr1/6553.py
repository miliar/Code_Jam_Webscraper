#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int n;
    cin >> n;
    string s[n*4];
    for( int i = 0 ; i < n*4 ; i++ )
    {
        cin >> s[i];
    }
    int count = 1;
    for( int i = 0 ; i < n*4 ; i += 4 )
    {
        int row1[4] = { 0 , 0 , 0 , 0};
        int column1[4] = { 0, 0 , 0 , 0};
        int diag11 = 0;
        int diag21 = 0;
        int row2[4] = { 0 , 0 , 0 , 0};
        int column2[4] = { 0, 0 , 0 , 0};
        int diag12 = 0;
        int diag22 = 0;
        int fill = 0;
        for( int j = i ; j < i+4 ; j++ )
        {
            for( int k = 0 ; k < 4 ; k++ )
            {
                if( s[j][k] == 'O' )
                {
                    row1[j%4]++;
                    column1[k]++;
                    if( j%4 == k )
                    {
                        diag11++;
                    }
                    if( ((j%4) == 0 && k == 3) || ((j%4) == 1 && k == 2) || ((j%4) == 2 && k == 1) || ((j%4) == 3 && k == 0) )
                    {
                        diag12++;
                    }
                    fill++;
                }
                if( s[j][k] == 'X' )
                {
                    row2[j%4]++;
                    column2[k]++;
                    if( j%4 == k )
                    {
                        diag21++;
                    }
                    if( ((j%4) == 0 && k == 3) || ((j%4) == 1 && k == 2) || ((j%4) == 2 && k == 1) || ((j%4) == 3 && k == 0) )
                    {
                        diag22++;
                    }
                    fill++;
                }
                if( s[j][k] == 'T' )
                {
                    row1[j%4]++;
                    column1[k]++;
                    row2[j%4]++;
                    column2[k]++;
                    if( j%4 == k )
                    {
                        diag21++;
                        diag11++;
                    }
                    if( ((j%4) == 0 && k == 3) || ((j%4) == 1 && k == 2) || ((j%4) == 2 && k == 1) || ((j%4) == 3 && k == 0) )
                    {
                        diag12++;
                        diag22++;
                    }
                    fill++;
                }
            }
        }
        int flag = 0;
        for( int l = 0 ; l < 4 ; l++ )
        {
            if( row1[l] == 4 || column1[l] == 4 )
            {
                cout << "Case #" << count << ": O won\n";
                flag = 1;
                break;
            }
            if( row2[l] == 4 || column2[l] == 4 )
            {
                cout << "Case #" << count << ": X won\n";
                flag = 1;
                break;
            }
        }
        if( flag == 1 )
        {
            flag = 0;
            count++;
            continue;
        }
        if( diag11 == 4 || diag12 == 4 )
        {
            cout << "Case #" << count << ": O won\n";
        }
        else if( diag21 == 4 || diag22 == 4 )
        {
            cout << "Case #" << count << ": X won\n";
        }
        else if( fill == 16 )
        {
            cout << "Case #" << count << ": Draw\n";
        }
        else
        {
            cout << "Case #" << count << ": Game has not completed\n";
        }
        count++;
    }
    return 0;
}
