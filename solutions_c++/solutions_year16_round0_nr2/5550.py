#include <cstdint>
#include <iostream>

using u64 = uint64_t;

u64 solve(const std::string& input) {
    u64 retVal = 0ul;

    bool is_face_up = input[0] == '+';
    for (u64 i = 0; i < input.size() - 1; ++i) {
        if (input[i] != input[i + 1])
        {
            is_face_up = !is_face_up;
            ++retVal;
        }
    }

    return is_face_up ? retVal : retVal + 1;
}

int main() {
    u64 total = 0ul;
    std::cin >> total;

    for (u64 number = 1ul; number <= total; ++number) {
        std::string stack;
        std::cin >> stack;

        std::cout << "Case #" << number
            << ": " << solve(stack) << std::endl;
    }
}
