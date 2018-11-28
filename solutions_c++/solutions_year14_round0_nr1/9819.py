#include <iostream>
#include <fstream>
#include <bitset>
using namespace std;


const int BAD_MAGICIAN = 0;
const int VOLUNTEER_CHEATED = -1;


int commonElement (const int* a, const int* b)
{
    bitset<16 + 1> exists;
    
    for (int i = 0; i < 4; ++i)
        exists.set(a[i]);
    
    int matched = 0;
    int common;
    for (int i = 0; i < 4; ++i)
    {
        if (exists.test(b[i]))
        {
            ++matched;
            common = b[i];
        }
        
        if (matched > 1)
            return BAD_MAGICIAN;
    }
    
    if (!matched)
        return VOLUNTEER_CHEATED;

    return common;
}


void testRunner ()
{
    int tests;
    cin >> tests;
    
    for (int t = 0; t < tests; ++t)
    {
        cout << "Case #" << t+1 << ": ";
        
        int cardRow1;
        cin >> cardRow1;
        
        int num;
        int a[4];
        for (int i = 0; i < 4; ++i)
            for (int j = 0; j < 4; ++j)
            {
                cin >> num;
                if (i == cardRow1-1)
                    a[j] = num;
            }
        
        int cardRow2;
        cin >> cardRow2;
        
        int b[4];
        for (int i = 0; i < 4; ++i)
            for (int j = 0; j < 4; ++j)
            {
                cin >> num;
                if (i == cardRow2-1)
                    b[j] = num;
            }
        
        int i = commonElement(a, b);
        switch (i)
        {
            case BAD_MAGICIAN:
                cout << "Bad magician!";
                break;
                
            case VOLUNTEER_CHEATED:
                cout << "Volunteer cheated!";
                break;
                
            default:
                cout << i;
                break;
        }
        
        cout << "\n";
    }
}


int main()
{
    testRunner();
}
