#include <cstdlib>
#include <cstdio>
#include <climits>

#define MAX_TST_CASES 100
 
inline void readStdin(int* pInputBuffer)
{
    int* pBufferWriter = pInputBuffer;
    
    size_t idxChar = 0;
    char oneLine[1000000];
    while((oneLine[idxChar++] = fgetc(stdin)) != EOF)
    {
        if(oneLine[idxChar - 1] == '\n')
        {
            idxChar = 0;
            *pBufferWriter++ = atoi(oneLine);
        }
    }
}

// ===========================================================

int analyze(const int inputNumber)
{
    if(inputNumber > 0)
    {
        int8_t digitsCount[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    
        int outputNumber = 1;
        bool found = false;
        for(size_t idx = 1; (idx <= ULONG_MAX) && (found == false); ++idx)
        {
            outputNumber = inputNumber * idx;
            
            int divVal = 1;
            int digit;
            while(outputNumber >= divVal)
            {
                digit = ((outputNumber / divVal) % 10);
                
                digitsCount[digit] |= 1;
                divVal *= 10;
            }
            
            found = digitsCount[0] & digitsCount[1] & digitsCount[2] & digitsCount[3] &
                        digitsCount[4] & digitsCount[5] & digitsCount[6] & digitsCount[7] &
                        digitsCount[8] & digitsCount[9];
        }
        
        if(found == true)
        {
            return (outputNumber);
        }
    }
    
    return (-1);
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
    
    for(int idx = 1; idx<= inputBuffer[0]; ++idx)
    {
        int inputNumber = inputBuffer[idx];
        
        int sleepAt = analyze(inputNumber);
        
        if(sleepAt > 0)
        {
            printf("Case #%d: %d\n", idx, sleepAt);
        }
        else
        {
            printf("Case #%d: INSOMNIA\n", idx);
            
        }
    }
 
    return (0);
}
