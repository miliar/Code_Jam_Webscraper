#include <iostream>
#include <string>

int main(){
    
    int T;
    std::string S;
    
    std::cin >> T;
    
    for(int t = 1; t <= T; ++t){
 
        std::cin >> S;
        char prev = S[0];
        int total = 0;
        
        for(int i = 1; i < S.size(); ++i){
            if(S[i] != prev) {
                prev = S[i];
                ++total;
            }
        }
        
        if(S[S.size()-1] == '-') ++total;
        
        std::cout <<"Case #" << t << ": "<< total << std::endl;
    }
}