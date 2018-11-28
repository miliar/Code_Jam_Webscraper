#include <iostream>
#include <fstream>
#include <array>
using namespace std;

int main()
{
    std::ifstream input{"D:\\input.txt"};
    std::ofstream output{"D:\\output.txt"};
    int testCases = 0;
    int i = 0;
    int N;
    std::array<bool, 10> seq = {false};
    input >> testCases;
    auto printi = [&i, &output] (int n) -> void { output << "Case #" << i + 1 << ": " << n << "\n"; };
    auto prints = [&i, &output] (std::string s) -> void { output << "Case #" << i + 1 << ": " << s << "\n"; };
    auto cleanArray = [&seq] (void) -> void { for(int i = 0; i < 10; i++) seq[i] = false; };
    auto checkArray = [&seq] (void) -> bool { for(int i = 0; i < 10; i++)
            if(seq[i] == false) return false; return true; };
    while (input >> N) {
        cleanArray();
        if (N == 0) {
            prints("INSOMNIA");
            i++;
            continue;
        }
        int steps = 0;
        for (long long k = N; ; k = k + N)
        {
            ++steps;
            int number = k;
            while(number > 0) {
                int mod = number % 10;
                seq[mod] = true;
                number = number - mod;
                number = number / 10;

            }
            if(checkArray() == true) {
                printi(k);
                break;
            }
            if(steps == 100) {
                prints("INSOMNIA");
                break;
            }
        }
        i++;
    }
}

