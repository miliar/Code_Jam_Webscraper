#include <bits/stdc++.h>>

using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int t;
    cin >> t;

    for(int i=0; i<t; i++)
    {
        string s;
        cin >> s;

        int k=0;
        for(int j=1; j<s.length(); j++)
        {
            if(s[j]!=s[j-1])
                k++;
        }
        if(s[s.length()-1] == '-')
            k++;

        cout << "Case #" << i+1 << ": " << k << endl;
    }
}
