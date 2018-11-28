#include <fstream>
#include <cstring>
using namespace std;
ifstream fi("test.in");
ofstream fo("test.out");
int t, i, num[101], j, k, ans;
string s;
int main()
{
    fi >> t;
    for ( i = 1 ; i <= t ; i++ )
    {
        fi >> num[i];
        fi >> s;
        for ( j = 0 ; j < s.size() ; j++ )
        {
            if ( j <= k ) k = k + (int) s[j] - (int) '0';
            else
            {
                ans = ans + j - k;
                k = j + (int) s[j] - (int) '0';
            }
        }
        fo << "Case #" << i << ":" << " " << ans;
        fo << '\n';
        ans = 0; k = 0;
    }
}
