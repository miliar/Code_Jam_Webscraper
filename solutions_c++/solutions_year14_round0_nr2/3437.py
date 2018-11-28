#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <bitset>


typedef double real;

int main(int argc, char** args)
{
    // number of cookies per second
    int N;
    real ncps = 2;
    real C,F,X;
    // time we spent just waiting until we get X with 2 cookies per second
    real accumTime = 0;
    
    // get number of cases
    std::cin >> N;
    std::cout << std::fixed;
    std::cout.precision(7);
    
    for (int i = 0; i < N; ++i) {
        std::cin >> C;
        std::cin >> F;
        std::cin >> X;
        ncps = 2;
        accumTime = 0;
        real minTime = X / ncps;
        //std::cout << "C: " << C << ", F: " << F << ", X: " << X << ", nf: " << X/2  << ", minTime: " << minTime <<  std::endl;
        
        // count until how many farms we can buy        
        while (accumTime < minTime) {
            // how much time we spent if we just use the current farms
            real t1 = accumTime + X / ncps;
            // we decide to buy a farm
            real buyTime = C / ncps;
            // now the time we need to wait until X with new ncps
            ncps += F;
            accumTime += buyTime;
            
            minTime = std::min(minTime, t1);
            
        }
  
           
        std::cout << "Case #" << i+1 << ": " << minTime << std::endl;
        
    }

    return 0;
}
