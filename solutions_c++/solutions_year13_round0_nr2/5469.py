#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <vector>


using namespace std;

int main()
{
    FILE* file;
    file = fopen("test.txt", "r");
    if (!file)
        return -1;

    int count = 0;
    fscanf(file, "%i", &count);
    bool* results = (bool*)(malloc(sizeof(bool)*count));
    for (int i = 0; i < count; i++)
    {
        int sizeX = 0, sizeY = 0;
        fscanf(file, "\n%i %i", &sizeY, &sizeX);
        int tableau[sizeY][sizeX];
        //int minInColumn[sizeX];
        int maxInColumn[sizeX];
        //int minInLine[sizeY];
        int maxInLine[sizeY];
        for (int j = 0; j < sizeX; j++)
        {
            //minInColumn[j] = 100;
            maxInColumn[j] = 0;
        }
        for (int j = 0; j < sizeY; j++)
        {
            //minInLine[j] = 100;
            maxInLine[j] = 0;
        }
        for (int j = 0; j < sizeY; j++)
        {
            fscanf(file, "\n");
            for (int k = 0; k<sizeX;k++)
            {
                fscanf(file, "%i", &tableau[j][k]);
                int tmp = tableau[j][k];
                if (tmp > maxInLine[j])
                    maxInLine[j] = tmp;
                //if (tmp < minInLine[j])
                //    minInLine[j] = tmp;
                if (tmp > maxInColumn[k])
                    maxInColumn[k] = tmp;
                //if (tmp < minInColumn[k])
                 //   minInColumn[k] = tmp;
            }
        }
        // check all mins :
        bool feasible = true;
        int val = 0;
        for (int j = 0; j < sizeY; j++)
        {
            for (int k = 0; k<sizeX;k++)
            {
                val = tableau[j][k];
                if (val < maxInLine[j] && val < maxInColumn[k])
                {
                    feasible = false;
                    break;
                }
            }
            if (!feasible)
                break;
        }
        results[i] = feasible;
    }

    FILE* file2;
    file2=fopen("testout.txt", "w");
    if (!file2)
        return -1;
    for (int i = 0; i < count; i++)
    {
        fprintf(file2,"Case #%i: ", i+1);
        if (results[i])
            fprintf(file2,"YES");
        else
            fprintf(file2,"NO");
        if (i != count-1)
            fprintf(file2,"\n");
    }
    return 0;
}












