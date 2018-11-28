#include "stdio.h"
#include "stdlib.h"
#include <vector>
#include <limits.h>
#include <queue>
#include <map>
#include <string>
#include <iostream>


void printVector(std::vector<int> shynessLevel, int maxShyness) {
        for (int i = 0; i <= maxShyness; i++) 
            std::cout << shynessLevel[i] << "\t";
        std::cout << std::endl;
}

int main() {
    int T;
    scanf("%d", &T);
    std::vector<int> shynessLevel;
    
    int number, result, maxShyness;
    for (int t = 0; t < T; t++) {
        result = 0;
        scanf("%d%d",&maxShyness, &number);
        //printf("=========== Test 1 ============ \nMax shyness: %d\n", maxShyness);

        for (int i = maxShyness; i >= 0; i--) {
            int digit = number % 10;
            shynessLevel.push_back(digit);
            number /= 10;
        }
        std::reverse(shynessLevel.begin(),shynessLevel.end()); 
        
        if (shynessLevel[0] == 0) {
            shynessLevel[0] = 1;
            result++; 
        }       
        for (int i = 1; i <= maxShyness; i++) {
            shynessLevel[i] += shynessLevel[i-1];
            if (shynessLevel[i] < i + 1) {
                shynessLevel[i] = i+1;
                result++; 
            }
        }
        
        printf("Case #%d: %d\n", t+1, result);
        shynessLevel.clear();
    }

}
