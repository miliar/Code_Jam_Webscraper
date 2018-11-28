#include <iostream>
#include <cstring>

using namespace std;

int main()
{
    int t;
    cin >> t;
    int j = 1;
    while( t -- )
    {
        int k;
        string s;
        cin >> k >> s;
        long long int wyn = 0;
        long long int sum = 0;
        for( int i = 0; i < s.size(); i ++ )
        {
            if( wyn < i )
            {
                sum += (i - wyn);
                wyn += (i - wyn);
            }
            wyn += (s[i] - '0');
        }
        cout << "Case #" << j << ": " << sum << "\n";
        j ++;
    }
    return 0;
}
