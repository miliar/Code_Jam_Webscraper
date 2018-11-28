#include <iostream>
#include <string>
#include <stack>
using namespace std;

stack<pair<char, int>> st;

int main()
{
    int t, kase = 0;
    cin >> t;
    while (t--)
    {
        string s;
        cin >> s;
        while (!st.empty()) st.pop();
        bool shouldPop = false;
        int totScore = 0;
        for (int i = 0; i < s.size(); i++)
        {
            int remaining = s.size() - i;
            if (remaining == st.size())
                shouldPop = true;
            if (shouldPop)
            {
                auto p = st.top();
                st.pop();
                if (s[i] == p.first)
                    totScore += p.second;
                else
                    totScore += p.second - 5;
            }
            else
            {
                if (st.empty() || s[i] != st.top().first)
                    st.emplace(s[i], 10);
                else
                {
                    auto p = st.top();
                    st.pop();
                    if (s[i] == p.first)
                        totScore += p.second;
                    else
                        totScore += p.second - 5;
                }
            }
        }
        cout << "Case #" << ++kase << ": " << totScore << endl;
    }
    return 0;
}