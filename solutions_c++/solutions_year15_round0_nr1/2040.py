#include <fstream>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
//#include <cstdlib>

int casenum;
std::vector<std::vector<int> > testcase;
std::vector<int> result;

bool readinput(std::string & filename)
{
    std::ifstream in(filename);
    if(!in)
    {
        std::cout << "Can't read in input file\n";
        return false;
    }
    in >> casenum;
    int maxskynum;
    std::string skylist;
    testcase.resize(casenum);
    for(unsigned i = 0; i < casenum; ++i)
    {
        in >> maxskynum;
        testcase[i].resize(maxskynum+1);
        in >> skylist;
        for(unsigned j = 0; j < maxskynum+1; ++j)
        {
            testcase[i][j] = (int)(skylist[j] - '0');
        }
    }  
    return true;
}

bool writeoutput(std::string & filename)
{
    std::ofstream out(filename);
    if(!out)
    {
        std::cout << "Can't open the output file\n";
        return false;
    }
    for(unsigned i = 0; i < casenum; ++i)
    {
        out << "Case #" << i+1 << ": " << result[i] << std::endl;
    }
    return true;

}
int ovation(std::vector<int> & testcase)
{
    if(testcase.size() == 0)
    {
        std::cout<< "testcase size is 0\n";
        return -1;
    }
    
    int addnum = 0;
    int standnum = testcase[0];
    
    for(int i = 1; i < testcase.size(); ++i)
    {
        if(standnum < i)
        {
            addnum = std::max(addnum,i - standnum);
        }
        standnum += testcase[i];
    }
    return addnum;
        
}

int main(int argc, char ** argv)
{
    std::string fn = argv[1];
    std::string output = argv[2];
    readinput(fn);
    result.resize(casenum);
    for(unsigned i = 0; i < casenum; ++i)
    {
        result[i] = ovation(testcase[i]);
    }
    writeoutput(output);
}