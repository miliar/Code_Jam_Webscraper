#include <fstream>
#include <iostream>
#include <string>
#include <set>
#include <vector>

std::set<int> parseIntsFromString(const std::string& line, char breakChar)
{
    std::set<int> ret;

    int lastSpacePos = 0;
    while(true)
    {
         
        int nextSpacePos = line.find(breakChar, lastSpacePos);
        bool lastToken = ( nextSpacePos == std::string::npos );
        std::string token = line.substr(lastSpacePos, nextSpacePos-lastSpacePos);
        
        ret.insert( std::stoi(token) );

        lastSpacePos = nextSpacePos+1;
        if(lastToken)
        {
            return ret;
        }
    }
}

std::set<int> parseGrid(std::ifstream& input_stream)
{
    std::string line;
    getline(input_stream, line);
    int chosenRow = std::stoi(line);

    for(int row=0; row<chosenRow; ++row)
    {
        getline(input_stream, line);
    }
    
    auto row = parseIntsFromString(line, ' ');

    for(int row=chosenRow; row<4; ++row)
    {
        getline(input_stream, line);
    }
    return row;
}

//arg1: input file name
//arg2: output file name
int main(int argc, const char** argv)
{
    if(argc!=3)
    {
        std::cout << "Got " << argc << " arguments. Expected 2 arguments: input file name and output file name" << std::endl;
        return -1;
    }

    std::vector<std::set<int>> commonCards;    
    {
        std::ifstream input_stream(argv[1]);
        if (!input_stream.is_open())
        {
            std::cout << "Failed to open \"" << argv[1] << "\" for input." << std::endl;
            return -1;
        }
        
        std::string line;
        getline(input_stream, line);
        int numTestCases = std::stoi(line);        
        
        for(int i=0; i<numTestCases; ++i)
        {
            auto firstLine = parseGrid(input_stream);
            auto secondLine = parseGrid(input_stream);
            std::set<int> commonInts;
            for(auto number: firstLine)
            {
                if(secondLine.count(number))
                {
                    commonInts.insert(number);
                }
            }
            commonCards.emplace_back(std::move(commonInts));
        } 
    }

    {
        std::ofstream output_stream(argv[2]);
        if(!output_stream.is_open())
        {
            std::cout << "Failed to open \"" << argv[2] << "\" for output." << std::endl;
            return -1;
        }

        int caseNum = 1;
        for(const auto& testCase: commonCards)
        {
            std::string caseOutput;
            auto commonNum = testCase.size();
            if(commonNum > 1)
            {
                caseOutput = "Bad magician!";
            }else if (commonNum == 1)
            {
                caseOutput = std::to_string( *(testCase.begin()) );
            }else
            {
                caseOutput = "Volunteer cheated!";
            }

            output_stream << "Case #" << caseNum << ": " << caseOutput << "\n";

            ++caseNum;
        }
    }
    return 0;
}
