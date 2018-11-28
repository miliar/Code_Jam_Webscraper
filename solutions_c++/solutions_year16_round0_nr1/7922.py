#include <iostream>
#include <string>
#include <sstream>
#include <bitset>
#include <vector>
#include <fstream>

int readNumberOfCases(std::istream& is)
{
    std::string line;
    std::getline(is, line);
    std::istringstream iss(line);
    int numberOfCases = 0;
    iss >> numberOfCases;
    return numberOfCases;
}

template <typename CaseType, typename CaseReaderType>
class ProblemReader
{
public:
    std::vector<CaseType> read(std::istream& is) const
    {
        std::string line;
        std::getline(is, line);
        std::istringstream iss(line);
        
        size_t numberOfCases = 0;
        iss >> numberOfCases;
        
        std::vector<CaseType> cases;
        cases.reserve(numberOfCases);
        
        CaseReaderType caseReader;
        for (auto i = 0; i < numberOfCases; ++i) {
            cases.emplace_back(caseReader.read(is));
        }
        
        return cases;
    }
};

class CountingSheepCase
{
public:
    uint64_t number;
};

class CountingSheepCaseReader
{
public:
    CountingSheepCase read(std::istream& is) const
    {
        std::string line;
        std::getline(is, line);
        std::istringstream iss(line);
        
        CountingSheepCase c;
        iss >> c.number;
        
        return c;
    }
};

int main(int argc, const char * argv[])
{
    if (argc < 2)
    {
        return 0;
    }
    
    std::ifstream ifs(argv[1]);
    
    auto cases = ProblemReader<CountingSheepCase, CountingSheepCaseReader>().read(ifs);
    
    for (auto i = 0; i < cases.size(); ++i) {
        auto& c = cases[i];
        
        if (c.number == 0) {
            std::cout << "Case #" << i + 1 << ": INSOMNIA\n";
        } else {
            std::bitset<10> occurence;
            auto lastNumber = 0;
            
            while (!occurence.all()) {
                lastNumber += c.number;
                auto testNumber = lastNumber;
                while (testNumber != 0) {
                    occurence.set(testNumber % 10);
                    testNumber /= 10;
                }
            }
            
            std::cout << "Case #" << i + 1 << ": " << lastNumber << "\n";
        }
    }
    return 0;
}
