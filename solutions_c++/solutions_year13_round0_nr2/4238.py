
#include <iostream>
#include <fstream>
#include <map>
#include <vector>

int main(int argc, char *argv[])
{
    std::string testcase ("/home/gquerol/Test/B-large");
    std::string inputfile = testcase + ".in";
    std::string outputfile = testcase + ".out";

    std::ifstream input(inputfile.c_str());
    std::ofstream output(outputfile.c_str(), std::ios_base::out & std::ios_base::trunc);

    std::cout << "reading " << inputfile << std::endl;


    int nbTests;
    input >> nbTests;
    for (int testIdx = 1; testIdx < nbTests + 1; ++testIdx)
    {
        std::cout << "solving testcase #" << testIdx << std::endl;
        int linecount;
        int columncount;

        input >> linecount;
        input >> columncount;

        std::vector<std::vector<int> > patternHeight;
        patternHeight.resize(linecount);
        for(int line = 0; line < linecount; ++line)
        {
            patternHeight[line].resize(columncount);
            for (int column = 0; column < columncount; ++column)
            {
                input >> patternHeight[line][column];
            }
        }

        std::vector<int> maxforithLine;
        std::vector<int> maxforithColumn;
        maxforithLine.resize(linecount);
        maxforithColumn.resize(columncount);

        // compute max height of each line
        for(int line = 0; line < linecount; ++line)
        {
            maxforithLine[line] = 0;
            for (int column = 0; column < columncount; ++column)
            {
                maxforithLine[line] = std::max(maxforithLine[line], patternHeight[line][column]);
            }
        }

        for (int column = 0; column < columncount; ++column)
        {
            maxforithColumn[column] = 0;
            // compute max height of each column
            for(int line = 0; line < linecount; ++line)
            {
                maxforithColumn[column] = std::max(maxforithColumn[column], patternHeight[line][column]);
            }
        }

        bool ok = true;

        // compute max height of each line
        for(int line = 0; line < linecount; ++line)
        {
            for (int column = 0; column < columncount; ++column)
            {
                ok &= patternHeight[line][column] >= maxforithColumn[column]
                   ||  patternHeight[line][column] >= maxforithLine[line];
                if (!ok)
                    break;
            }
            if (!ok)
                break;
        }

        std::cout << "Case #" << testIdx << ": " << (ok ? "YES" : "NO") << std::endl;
        output << "Case #" << testIdx << ": " << (ok ? "YES" : "NO") <<  std::endl;

        std::cout << "end solving testcase #" << testIdx << std::endl;
    }


    std::cout << "writing " << outputfile << std::endl;
}
