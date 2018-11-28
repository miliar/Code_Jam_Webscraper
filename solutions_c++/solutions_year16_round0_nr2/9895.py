#include <iostream>

using namespace std;

// Find continuous blocks of same side, treat them as one

int compute(string s)
{
    int l = s.length();
    
    char current = s[0];
    int flips = 0;
    
    for (int i = 1; i < l; i++)
    {
        if(s[i] != current)
        {
            current = s[i];
            flips++;
        }
    }

    return current == '+' ? flips : flips + 1;
}

int main()
{
    int t;
    string s;

    cin >> t;

    for(int i = 0; i < t; i++)
    {
        cin >> s;
        cout << "Case #" << i+1 << ": " << compute(s) << endl;
    }

    return 0;
}
