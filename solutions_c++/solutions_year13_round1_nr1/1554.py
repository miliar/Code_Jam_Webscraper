#include <fstream>
#include <sstream>
#include <string>
#include <cstdio>
#include <cstdlib>

int
solve(
    const long r,
    const long t
)
{
    int retval(0);
    long amount(t);
    long radius(r);
    long white(r*r);
    while (true)
    {
        long painted = (radius + 1)*(radius + 1) - white;
        amount -= painted;
        if (amount >= 0)
        {
            retval++;
        }
        else
        {
            break;
        }
        
        radius += 2;
        white = radius*radius;
    }   // while
    return retval;
}   // solve


int
main(
    int argc,
    char *argv[]
)
{
    std::ifstream inFile(argv[1]);
    
    std::string line;
    std::getline(inFile, line);
    int caseCount(atoi(line.c_str()));
    
    for (int i = 1; i <= caseCount; ++i)
    {
        std::getline(inFile, line);
        std::istringstream lineStream(line);
        long r, t;
        lineStream >> r >> t;
        
        printf("Case #%d: %d\n", i, solve(r, t));
    }   // for
}   // main
