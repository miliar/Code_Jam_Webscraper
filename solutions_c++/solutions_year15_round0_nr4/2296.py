#include <iostream>
#include <string>

using namespace std;

// brute force the small instances

bool RWins(int X, int R, int C)
{
    if(R > C)
        return RWins(X,C,R);
    
    if(X == 1) 
    {
        return false;
    }
    else if(X == 2)
    {
        return (R*C % 2 == 1);
    }
    else if(X == 3)
    {
        if(R*C % 3 != 0)
            return true;
        else if(R == 1 || C == 1)
            return true;
        else
            return false;
    }
    else if(X == 4)
    {
        if( R <= 3 && C <= 3 )
            return true;
        else if( R < 3 )
            return true;
        return false;
    }
    
    if( X >= 7 )
        return true;
    else
        return false;
}

int main()
{
    int tests;
    cin >> tests;
    //cout << tests << endl;
    
    for(int i = 0; i < tests; i++)
    {
        int X, R, C;
        cin >> X >> R >> C;
        
        cout << "Case #" << i+1 << ": " << (RWins(X,R,C)?"RICHARD":"GABRIEL") << endl;
    }
    
    return 0;
}