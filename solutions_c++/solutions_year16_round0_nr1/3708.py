#include <iostream>
#include <string>

using namespace std;

bool seen[11];

bool end() {
    for(auto i = 0u; i < 10; i++) {
        if(not seen[i]) 
            return false;
    }
    return true;
}

void solve()
{
    unsigned int n;

    for(auto i = 0u; i < 10; i++)
        seen[i] = false;

    cin >> n;
    int ans = 0;
    if(n == 0) {
        cout << "INSOMNIA";
    } else {
        auto i = n;
        for(; not end(); i += n) {
            auto s = to_string(i);
            for(auto j = 0u; j < s.size(); j++) {
                seen[s[j] - '0'] = true;
            }
        }
        cout << i - n;
    }
}

int main()
{
    unsigned int cases;
    cin >> cases;
    for(auto i = 1u; i <= cases; i++) {
        cout << "Case #" << i << ": ";
        solve();
        cout << endl;
    }
    return 0;
}
