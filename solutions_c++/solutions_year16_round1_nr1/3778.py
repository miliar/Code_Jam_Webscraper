#include <stdio.h>
#include <stdint.h>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

void solve(int T) {
    std::string S;
    std::cin >> S;
    std::string Maxer = S;
    std::string SS = S;
    char tmp = Maxer[0];
    size_t len = S.size();
    for (size_t i = 1; i < len; ++i) {
        if (tmp < Maxer[i]) {
            tmp =  Maxer[i];
        }
        Maxer[i] = tmp;
    }

    std::reverse(S.begin(), S.end());
    std::reverse(Maxer.begin(), Maxer.end());
    std::string op, ret;
    for (size_t i = 0; i < len - 1; ++i) {
        if (S[i] >= Maxer[i+1]) {
            op.append(1, 'b');
        } else {
            op.append(1, 'a');
        }
    }
    std::reverse(op.begin(), op.end());

    ret.append(1, SS[0]);
    for (size_t i = 1; i < len; ++i) {
        if (op[i-1] == 'a') {
            ret.append(1, SS[i]);
        } else {
            ret = std::string(1, SS[i]) + ret;
        }
    }

    std::cout << "Case #" << T << ": " << ret << std::endl;
}

int main(int argc, char* argv[]) {
    int T;
    std::cin >> T;
    for (int i = 0; i < T; ++i) {
        solve(i + 1);
    }
    return 0;
}
