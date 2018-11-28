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
        u64 K, C, S;
        input >> K >> C >> S;

        output << "Case #" << i + 1<< ": ";
        for(size_t i = 1; i <= S; ++i)
            output << i << " ";
        output << "\n";
    }

    return 0;
}