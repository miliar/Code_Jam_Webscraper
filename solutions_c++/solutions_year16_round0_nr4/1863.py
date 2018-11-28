#include <bits/stdc++.h>

using namespace std;

int main(int argc, const char * argv[]) {
    
    int numCases;
    
    stdin = fopen("/Inputs/input.txt", "r");
    stdout = fopen("/Inputs/output", "w");
    
    scanf("%d", &numCases);
    
    for(int i = 0; i < numCases; i++){
        int k, c, s;
        scanf("%d %d %d", &k, &c, &s);
        
        printf("Case #%d: ", i + 1);
        for(int j = 0; j < k; j++){
            printf("%d ", j + 1);
        }
        printf("\n");
    }
    
    return 0;
}
