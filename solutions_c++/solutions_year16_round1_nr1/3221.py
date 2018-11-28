#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>

using namespace std;
vector <char> front, back;

int main()
{
    ios::sync_with_stdio(false);
    string s;
    char m;
    int t;
    cin >> t;
    for(int cases = 1;cases <= t;++cases)
    {
        cin >> s;
        m = -1;
        front.clear();
        back.clear();
        for(int i = 0;i < s.length();++i)
        {
            if(s[i] >= m)
            {
                front.push_back(s[i]);
                m = s[i];
            }
            else
            {
                back.push_back(s[i]);
            }
        }
        reverse(front.begin(), front.end());
        cout << "Case #" << cases << ": ";
        for(int i = 0;i < front.size();++i)
            cout << front[i];
        for(int i = 0;i < back.size();++i)
            cout << back[i];
        cout << endl;
    }
    return 0;
}
