
#include <cstdio> 
#include <iostream>
#include <string>

using namespace std;

typedef unsigned long long ull;

ull help(ull start, ull len, ull depth)
{
    ull sum = 0;
    for (ull i = 0; i < len; i++ )
    {
        sum *= depth;
        ull factor = start + i - 1;
        sum += factor ;

    }
    return sum+1 ;
}

int main()
{
    int T;
    cin >> T;
  
    int count = 1;
    while(T--)
    {
       ull len, depth, c;
       cin >> len;    
       cin >> depth;    
       cin >> c;
       cout << "Case #" << count++ << ":";
       if (c*depth < len)    
        {
            cout << " IMPOSSIBLE" << endl;
        }  
        else 
        {
            for (ull i = 1; i <= len; i += depth)
            {
                cout << " " << help(i, min(len - i + 1, depth), len);
            }
            cout << endl;
        }

            
    }
    
}
   
