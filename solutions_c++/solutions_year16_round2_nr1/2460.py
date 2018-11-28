#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;
int A[30];

int count(int x)
{
    int ans = 0;
    if(x == 0)
    {
        ans = min(A['Z' - 'A'], min(A['E'-'A'], min(A['R' - 'A'], A['O' - 'A'])));
        A['Z'-'A'] -= ans;
        A['E'-'A'] -= ans;
        A['R'-'A'] -= ans;
        A['O'-'A'] -= ans;
    }
    if(x == 1)
    {
        ans = min(A['O' - 'A'], min(A['N'-'A'], A['E' - 'A']));
        A['E'-'A'] -= ans;
        A['N'-'A'] -= ans;
        A['O'-'A'] -= ans;
    }
    if(x == 2)
    {
        ans = min(A['T' - 'A'], min(A['W'-'A'], A['O' - 'A']));
        A['T'-'A'] -= ans;
        A['W'-'A'] -= ans;
        A['O'-'A'] -= ans;
    }
    if(x == 3)
    {
        ans = min(A['T' - 'A'], min(A['E'-'A'] / 2, min(A['R' - 'A'], A['H' - 'A'])));
        A['T'-'A'] -= ans;
        A['E'-'A'] -= 2*ans;
        A['R'-'A'] -= ans;
        A['H'-'A'] -= ans;
    }
    if(x == 4)
    {
        ans = min(A['F' - 'A'], min(A['U'-'A'], min(A['R' - 'A'], A['O' - 'A'])));
        A['F'-'A'] -= ans;
        A['U'-'A'] -= ans;
        A['R'-'A'] -= ans;
        A['O'-'A'] -= ans;
    }
    if(x == 5)
    {
        ans = min(A['F' - 'A'], min(A['E'-'A'], min(A['I' - 'A'], A['V' - 'A'])));
        A['F'-'A'] -= ans;
        A['E'-'A'] -= ans;
        A['I'-'A'] -= ans;
        A['V'-'A'] -= ans;
    }
    if(x == 6)
    {
        ans = min(A['S' - 'A'], min(A['I'-'A'], A['X' - 'A']));
        A['S'-'A'] -= ans;
        A['I'-'A'] -= ans;
        A['X'-'A'] -= ans;
    }
    if(x == 7)
    {
        ans = min(A['S' - 'A'], min(A['E'-'A'] / 2, min(A['V' - 'A'], A['N' - 'A'])));
        A['S'-'A'] -= ans;
        A['E'-'A'] -= 2*ans;
        A['V'-'A'] -= ans;
        A['N'-'A'] -= ans;
    }
    if(x == 8)
    {
        ans = min(A['I' - 'A'], min(A['E'-'A'], min(A['G' - 'A'], min(A['H' - 'A'], A['T'-'A']))));
        A['E'-'A'] -= ans;
        A['I'-'A'] -= ans;
        A['G'-'A'] -= ans;
        A['H'-'A'] -= ans;
        A['T' - 'A'] -= ans;
    }
    if(x == 9)
    {
        ans = min(A['N' - 'A'] / 2, min(A['E'-'A'], A['I' - 'A']));
        A['N'-'A'] -= 2*ans;
        A['E'-'A'] -= ans;
        A['I'-'A'] -= ans;
    }
    return ans;
}

int main()
{
    int t, x, a[] = {6, 0, 4, 3, 2, 5, 7, 8, 9, 1};
    string s;
    cin >> t;
    for(int cases = 1;cases <= t;++cases)
    {
        cin >> s;
        memset(A, 0, sizeof(A));
        for(int i = 0;i < s.length();++i)
            A[s[i] - 'A']++;
        cout << "Case #" << cases << ": ";
        string s1 = "";
        for(int i = 0;i < 10;++i)
        {
            x = count(a[i]);

            for(int j = 0;j < x;++j)
                s1 += (char)(a[i] + '0');
        }
        sort(s1.begin(), s1.end());
        cout << s1 << endl;
    }
    return 0;
}
