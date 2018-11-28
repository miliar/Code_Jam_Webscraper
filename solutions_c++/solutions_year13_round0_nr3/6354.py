#include <iostream> 
#include <fstream>
#include <cmath>

using namespace std;

// Start includes & defs
bool pallindrome ( uint64_t num )
{
    uint64_t oNum = num;
    uint64_t rev = 0;
    while ( oNum > 0 ) 
    {
        int digit = oNum % 10;
        rev = rev*10 + digit;
        oNum /= 10;
    }
    return (rev == num);
}
// End include  & defs

int main (int argc, char** argv)
{
    ifstream read;
    read.open(argv[1]);

    ofstream write;
    write.open(argv[2]);

    int noOfTest = -1;
    read >> noOfTest;

    int n = 1;

    while ( n <= noOfTest )
    {
        // Start code ... 
        uint64_t start;
        uint64_t end;
        read >> start;
        read >> end;

        uint64_t count = 0;
        uint64_t startSqRt = ceil(sqrt(start));
        uint64_t startSq = startSqRt*startSqRt;

        while ( startSq <= end )
        {
            if ( pallindrome(startSqRt) and pallindrome(startSq) )
                ++count;
            startSq += 2*startSqRt + 1;
            ++startSqRt;
        }
        // End code ...
        write << "Case #" << n << ": " << count << endl;
        ++n;
    }

    read.close();
    write.close();
    return 0;
}
