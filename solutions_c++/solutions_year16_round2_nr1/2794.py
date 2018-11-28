#include<stdio.h>
#include<math.h>
#include<string.h>
#include <vector>

#define NUMIDX(x) x-65
using namespace std;

void printNumber(char str[]) {
    int idx;
    vector<int> AlphabetCount;
    vector<int> NumberCount;
    AlphabetCount.resize(26,0);
    NumberCount.resize(10,0);
    for(idx = 0; idx < strlen(str); idx++) {
        AlphabetCount[str[idx]-65]++;
    }
    
    int count;
    
    //Eliminate 2
    count = AlphabetCount[NUMIDX('W')];
    AlphabetCount[NUMIDX('W')] = 0;
    AlphabetCount[NUMIDX('T')] -=  count;
    AlphabetCount[NUMIDX('O')] -=  count;
    NumberCount[2] = count;
    
    //Eliminate 0
    count = AlphabetCount[NUMIDX('Z')];
    AlphabetCount[NUMIDX('Z')] = 0;
    AlphabetCount[NUMIDX('E')] -=  count;
    AlphabetCount[NUMIDX('R')] -=  count;
    AlphabetCount[NUMIDX('O')] -=  count;
    NumberCount[0] = count;
    
    //Eliminate 6
    count = AlphabetCount[NUMIDX('X')];
    AlphabetCount[NUMIDX('X')] = 0;
    AlphabetCount[NUMIDX('S')] -=  count;
    AlphabetCount[NUMIDX('I')] -=  count;
    NumberCount[6] = count;
    
    //Eliminate 8
    count = AlphabetCount[NUMIDX('G')];
    AlphabetCount[NUMIDX('G')] = 0;
    AlphabetCount[NUMIDX('E')] -=  count;
    AlphabetCount[NUMIDX('I')] -=  count;
    AlphabetCount[NUMIDX('H')] -=  count;
    AlphabetCount[NUMIDX('T')] -=  count;
    NumberCount[8] = count;
    
    //Eliminate 7
    count = AlphabetCount[NUMIDX('S')];
    AlphabetCount[NUMIDX('S')] = 0;
    AlphabetCount[NUMIDX('E')] -=  2*count;
    AlphabetCount[NUMIDX('V')] -=  count;
    AlphabetCount[NUMIDX('N')] -=  count;
    NumberCount[7] = count;
    
    //Eliminate 5
    count = AlphabetCount[NUMIDX('V')];
    AlphabetCount[NUMIDX('V')] = 0;
    AlphabetCount[NUMIDX('E')] -=  count;
    AlphabetCount[NUMIDX('F')] -=  count;
    AlphabetCount[NUMIDX('I')] -=  count;
    NumberCount[5] = count;
    
    //Eliminate 4
    count = AlphabetCount[NUMIDX('F')];
    AlphabetCount[NUMIDX('F')] = 0;
    AlphabetCount[NUMIDX('O')] -=  count;
    AlphabetCount[NUMIDX('U')] -=  count;
    AlphabetCount[NUMIDX('R')] -=  count;
    NumberCount[4] = count;
    
    //Eliminate 3
    count = AlphabetCount[NUMIDX('H')];
    AlphabetCount[NUMIDX('T')] = 0;
    AlphabetCount[NUMIDX('E')] -=  2*count;
    AlphabetCount[NUMIDX('R')] -=  count;
    NumberCount[3] = count;
    
    //Eliminate 1
    count = AlphabetCount[NUMIDX('O')];
    AlphabetCount[NUMIDX('O')] = 0;
    AlphabetCount[NUMIDX('N')] -=  count;
    AlphabetCount[NUMIDX('E')] -=  count;
    NumberCount[1] = count;
    
    //Eliminate 9
    count = AlphabetCount[NUMIDX('I')];
    AlphabetCount[NUMIDX('I')] = 0;
    AlphabetCount[NUMIDX('N')] -=  2*count;
    AlphabetCount[NUMIDX('E')] -=  count;
    NumberCount[9] = count;
    
    for(int itr = 0; itr <= 9; itr++) {
        for(int cnt = 0; cnt < NumberCount[itr]; cnt++) {
            printf("%d",itr);
        }
    }
}

int main() {
    int TestCaseCount, cnt;
    char str[2000];
    TestCaseCount = 0;
    FILE*   fpIn = freopen("A-large.in", "r+", stdin);
    FILE*   fpOut = freopen("out", "w+", stdout);
    scanf("%d",&TestCaseCount);
    
    for(cnt = 0; cnt<TestCaseCount; cnt++) {
        scanf("%s",str);
        printf("Case #%d: ", cnt+1);
        printNumber(str);
        if(cnt!=TestCaseCount-1)
            printf("\n");
    }
    
    fclose(fpIn);
    fclose(fpOut);
    
    return 0;    
}

