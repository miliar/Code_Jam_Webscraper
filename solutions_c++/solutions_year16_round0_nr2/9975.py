#include <cstdlib>
#include <cstdio>
#include <climits>

#define MAX_TST_CASES 100

inline void readStdin(int *pInputBuffer)
{
    char oneLine[100 + 1];
    size_t idxChar = 0;
    
    int* pInputWriter = pInputBuffer;
    bool isFirstElement = true;
    while((oneLine[idxChar++] = fgetc(stdin)) != EOF)
    {
        if(oneLine[idxChar - 1] == '\n')
        {
            if(isFirstElement == true)
            {
                *pInputWriter++ = atoi(oneLine);
                isFirstElement = false;
            }
            else
            {
                int minusCounter = 0;
                bool plusEncountered = false;
                bool stopCountingMinus = false;
                for(size_t idx = 0; idx < (idxChar - 1); ++idx)
                {
                    if(oneLine[idx] == '+')
                    {
                        plusEncountered = true;
                        stopCountingMinus = false;
                    }
                    else
                        if((oneLine[idx] == '-') && (stopCountingMinus == false))
                        {
                            stopCountingMinus = true;
                            
                            if(plusEncountered == true)
                            {
                                minusCounter+= 2;
                                plusEncountered = false;
                            }
                            else
                            {
                                ++minusCounter;
                            }
                        }
                }
                
                *pInputWriter++ = minusCounter;
            }
            
            idxChar = 0;
        }
    }
}
 
// ===========================================================
 
int main(int argc, char* argv[])
{
    ////////////////////////////////////////////////////////
    //  Read the input.
    ////////////////////////////////////////////////////////
    
    // Max test cases + 1 for number of given test cases.
    // Index 0 contains number of test cases.
    int inputBuffer[MAX_TST_CASES + 1];
    readStdin(inputBuffer);
    
    const int tstCases = inputBuffer[0];
    
    for(int idx = 1; idx<= tstCases; ++idx)
    {
        printf("Case #%d: %d\n", idx, inputBuffer[idx]);
    }
 
    return (0);
}
 