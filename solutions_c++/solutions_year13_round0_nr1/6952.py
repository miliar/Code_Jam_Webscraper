#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <stdio.h>

int fourConnected(std::string str)
{
    if (str == "XXXX" || str == "XXXT" || str == "XXTX" || str == "XTXX" || str == "TXXX")
        return 0;
    else if (str == "OOOO" || str == "OOOT" || str == "OOTO" || str == "OTOO" || str == "TOOO")
        return 1;
    else if (str.find(".") != std::string::npos)
        return 3;
    else
        return 2;
}

int main(void)
{
    std::ifstream inputFile("A-large.in");
    std::FILE * outputFile = std::fopen("output", "w");
    if (inputFile.is_open())
    {
        std::string result[4] = {"X won", "O won", "Draw", "Game has not completed"};
        std::string line;
        getline(inputFile, line);
        int cases = atoi(line.c_str());
        
        for (int c=0; c<cases; ++c)
        {
            std::string row[10];
            int won = 2;
            
            for (int i=0; i<4; ++i)
            {
                getline(inputFile, row[i]);
                
                if (won > 1)
                {
                    int tempWon = fourConnected(row[i]);
                    if (tempWon == 0 || tempWon == 1 || (tempWon == 3 && won != 0 && won != 1))
                        won = tempWon;
                        
                    for (int ii=0; ii<4; ++ii)
                    {
                        row[ii+4].append(row[i], ii, 1);
                    }
                    row[8].append(row[i], i, 1);
                    row[9].append(row[i], 3-i, 1);
                }
            }
            
            if (won > 1)
            {
                for (int i=4; i<10; ++i)
                {
                    int tempWon = fourConnected(row[i]);
                    if (tempWon == 0 || tempWon == 1 || (tempWon == 3 && won != 0 && won != 1))
                    {
                        won = tempWon;
                        if (tempWon == 0 || tempWon == 1)
                            break;
                    }
                }
            }
            
            std::fprintf(outputFile, "Case #%d: %s\n", c+1, result[won].c_str());
            getline(inputFile, line);
        }
    }
    
    inputFile.close();
    std::fclose(outputFile);
    
    return 0;
}
