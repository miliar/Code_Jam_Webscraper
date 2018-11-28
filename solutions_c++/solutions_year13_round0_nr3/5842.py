#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <stdlib.h>
#include <stdio.h>

int main(void)
{
    std::ifstream inputFile("C-small-attempt0.in");
    std::FILE * outputFile = std::fopen("output", "w");
    if (inputFile.is_open())
    {
        std::vector<int> vecFairAndSquare;
        std::string line;
        getline(inputFile, line);
        int cases = atoi(line.c_str());
        
        for (int i=1; i<=1000; ++i)
        {
            char bufferI[124];
            std::snprintf(bufferI, sizeof(bufferI), "%d", i);
            std::string baseI, reverseI;
            baseI.assign(bufferI);
            reverseI.assign(baseI.rbegin(), baseI.rend());
            if (i == atoi(reverseI.c_str()))
            {
                int j = i*i;
                char bufferJ[124];
                std::snprintf(bufferJ, sizeof(bufferJ), "%d", j);
                std::string baseJ, reverseJ;
                baseJ.assign(bufferJ);
                reverseJ.assign(baseJ.rbegin(), baseJ.rend());
                if (j == atoi(reverseJ.c_str()))
                {
                    vecFairAndSquare.push_back(j);
                }
            }
        }
        
        for (int c=0; c<cases; ++c)
        {
            getline(inputFile, line);
            int seperatorPos = line.find(" ");
            std::string strHeight;
            std::string strWidth;
            strHeight.assign(line, 0, seperatorPos);
            strWidth.assign(line, seperatorPos, line.length()-seperatorPos);
            int a = atoi(strHeight.c_str());
            int b = atoi(strWidth.c_str());
            int areFairAndSquare = 0;
            int minValueToBegin = 0;
            int vecSize = vecFairAndSquare.size();
            
            for (int i=a; i<=b; ++i)
            {
                for (int ii=minValueToBegin; ii<vecSize; ++ii)
                {
                    if (i == vecFairAndSquare[ii])
                    {
                        areFairAndSquare++;
                        minValueToBegin = ii+1;
                    }
                }
                if (minValueToBegin >= vecSize)
                    break;
            }
            
            std::fprintf(outputFile, "Case #%d: %d\n", c+1, areFairAndSquare);
        }
    }
    
    std::fclose(outputFile);
    inputFile.close();
    
    return 0;
}
