#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    std::ifstream input{"D:\\input.txt"};
    std::ofstream output{"D:\\output.txt"};
    int testCases = 0;
    std::string pancakes;
    int i = 0;
    input >> testCases;
    auto printi = [&i, &output] (int n) -> void { output << "Case #" << i + 1 << ": " << n << "\n"; };
    while(input >> pancakes) {
        std::cout << pancakes << std::endl;
        int result = 1;
        auto last = pancakes[0];
        for(auto c : pancakes) {
            if(c != last) ++result;
            last = c;
        }
        if(last == '+') --result;
        printi(result);
        i++;
    }
}

