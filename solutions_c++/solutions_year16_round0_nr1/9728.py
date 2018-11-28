#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <fstream>

using namespace std;

std::string countingSheep(long N);

int main() {
    int numTestCases;
    long N;
    std::ifstream infile("large_input.txt");
    infile >> numTestCases;
    int coutadjuster = 1;
    do
    {
    infile >> N;
    cout << "Case #" << coutadjuster++ << ": " << countingSheep(N) << endl;
    }
    while(coutadjuster <= numTestCases);
    return 0;
}

std::string countingSheep(long N)
{
    std::vector<int> digits = {0,1,2,3,4,5,6,7,8,9};
    if(N == 0)
    {
        return "INSOMNIA";
    }
    long multiplier = 1;
    while(digits.size() != 0)
    {
        long long result = multiplier * N;
        std::ostringstream intStream;
        intStream << result;
        std::string intString(intStream.str());
        std::string returnResult(intString);
        std::for_each(intString.begin(), intString.end(), [&digits](char c){
            auto iter = std::find(digits.begin(), digits.end(), c - '0');
            if(iter != digits.end())
            {
                digits.erase(iter);
            }
        });

        if(digits.size() == 0)
        {
            return returnResult;
        }
        multiplier++;
    }
}