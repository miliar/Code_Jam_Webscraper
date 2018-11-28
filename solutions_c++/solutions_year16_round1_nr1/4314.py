#include <bits/stdc++.h>
using namespace std;

string inp;
deque<char> ans;

int main() {
    int tt;
    cin >> tt;
    for (int cas = 1; cas <= tt; ++cas) {
        cin >> inp;
        ans.clear();
        for (char ch: inp)
            if (!ans.size())
                ans.push_back(ch);
            else if (ans.front() <= ch)
                ans.push_front(ch);
            else
                ans.push_back(ch);
        string out;
        for (char ch: ans)
            out.push_back(ch);
        cout << "Case #" << cas << ": ";
        cout << out << endl;
    }
}
