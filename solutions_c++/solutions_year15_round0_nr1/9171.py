#include <iostream>
using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int i=1; i<=t; ++i)
    {
        int sm;
        char s[1002];
        cin >> sm >> s;
        int req = 0, count = 0;
        for(int j = 0; j<=sm; ++j)
        {
            if(count < j)
            {
                req += (j - count);
                count += (j - count);
            }
            count += (s[j] - '0');
        }
        cout << "Case #" << i << ": " << req << "\n";
    }
}

