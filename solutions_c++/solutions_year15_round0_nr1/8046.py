#include <iostream>
#include <cstdlib>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int i=1; i<=t; i++)
    {
        int n;
        string s;
        cin >> n >> s;
        int count = 0;
        int add = 0;
        for(int j=0; j<=n; j++)
        {
            int numshy = s[j] - '0';
            if( count < j)
            {
                add += j - count;
                count = j;
            }
            count += numshy;
        }
        cout << "Case #" << i << ": " << add << endl;
    }
    return 0;
}


