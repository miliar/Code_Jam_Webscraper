
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false); cin.tie(0);
    int T,ntest=1;
    string s;
    deque<char> dq;
    cin >> T;
    while(T--)
    {
        cin >> s;
        dq.clear();
        dq.push_back(s[0]);
        for(int i = 1; i < s.size(); i++)
            if(s[i] < dq.front())
                dq.push_back(s[i]);
            else
                dq.push_front(s[i]);

        cout << "Case #" << ntest++ << ": ";
        while(!dq.empty())
        {
            cout << dq.front();
            dq.pop_front();
        }
        cout << '\n';
    }
    return 0;
}