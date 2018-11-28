#include <iostream>
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int numCases = 0;   
    int count = 0;      
    int maxShy = 0;   
    int numStanding;
    char temp;
    
    std::cout << "Begin input." << std::endl;
    
    std::cin >> numCases;
    count = numCases;
    
    int cases[numCases];

    while(count-- > 0)
    {
        numStanding = 0;
        cases[numCases - count - 1] = 0;
        std::cin >> maxShy;
        
        getchar();      
        
        for(int i = 0; i <= maxShy; i++)
        {
            temp = getchar();
            if(temp == '0' && numStanding < i + 1)
            {
                cases[numCases - count - 1]++;
                numStanding++;
            }
            else
            {
              numStanding += temp - 48;
            }
        }
    }
    
    puts("\nBegin output.");
    
    while(++count < numCases)
    {
        std::cout << "Case #" << count + 1 << ": " << cases[count] << std::endl;
    }

    return 0;
}
