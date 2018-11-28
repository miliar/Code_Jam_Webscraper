#include <iostream>
#include <set>
#include <string.h>
#define lli long long int
using namespace std;

int solve(string);

int main()
{
    int t;
    cin >> t;
    int case1 = 0;
    while(t--)
    {
        case1++;
        string s;
        cin >> s;
        cout << "Case #" << case1 << ": " << solve(s) << endl;
    }
    return 0;
}

int solve(string s)
{
    int count = 0;
    if (s[0] == '-')
        count++;
    for (int i = 1 ; i < s.size() ; i++) {
        if (s[i] != s[i-1] && s[i] == '-')
            count +=2;
    }
    return count;
}
