#include <fstream>
#include <iostream>
#include <cstdint>

using namespace std;

int main(int argc, char *argv[])
{
    if (argc != 2) {
        cerr << "Expected 1 argument" << endl;
        return 1;
    }

    ifstream infile(argv[1]);

    if (infile == NULL) {
        cerr << "Could not open file " << argv[1] << " for reading" << endl;
        return 1;
    }

    ofstream outfile("output.txt");

    if (outfile == NULL) {
        cerr << "Could not open file output.txt for writing" << endl;
        return 1;
    }

    int casesNumber;
    infile >> casesNumber; //get the number of cases
    infile.seekg(1, infile.cur); //get past the newline

    for (int caseNumber = 0; caseNumber < casesNumber; caseNumber++) {
        outfile << "Case #" << caseNumber+1 << ": ";

        uint32_t shynessLevelsCount;
        infile >> shynessLevelsCount;
        shynessLevelsCount++;

        infile.seekg(1, infile.cur);//get past the space

        uint32_t humansCount = 0;
        uint32_t humansNeeded = 0;

        for (uint32_t curShynessLevel = 0; curShynessLevel < shynessLevelsCount; curShynessLevel++) {

            char curHumanCountChar;
            infile.get(curHumanCountChar);
            int curHumanCount = curHumanCountChar - '0';

            if (curHumanCount == 0) {
                continue;
            }

            int32_t curHumansNeeded = curShynessLevel - humansCount;
            humansCount += curHumanCount;
            if (curHumansNeeded > 0) {
                //add the needed HOOMANS to reach that shyness lvl
                humansNeeded += curHumansNeeded;
                humansCount += curHumansNeeded;
            }
        }

        outfile << humansNeeded;

        if (caseNumber != casesNumber-1) {
            //if not the last case, add newline
            outfile << endl;
        }
    }

    infile.close();
    outfile.close();

    return 0;
}
