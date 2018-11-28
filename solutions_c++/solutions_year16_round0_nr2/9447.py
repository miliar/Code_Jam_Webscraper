#include <iostream>
#include <vector>
#include <string>


std::vector<bool> readTest() {
    std::vector<bool> vec;
    vec.clear();
    std::string S;
    std::cin >> S;
    vec.resize(S.size());
    for (size_t i = 0; i < S.size(); ++i) {
        if (S[i] == '-')
            vec[i] = false;
        else
            vec[i] = true;
    }
    return vec;
}


int solve() { 
    std::vector<bool> vec = readTest(), a, b; 
    int res = 0;

    for (int i = 0; i < vec.size() - 1; ++i)
    {
        if (vec[i] != vec[i+1])
            ++res;
    }
    
    if (vec.back()==false)
        ++res;

    return res;
}

int main() {
    int q;
    std::cin >> q;

    for (int i = 1; i <= q; ++i)
        std::cout << "Case #" << i << ": " << solve() << "\n";

    return 0;
}
