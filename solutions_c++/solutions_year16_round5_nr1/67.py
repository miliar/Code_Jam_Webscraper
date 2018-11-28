#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main()
{
    int t, ct;
 
    ios::sync_with_stdio(false);

    cin >> t;
    for (ct = 1; ct <= t; ct++)
    {
        string s;

        cin >> s;

        stack<char> st;
        for (char c : s)
        {
            if (st.empty())
            {
                st.push(c);
            }
            else if (st.top() == c)
            {
                st.pop();
            }
            else
            {
                st.push(c);
            }
        }

        cout << "Case #" << ct << ": " << s.size() * 5 - st.size() / 2 * 5 << endl;
    }

    return 0;
}
