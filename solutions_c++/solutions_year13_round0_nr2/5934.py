
#include <fstream>
#include <string>
#include <sstream>
#include <iostream>
#include <cstdlib>


int main()
{
    std :: string filenamePrefix = "B-large";
    // open input file and create and open output file (destroys old one first)
    std :: fstream inFile, outFile;
    inFile.open((filenamePrefix + ".in").c_str(), std :: ios :: in);
    outFile.open((filenamePrefix + ".out").c_str(), std :: ios :: out | std :: ios :: trunc);

    if(!inFile)
    {
        std :: cout << "Could not open input file: \"" << filenamePrefix + ".in" << "\".";
        exit(1);
    }

    if(!outFile)
    {
        inFile.close();
        std :: cout << "Could not open output file: \"" << filenamePrefix + ".out" << "\".";
        exit(1);
    }



    // obtain number of cases
    int testCaseCount = 0;
    inFile >> testCaseCount;
    for(int testCase = 1; testCase <= testCaseCount; testCase ++)
    {
        if(testCase != 1)
            outFile << std :: endl;

        // dump "Case #x: " to the output file line
        outFile << "Case #" << testCase << ": ";

        // obtain dimensions
        int rowCount = 0, columnCount = 0;
        inFile >> rowCount;
        inFile >> columnCount;

        // allocate space to hold relevant data
        int totalCount = rowCount * columnCount;
        int* heights = new int[totalCount];
        int* rowMax = new int[rowCount];
        int* columnMax = new int[columnCount];

        // initialize max value arrays to 0
        for(int a = 0; a < rowCount; a ++)
            rowMax[a] = 0;
        for(int a = 0; a < columnCount; a ++)
            columnMax[a] = 0;


        // obtain height values
        for(int row = 0; row < rowCount; row ++)
        {
            for(int column = 0; column < columnCount; column ++)
            {
                int value = 0;
                inFile >> value;
                heights[row * columnCount + column] = value;
                if(value > rowMax[row])
                    rowMax[row] = value;
                if(value > columnMax[column])
                    columnMax[column] = value;
            }
        }

        /*
        std :: cout << "Row Max Values: ";
        for(int a = 0; a < rowCount; a ++)
            std :: cout << rowMax[a] << " ";
        std :: cout << std :: endl;
        std :: cout << std :: endl;

        std :: cout << "Column Max Values: ";
        for(int a = 0; a < columnCount; a ++)
            std :: cout << columnMax[a] << " ";
        std :: cout << std :: endl;

        system("pause");
        */


        // if a square in a row is less than the row's maximum value, it must be the maximum of that column
        // or the entire pattern is impossible
        bool bPossible = true;
        for(int row = 0; row < rowCount; row ++)
        {
            for(int column = 0; column < columnCount; column ++)
            {
                int a = row *columnCount + column;
                int value = heights[a];

                // blindly accept values if they are the row's maximum
                if(value == rowMax[row])
                    continue;

                // other values must be equal to the column's maximum
                if(value == columnMax[column])
                    continue;

                // reaching here means that the pattern is impossible
                // so mark the flag and set the loop end conditions
                bPossible = false;
                row = rowCount;
                column = columnCount;
            }
        }


        // dump the answer to the output file
        // outFile << (bPossible? "YES": "NO");
        if(bPossible)
            outFile << "YES";
        else
            outFile << "NO";


        // delete arrays since don't need them anymore (should really only deallocate right at the end since dynamic allocation is uber slow... <_<')
        delete[] heights;
        delete[] rowMax;
        delete[] columnMax;
    }


    // close the input and output files
    inFile.close();
    outFile.close();
}
