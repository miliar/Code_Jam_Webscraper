#include <iostream>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    for(int tt = 0; tt < t; ++tt)
    {
        string s;
        cin >> s;
        int w = 0;
        for(int i = 1; i < s.size(); ++i)
            w += (s[i-1]!=s[i]);
        w += (s[s.size()-1] == '-');
        cout << "Case #" << tt+1 << ": " << w << endl;
    }
    return 0;
}
