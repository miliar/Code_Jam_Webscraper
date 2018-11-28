#include <stdio.h>

#define NUM 1000
#define max( a, b ) ( ( a > b) ? a : b )

int main(int argc, const char * argv[]) {
    FILE *pfile = fopen("/Users/jimmyliao/Downloads/A-large.in", "rt");
    FILE *pOutput = fopen("/Users/jimmyliao/Downloads/output.txt", "wt");
    int NumOfTestCase = 0;
    int shyness = 0;
    int attendeeCount = 0;
    int friendNeeded = 0;
    int attendeeNum[NUM];
    int i,j;
    char attendee[NUM];

    
    fscanf(pfile, "%d", &NumOfTestCase);
    
    for (i = 0; i < NumOfTestCase; i++) {
        fscanf(pfile, "%d %s", &shyness, attendee);

        for (j = 0; j <= shyness; j++) {
            attendeeNum[j] = attendee[j] - '0';
            
            if (attendeeCount < j)
                friendNeeded = max(j-attendeeCount, friendNeeded);
            
            attendeeCount += attendeeNum[j];
        }
        fprintf(pOutput, "Case #%d: %d\n", i+1, friendNeeded);
        
        // Reset variables
        friendNeeded = 0;
        attendeeCount = 0;
        for (j=0; j<NUM; j++)
            attendeeNum[j] = 0;
    }
    
    return 0;
}
