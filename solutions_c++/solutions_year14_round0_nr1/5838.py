//takes input and does shit
#include <iostream>

using namespace std;
int process();

int main ()
{
    int test;
    cin >> test;
    int i; // loop variable
    int result[test]; // results for each case
    for ( i = 0 ; i < test; i++)
    {
        result[i]=process();
    }
    
    //print results
    for (i = 0 ; i < test; i++)
    {
        cout << "Case #" << (i+1) << ": ";
        switch (result[i])
        {
            case 17 :  cout << "Bad Magician!\n";
            break;
            case 0 :   cout << "Volunteer Cheated!\n";
            break;
            default :  cout << result[i] << "\n";
            break;
        }
    }
}

int process()
{
    //take in 4 numbers
    int arrange1[4][4];
    //row inputs
    int r1, r2;
    cin >> r1;
    //loops and shit
    int i,j; // loop
    for (i = 0 ; i < 4; i++)
    {
        cin >> arrange1[i][0] >> arrange1[i][1] >> arrange1[i][2] >> arrange1[i][3];
    }
    int arrange2[4][4];
    cin >> r2;
    for (i = 0 ; i < 4; i++)
    {
        cin >> arrange2[i][0] >> arrange2[i][1] >> arrange2[i][2] >> arrange2[i][3];
    }
    //compare and check each numbers
    int result;
    r1 --;
    r2 --;
    int compared = 0;
    for ( i = 0 ; i < 4; i++ )
    {
        if (arrange1[r1][i] == arrange2[r2][0])
        {
            compared ++;
            result = arrange1[r1][i];
        }
        if (arrange1[r1][i] == arrange2[r2][1])
        {
            compared ++;
            result = arrange1[r1][i];
        }
        if (arrange1[r1][i] == arrange2[r2][2])
        {
            compared ++;
            result = arrange1[r1][i];
        }
        if (arrange1[r1][i] == arrange2[r2][3])
        {
            compared ++;
            result = arrange1[r1][i];
        }
    }
    if (compared == 0)
    {
        result = 0;
    }
    if (compared > 1)
    {
        result = 17;
    }
    return result;
}