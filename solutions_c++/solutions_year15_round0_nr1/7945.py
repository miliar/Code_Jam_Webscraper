#include <iostream>
#include <fstream>
#include <cstdio>
#include <cassert>
#include <sstream>
#include <typeinfo>

int TestFunc(int level_max, const std::string s_level) {
    int total_counter = 0;
    int friend_num = 0;
    for (auto i = 0; i <= level_max; ++i) {
        const char num_str = s_level.at(i);
        int num = std::stoi(&num_str);

        if (!(total_counter >= i)) {
            friend_num    += i - total_counter;
            total_counter += i - total_counter;
        }

        total_counter += num;
    }

    return friend_num;
}

int main(int argc, char * argv[])
{
    assert(argc > 1);

    std::ifstream in(argv[1]);
    assert(in.is_open());

    std::ofstream out(argv[2]);
    assert(out.is_open());

    std::string line;
    std::getline(in, line);

    auto case_num = std::stoi(line);

    std::cout << case_num << std::endl;

    for (int num = 1; num <= case_num; ++num) {
        std::string level_max_str;
        in >> level_max_str;
        auto level_max = std::stoi(level_max_str);

        std::string s_level;
        in >> s_level;

        auto ans = TestFunc(level_max, s_level);
        out << "Case #" << num << ": " << ans << std::endl;
    }

    return 0;
}
