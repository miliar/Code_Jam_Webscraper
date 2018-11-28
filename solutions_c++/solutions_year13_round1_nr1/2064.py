#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int main ()
{
    long T, t, r;
    
    cin >> T;
    for (int i = 0; i < T; ++i)
    {
        cin >> r;
        cin >> t;
        
        r = r + 1;
        
        int count = 0;
        while ( t >= ((r * r) - ((r-1)*(r-1))) )
        {
            t -= ((r * r) - ((r-1)*(r-1)));
            r += 2;
            
            ++count;
        }
        
        cout << "Case #" << i + 1 << ": " << count << endl;
    }
    
  	return 0;
}

/*

 5
 1  9
 1  10
 3  40
 
*/