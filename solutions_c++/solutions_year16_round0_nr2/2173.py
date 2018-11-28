#include <QCoreApplication>

#include <fstream>
#include <array>
#include <cstdint>

int main(int argc, char *argv[]) {
    std::ifstream in("in.txt");
    std::ofstream out("out.txt");

    int T;
    in >> T;
    for (int i = 1; i <= T; ++i) {
        std::string str;
        in >> str;
        size_t last = 0;
        std::reverse(str.begin(), str.end());
        int turns = 0;
        last = str.find('-');
        while (last != std::string::npos) {
            bool plus = false;
            int j = 1;
            while (str[str.size() - j] == '+') {
                str[str.size() - j] = '-';
                plus = true;
                ++j;
            }
            if (plus)
                turns++;
            for (size_t j = last; j < str.size(); ++j)
                if (str[j] == '+')
                    str[j] = '-';
                else
                    str[j] = '+';
            std::reverse(str.begin() + last, str.end());
            ++turns;
            last = str.find('-', last);
        }
        out << "Case #" << i << ": " << turns << std::endl;
    }
    return 0;
}
