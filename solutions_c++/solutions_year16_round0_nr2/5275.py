#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define F first
#define S second

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int h=0; h<t; h++)
    {
        string s;
        cin >> s;
        s += '#';
        int k = 0;
        for (int i=0; i<s.length()-1; i++)
        {
            if (s[i] != s[i+1])
                k++;
            if (s[i+1] == '#'  && s[i] == '+')
                k --;
        }
        cout << "Case #" << h+1 << ": " << k << endl;
    }
    return 0;
}
