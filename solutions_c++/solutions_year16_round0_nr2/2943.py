#include <iostream>
#include <map>
#include <string>
using namespace std;

map<string, int> m;

int main()
{
    int n;
    cin >> n;
    int N = 0;
    while (n--)
    {
        N++;
        string s;
        cin >> s;
        char pos = s[0];
        int count = 0;
        for (int i = 1; i < s.size(); i++)
        {
            if (pos == s[i])
                continue;
            else
            {
                pos = s[i];
                count++;
            }
        }
        if (pos == '-')
            count++;
        cout << "Case #" << N << ": " << count << endl;
    }
    return 0;
    
}