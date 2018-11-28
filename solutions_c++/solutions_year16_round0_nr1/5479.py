#include <cstdint>
#include <iostream>

using u32 = uint32_t;

u32 to_bitfield(u32 input) {
    u32 retVal = 0;
    while (input >= 10) {
        retVal |= (1u << input % 10);
        input /= 10;
    }
    retVal |= (1u << input);
    return retVal;
}

u32 count_sheep(u32 n) {
    u32 numbers_seen = 0u;
    u32 last_used = 0u;
    for (u32 i = 1u; i <= 10000000u && numbers_seen != 1023u; ++i) {
        numbers_seen |= to_bitfield(last_used = i * n);
    }
    return numbers_seen == 1023u ? last_used : 0u; 
}

void run_case(u32 number, u32 input) {
    std::cout << "Case #" << number << ": ";
    auto result = count_sheep(input);
    if (result) {
        std::cout << result << std::endl;
    } else {
        std::cout << "INSOMNIA" << std::endl;
    }
}

int main() {
    u32 total = 0;
    std::cin >> total;

    for (u32 number = 1; number <= total; ++number) {
        u32 input;
        std::cin >> input;

        run_case(number, input);
    }
}
