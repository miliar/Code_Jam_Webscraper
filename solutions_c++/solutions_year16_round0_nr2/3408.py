#include <bits/stdc++.h>
using i64 = long long;
using u64 = unsigned long long;
using u32 = unsigned;
using namespace std;
int main() {
    ios::sync_with_stdio(false);

    ofstream output("out.txt");
    ifstream input("in.txt");
    assert(output.is_open() && input.is_open());
    u64 T;
    input >> T;

    for(size_t i = 0; i < T; ++i){
        string s;
        input >> s;
        bool flip = false;
        u64 cnt = 0;
        for(i64 i = s.length() - 1; i >= 0; --i) {
            if (i - 1 >= 0 && s[i - 1] == s[i])
                continue;
            if (!flip && s[i] == '-' || flip && s[i] == '+') {
                flip = !flip;
                cnt++;
            }
        }
        output << "Case #" << i + 1<< ": " << cnt << "\n";
    }

    return 0;
}