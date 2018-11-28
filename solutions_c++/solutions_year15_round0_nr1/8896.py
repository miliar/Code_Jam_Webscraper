#include <iostream>
#include <string>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int i=0; i<t; i++)
    {
        int sm;
        cin >> sm;
        string s;
        cin >> s;
        int r = 0;
        int a = 0;
        for(int j=0; j<s.length(); j++)
        {
            int si = s[j] - '0';
            if(a+r < j)
            {
                r += j-(a+r);
            }
            a += si;
        }
        cout << "Case #" << i+1 << ": " << r << endl;
    }
    return 0;
}

