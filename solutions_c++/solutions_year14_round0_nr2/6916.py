#include <algorithm>
#include <iostream>
using namespace std;

int main()
{
    int tests_count;
    cin >> tests_count;
    
    for (size_t i = 0; i < tests_count; ++i)
    {
        double c, f, x, p = 2, rs = 0;
        cin >> c >> f >> x;
        
        while (true)
        {
            double t1 = x / p;
            double t2 = (c / p) + (x / (p + f));
            
            if (t1 <= t2)
            {
                rs += t1;
                break;
            }
            else
            {
                rs += (c / p);
                p  += f;
            }
        }
        
        cout.setf(ios::fixed, ios::floatfield);
        cout.precision(7);
        cout << "Case #" << (i + 1) << ": " << rs << endl;
    }
    
    return 0;
}