#include <bits/stdc++.h>

using namespace std;

int main(int argc, const char * argv[]) {
    
    stdin = fopen("/Inputs/input.txt", "r");
    stdout = fopen("/Inputs/output", "w");
    
    int numCases;
    scanf("%d", &numCases);
    
    for(int i = 0; i < numCases; i++){
        int startNum;
        set<char> digitsSeen;
        scanf("%d", &startNum);
        if(startNum == 0){
            printf("Case #%d: INSOMNIA\n", i+1);
            continue;
        }
        long long mult = 0;
        //Eval
        while(digitsSeen.size() < 10){
            mult++;
            long long res = mult * startNum;
            string resu = to_string(res);
            for(char digit : resu){
                digitsSeen.insert(digit);
            }
            if(res < 0){
                printf("WTF");
                return 1;
            }
        }
        printf("Case #%d: %lld\n", i+1, mult * startNum);
    }
    
    fclose(stdin);
    fclose(stdout);
    
    return 0;
}
