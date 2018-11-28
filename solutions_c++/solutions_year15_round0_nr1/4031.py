#include <iostream>
#include <string>
#include <fstream>
#define lol long long
using namespace std;

ofstream out("output.txt");
ifstream in("input.txt");

#define cin in
#define cout out


int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i)
    {
        lol ans = 0;
        lol curr = 0;
        int n;
        cin >> n;
        string s;
        cin >> s;
        int last = s.length() - 1;
        while (last && s[last] == '0')
            --last;
        for (int j = 0; j <= last; ++j)
        {
            if (curr < j)
            {
                ans += j - curr;
                curr += j - curr;
            }
            curr += s[j] - '0';
        }
        cout << "Case #" << i << ": " << ans << endl;
    }
}