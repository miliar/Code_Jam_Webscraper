#include <fstream>
#include <iostream>
#include <map>
#include <vector>
#include <string>


int main(int argc, char *argv[]){
    std::ifstream inF;
    inF.open(argv[1]);
    int n;
    inF>>n;
    for (int j = 1; j < n+1; ++j){
        std::string state;
        inF>>state;
        size_t pos;
        int c = 0;
        pos = state.rfind('-');
        while (pos != std::string::npos){
            c++;
            for (size_t b = 0; b <= pos; ++b)
                state[b] = (state[b] == '+' ? '-': '+');
            pos = state.rfind('-');
        }
        std::cout<<"Case #"<<j<<": "<<c<<std::endl;
    }

    return 0;
}
