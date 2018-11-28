#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <utility>
#include <string>

using namespace std;

template<typename T>
T next() { T tmp; cin >> tmp; return tmp; }

void solve() {
    string data = next< string >() + "+";
    int result = 0;
    for (size_t i = 0; i < data.size() - 1; ++i) {
        result += data[i] != data[i + 1] ? 1 : 0;
    }
    cout << result << endl;
}

int main() {
    int n = next< int >();
    for (int i = 1; i <= n; ++i) {
        cout << "Case #" << i << ": ";
        solve();
    }

    return 0;
}
