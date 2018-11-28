
#include <iostream>
#include <vector>
#include <algorithm>

int main(int argc, const char * argv[])
{
    int numCases = 0;
    
    std::cin >> numCases;
    
    for(int i = 0; i < numCases; i++){
        
        std::cout << "Case #" << i+1 << ": ";
        
        int countP = 0;
        
        int line, numTemp;
        int values[5];
        values[4] = -1;
        std::cin >> line;
        for (int j = 0; j < 16; j++) {
            std::cin >> numTemp;
            if (j / 4 == line-1) {
                values[j % 4] = numTemp;
            }
        }
        
        int * answer1 = NULL;
        int * answer2 = NULL;
        std::cin >> line;
        for (int j = 0; j < 16; j++) {
            std::cin >> numTemp;
            if (j / 4 == line-1) {
                answer1 = std::find(values, values+4, numTemp);
                
                if(answer1!=values+4)
                {
                    answer2 = answer1;
                    countP++;
                }
                
            }
        }
        
        
        if (countP > 1) {
            std::cout << "Bad magician!";
        }
        else if (countP == 0) {
            std::cout << "Volunteer cheated!";
        }else{
            std::cout << *answer2;
        }
        
        std::cout << std::endl;
        
    }
    
    return 0;
}

