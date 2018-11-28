#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <unordered_map>
#include <set>
#include <cstdint>

using namespace std;

#define debug(...) fprintf(stderr, __VA_ARGS__)
//#define debug(format, ...)

int main(int argc, char* argv[])
{
    string inputFile = "input.in";
    string outputFile = "output.out";

    if (argc >= 3) {
        inputFile = argv[1];
        outputFile = argv[2];
        debug("Using inputFile \"%s\" and outputFile \"%s\"\n", inputFile.c_str(), outputFile.c_str());
    }

    freopen(inputFile.c_str(), "r", stdin);
    freopen(outputFile.c_str(), "w", stdout);

    int tc;
    cin >> tc;

    debug("CounterSheep with %d test cases\n", tc);
    for (int n = 1; n <= tc; ++n) {
        string solution;
        set<char> numberSet;
        int insomniaNumbers = 0;
        int insomniaTimes = 0;
        int insomniaLimit = 100;

        uint64_t number;
        cin >> number;

        int times = 0;
        while (true) {
            times++;
            uint64_t sheeps = times * number;
            string sheepsStr = to_string(sheeps);
            for (unsigned i=0; i < sheepsStr.length(); ++i) {
                numberSet.insert(sheepsStr.at(i));
            }

            int numbers = numberSet.size();

            /*string numberSetStr;
            for (auto it = numberSet.begin(); it != numberSet.end(); it++) {
                numberSetStr += *it;
            }
            debug("Case #%d: Times %d, sheeps %llu, numberSet.size() %d, insomniaNumbers %d, numberSet %s\n",
                  n, times, sheeps, numbers, insomniaNumbers, numberSetStr.c_str());*/

            if (numbers == 10) {
                char buffer[128];
                sprintf(buffer, "%llu", sheeps);
                solution = buffer;
                break;
            } else if (insomniaNumbers != numbers) {
                insomniaNumbers = numbers;
                insomniaTimes = 0;
            } else {
                if (++insomniaTimes >= insomniaLimit) {
                    solution = "INSOMNIA";
                    break;
                }
            }
        };

        printf("Case #%d: %s\n", n, solution.c_str());
    }

    return 0;
}
