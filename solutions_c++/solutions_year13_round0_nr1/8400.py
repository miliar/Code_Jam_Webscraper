#include <string>
#include <vector>
#include <fstream>

class SharedIO
{

public:
    SharedIO(const std::string& problemname);
    ~SharedIO();

    size_t ReadNumTestCases();

    std::vector<double>                     ReadTestCaseDoubles();
    std::vector<std::vector<double> >       ReadTestCaseDoubleLists();
    std::vector<int>                        ReadTestCaseInts();
    std::vector<std::vector<int> >          ReadTestCaseIntLists();
    std::vector<unsigned int>               ReadTestCaseUInts();
    std::vector<std::vector<unsigned int> > ReadTestCaseUIntLists();
    std::vector<std::string>                ReadTestCaseStrings();

    void WriteTestCase(std::string output);

private:
    std::ifstream infile_;
    std::ofstream outfile_;

    size_t numTestCases_;
    size_t outputCaseNumber_;
};