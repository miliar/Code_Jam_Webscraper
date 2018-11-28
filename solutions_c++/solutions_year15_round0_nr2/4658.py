#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <math.h>

int powOf2[11] = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024};

void printPlates(std::vector<int> p)
{
    for(int i = 0; i < p.size(); i++)
    {
        std::cout << p.at(i) << " ";
    }
    std::cout << std::endl;
}

int nextMin(std::vector<int> p, bool s, int numTurns, int tRem)
{
    bool done = true;
    std::vector<int> p2 = p;
    //printPlates(p);
    //printPlates(p2);
    if(tRem == 0)
    {
        return numTurns;
    }
    for(int i = 0; i < p.size(); i++)
    {
        if(p[i] != 0)
        {
            done = false;
            break;
        }
    }
    if(done)
        return numTurns;
    if(s)
    {
        int largest = 0;
        int indexLargest = 0;
        int numlargest = 0;
        int temp;
        for(int i = 0; i < p.size(); i++)
        {
            if(p[i] > largest)
            {
                largest = p[i];
                indexLargest = i; 
            }
        }
        for(int i = 0; i < p.size(); i++)
        {
            if(p[i] == largest)
                numlargest++;
        }
        if(largest > 4 && largest == 9 && numlargest%3)
        {
            p.push_back(p[indexLargest]-3);
            p[indexLargest] -= p[indexLargest]-3;  
        }
        else
        {
            p.push_back(floor(p[indexLargest]/2));
            p[indexLargest] -= floor(p[indexLargest]/2);
        }
        numTurns++;
        tRem--;
        largest = nextMin(p, true, numTurns, tRem);
        indexLargest = nextMin(p, false, numTurns, tRem);
        return largest > indexLargest? indexLargest: largest;
    }
    else
    {
        int A = 0, B = 0;
        for(int i = 0; i < p.size(); i++)
        {
            if(p[i] == 0)
                continue;
            p[i]--;
        }
        numTurns++;
        tRem--;
        
        
        A = nextMin(p, true, numTurns, tRem);
        B = nextMin(p, false, numTurns, tRem);
        return A > B? B: A;
    }
}

int main()
{
    int numCases; 
    int numEating;
    int numCakes;
    int totalCakes = 0;
    std::vector<int> plates;
    int size;
    int numMinutes = 0;
    bool sNeeded = false;
    int largest[2] = {0};
    int numLargest = 0;
    int maxTurns = 0;
    int turnsRem;
    int A = 0, B = 0;
    
    
    std::cout << "Begin input." << std::endl;
    std::cin >> numCases;
    
    int cases[numCases];

    for(int i = 0; i < numCases; i++)
    {
        plates.clear();
        std::cin >> numEating;
        largest[1] = 0;
        largest[0] = 0;
        totalCakes = 0;
        for(int j = 0; j < numEating; j++)
        {
            std::cin >> numCakes;
            plates.push_back(numCakes);
            totalCakes += numCakes;
        }
        for(int j = 0; j < plates.size(); j++)
        {
            if(plates[j] > largest[1])
            {
                largest[1] = plates[j];
                largest[0] = j; 
            }
        }
        maxTurns = largest[1];
        
        A = nextMin(plates, true, 0, maxTurns);
        B = nextMin(plates, false, 0, maxTurns);
        
        A < B ? cases[i] = A: cases[i] = B; 
    }
    
    
    puts("\nBegin output.");
    
    for(int i = 0; i < numCases; i++)
    {
        std::cout << "Case #" << i + 1 << ": " << cases[i] << std::endl;
    }

    return 0;
}
