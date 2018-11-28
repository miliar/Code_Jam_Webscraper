#include "CodeJam.hpp"
#include "Sheep.hpp"

int Sheep::solveAll() {
    int testCases;
    readln(testCases);
    
    for (curCase = 1; curCase <= testCases; ++curCase) {
        solve(curCase);
        std::cout << "Test " << curCase << " of " << testCases << std::endl;
    };
    return testCases;
}


void Sheep::solve(int task) {
    std::vector<int> nums(10);
    int N;
    readln(N);
    std::cout << N;
    
    std::cout << std::endl;
    if(N==0) {
        writeResult("INSOMNIA");
    } else {
        int done=0;
        int c=0;
        while(!done){
            c++;
            int w = c * N;
            std::ostringstream os;
            
            os << w;
            std::string digits = os.str();
            for(std::string::size_type i = 0; i < digits.size(); ++i) {
                nums[std::stoi(digits.substr(i,1))]=1;
            }
            
            if(10==std::accumulate(begin(nums), end(nums), 0, std::plus<int>())) {
                done = true;
                writeResult(c*N);
            }
        }
    }
}

int Sheep::count(int task) {
    return task;
}