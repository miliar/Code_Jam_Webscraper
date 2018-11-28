// CodeJam 2016 Qualification A
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main()
{
    int T, N;
    vector<bool> found;
    int countFound, lastDigit;
    
    cin >> T;
    for(int c = 1; c <= T; ++c)
    {
        cout << "Case #" << c << ": ";
        cin >> N;

        if (N == 0)
        {
            cout << "INSOMNIA" << endl;
            continue;
        }
        
        found.assign(10,false);
        countFound = 0;
        int i = 0;
        while (countFound < 10)
        {
            ++i;
            long long multiple = i * N;
            while (multiple > 0)
            {
                lastDigit = multiple % 10;
                multiple /=  10;
                
                if (!found[lastDigit])
                {
                    ++countFound;
                    found[lastDigit] = true;
                }
            }
        }
        
        cout << i * N << endl;
    }
}
