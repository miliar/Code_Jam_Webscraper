#include <bits/stdc++.h>

int main(int argc, const char * argv[]) {
    
    stdin = fopen("/Inputs/input.txt", "r");
    stdout = fopen("/Inputs/output", "w");
    
    int numCases;
    char currChar;
    char lastChar;
    
    scanf("%d%c", &numCases, &currChar);
    
    for(int i = 0 ;i < numCases; i++){
        currChar = 'd';
        long long numSwaps = 0;
        do {
            lastChar = currChar;
            scanf("%c", &currChar);
            if(lastChar != currChar){
                numSwaps++;
            }
        } while (currChar != '\n');
        if(lastChar == '+'){
            numSwaps--;
        }
        printf("Case #%d: %lld\n", i+1, numSwaps-1);
    }
    
    fclose(stdin);
    fclose(stdout);
    
    return 0;
}
