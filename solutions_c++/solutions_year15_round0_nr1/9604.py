#include <iostream>
using namespace std;

int main()
{
    int T, t, max, n, count, i;
    bool S[1005];
    char m[1005];
    int M[1005];
    
    cin >> T;
    for (t = 1; t <= T; t++)
    {
        count = 0;
        n = 0;
        cin >> max;
        cin.get();
        for (i = 0; i <= max; i++)
        {
            cin.get(m[i]);
            M[i] = (int)(m[i] - '0');
            //cout << M[i] << " -- ";
        }
        
        i = 1;
        if (M[0] > 0)
        {
            n = M[0];
            //cout << n << " people already clapping!" << endl;
            count = 0;
        }
        else
        {
           //cout << "we add 1 friend!" << endl;
           count = 1;
           M[0] = 1;
           n = 1;
        }
        
        while (i <= max)
        {
            if (n < i) // we need more people
            {
                //cout << "we need more people: " << n << " is less than " << i << endl;
                count += (i - n);
                n = i;
                //cout << "count is now " << count << endl;
            }
            n += M[i];
            i++;
        }
        
        cout << "Case #" << t <<": " << count << endl;
    }
    return 0;
}