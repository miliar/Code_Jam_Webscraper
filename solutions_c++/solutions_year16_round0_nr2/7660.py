#include <iostream>
#include <string>
using namespace std;

int main()
{
    int t;
    string s;
    cin >> t;

    for( int i = 1; i <= t; ++i )
    {
        cin >> s;
        cout << "Case #" << i << ": ";
        size_t last;
        int count = 0;
        while( (last = s.rfind('-')) != std::string::npos )
        {
            size_t first = s.find('-');
            if( first != 0 )
            {
                for (int a = 0; a < first; ++a) s[a] = '-';
                ++count;
            }

            if( s.find('-') == std::string::npos ) break;
            std::string sub = s.substr(0, last+1);
            for(int a = 0; a < sub.length(); ++a)
            {
                s[a] = sub[sub.length() - a - 1] == '-' ? '+' : '-';
            }
            ++count;
        }
        cout << count << std::endl;
    }
    return 0;
}
