#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int cases;
    cin >> cases;
    
    for(int tcase = 1; tcase <= cases; ++tcase)
    {
        int a, b, k;
        cin >> a >> b >> k;
        
        int count = 0;
        
        for(int i = 0; i < a; ++i)
        {
            for(int j = 0; j < b; ++j)
            {
                for(int l = 0; l < k; ++l)
                {
                    if(l == (i & j))
                    {
                        ++count;
                    }
                }
            }
        }
        
        cout << "Case #" << tcase << ": " << count << endl;
    }
    
    return 0;
}
