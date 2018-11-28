#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <fstream>
#include <algorithm>

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
            cases.push_back(caseReader.read(is));
        }
        
        return cases;
    }
};

class RevengeOfThePancakesCase
{
private:
    class Solver
    {
    public:
        Solver(const std::string& stack)
        {
            std::transform(begin(stack), end(stack), std::back_inserter(stack_), [](char c) -> bool {
               return c == '+';
            });
        }
        
        Solver(std::vector<bool> stack)
        : stack_(std::move(stack))
        {
        }
        
        Solver flip() const
        {
            auto flipped = stack_;
            std::reverse(begin(flipped), end(flipped));
            for (auto it = begin(flipped); it != end(flipped); ++it) {
                *it = !*it;
            }
            
            return Solver(std::move(flipped));
        }
        
        size_t solve(bool target = true) const
        {
            if (stack_.size() == 0) return 0;
            else {
                auto back = stack_.back();
                int i = 0;
                for (auto it = stack_.rbegin(); it != stack_.rend(); ++it, ++i) {
                    if (*it != back)
                        break;
                }
                auto end = std::begin(stack_);
                std::advance(end, stack_.size() - i);
                if (back == target)
                    return Solver(std::vector<bool>(std::begin(stack_), end)).solve();
                else
                    return Solver(std::vector<bool>(std::begin(stack_), end)).solve(back) + 1;
            }
        }
        
    private:
        std::vector<bool> stack_;
    };
    
public:
    RevengeOfThePancakesCase(std::string stack)
    : stack_(std::move(stack))
    {
    }
    
    std::string solve() const
    {
        return std::to_string(Solver(stack_).solve());
    }
    
private:
    std::string stack_;
};

class RevengeOfThePancakesCaseReader
{
public:
    RevengeOfThePancakesCase read(std::istream& is) const
    {
        std::string line;
        std::getline(is, line);
        std::istringstream iss(line);
        
        std::string stack;
        iss >> stack;
        
        return RevengeOfThePancakesCase(std::move(stack));
    }
};

int main(int argc, const char * argv[])
{
    if (argc < 2)
    {
        return 0;
    }
    
    std::ifstream ifs(argv[1]);
    
    auto cases = ProblemReader<RevengeOfThePancakesCase, RevengeOfThePancakesCaseReader>().read(ifs);
    
    for (auto i = 0; i < cases.size(); ++i) {
        std::cout << "Case #" << i + 1 << ": " << cases[i].solve() << "\n";
    }
    return 0;
}
