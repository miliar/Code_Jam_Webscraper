#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
#include <stdlib.h>


int main(void)
{
    std::ifstream inputFile("A-small-attempt0.in");
    std::FILE* outputFile = std::fopen("output", "w");

    if (inputFile.is_open())
    {
        std::string line;
        getline(inputFile, line);
        int cases = atoi(line.c_str());

        for (int c=0; c<cases; ++c)
        {
            float PI = 3.14;
            //printf("%f\n", PI);
            getline(inputFile, line);
            int seperatorPos = line.find(" ");
            std::string strMillilitres, strRadius;
            strRadius.assign(line, 0, seperatorPos);
            strMillilitres.assign(line, seperatorPos, line.length()-seperatorPos);
            float radius = atof(strRadius.c_str()) + 1.0f;
            float millilitres = atof(strMillilitres.c_str());
            int rings = 0;

            while (millilitres > 0.0f)
            {
                if (millilitres >= (radius*radius) - ((radius-1)*(radius-1)))
                {
                    millilitres -= (radius*radius) - ((radius-1)*(radius-1));
                    radius += 2;
                    rings++;
                }
                else
                    break;
            }

            std::fprintf(outputFile, "Case #%d: %d\n", c+1, rings);
        }
    }

    std::fclose(outputFile);
    inputFile.close();

    return 0;
}
