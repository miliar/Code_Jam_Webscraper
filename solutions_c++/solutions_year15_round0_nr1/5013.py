#include <fstream>
#include <cctype>
using namespace std;

int main(int argc, char * argv[])
{
    ifstream infile("opera.in");
    ofstream outfile("opera.out", ios_base::out | ios_base::trunc);
    
    unsigned int numCases, numLevels, numStanding, numInvited, invite, sample, level;
    char c;
    infile >> numCases;
    for (sample = 1; sample <= numCases; sample++)
    {
        numStanding = numInvited = 0;
        infile >> numLevels;
        for (level = 0; level <= numLevels; infile.get(c))
            if (isdigit(c))
            {
                invite = (c > 0x30 && numStanding < level) ? level - numStanding : 0;
                numInvited += invite;
                numStanding += (static_cast<int>(c) - 0x30) + invite;
                level++;
            }
        outfile << "Case #" << sample << ": " << numInvited << endl;
    }
    
    return 0;
}