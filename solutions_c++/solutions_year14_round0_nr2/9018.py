
#include <iostream>
#include <vector>

#define NUMBTYPE double
#define INITIALFREQ 2

int main(int argc, const char * argv[])
{
    int numCases;
    
    std::cin >> numCases;
    
    std::vector<NUMBTYPE> results;
    
    for (int i = 0; i < numCases; i++){
        NUMBTYPE cost, imp, aim, lastFreq, timeFarm, actTime, postTime, result;
        
        result = 0;
        
        results.clear();
        
        std::cin >> cost >> imp >> aim;
        
        lastFreq = INITIALFREQ;
        
        results.push_back(0);
        
        
        while (true) {
            timeFarm = cost / lastFreq;
            
            actTime = aim / (lastFreq);
            postTime = aim / (lastFreq + imp);
            
            if (actTime > postTime + timeFarm) {
                results.push_back(timeFarm);
                lastFreq += imp;
            }else{
                break;
            }
        }
        
        for (std::vector<NUMBTYPE>::iterator it = results.begin(); it != results.end(); ++it) {
            result += *it;
        }
        
        result+= aim / lastFreq;
        
        std::cout.precision(7);
        std::cout.setf( std::ios::fixed, std:: ios::floatfield );
        std::cout << "Case #" << i+1 << ": " << result << std::endl;
        
    }

    return 0;
}

