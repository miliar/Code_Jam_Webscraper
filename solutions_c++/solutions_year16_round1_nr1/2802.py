#include <bits/stdc++.h>

using i64 = long long;
using u64 = unsigned long long;
using u32 = unsigned;
using namespace std;

int main() {
    ifstream in("in.txt");
    ofstream out("out.txt");
    u64 T;
    in >> T;
    for (size_t u = 0; u < T; ++u) {
        string s;
        in >> s;
        list<char> ans;
        u64 len = s.length();
        ans.push_back(s[0]);
        for(size_t i = 1; i < len; ++i)
            if (ans.front() <= s[i])
                ans.push_front(s[i]);
            else
                ans.push_back(s[i]);
        out << "Case #" << u + 1 << ": ";
        for(auto i : ans)
            out << i;

        out << "\n";
    }
}