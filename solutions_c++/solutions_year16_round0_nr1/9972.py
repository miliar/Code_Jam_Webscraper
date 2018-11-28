
#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>



typedef unsigned int itype;




unsigned int digit_register(itype x) {
    
    unsigned int digits = 0;
    
    unsigned int powersof2[10] = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512};
    
    
    for(itype decimal = 1; decimal*10 <= x*10; decimal *= 10) {
        unsigned int digit = (x % (decimal*10)) / decimal;   // get individual digit
        
        digits = digits | powersof2[digit];                  // 'store' digit to register
    }
    
    return(digits);
}


itype find_iN(itype N) {
    
    unsigned int digits_acumulated = 0;
    
    for(int i = 1; i < 10e3; ++i) {
        
        digits_acumulated = digits_acumulated | digit_register(N * i);
        
        
        if(digits_acumulated >= 1023) {
            return(N*i);
        }
    }
    
}



int main(int argc, char* argv[]) {

    std::string fname_input = argv[1];
    std::string fname_output = argv[2];
    
    
    int n;
    
    // open file
    
    std::ifstream input(fname_input);
    if(! input.good()) {
        std::cerr << "Error: could not read input file" << std::endl;
        exit(1);
    }
    
    // read file
    std::string line;
    std::getline(input, line);
    
    n = std::stoi(line);

    std::vector<itype> Ns(n,0);
    
    for(int i = 0; i < n; ++i) {
        std::getline(input, line);
        Ns[i] = std::stoi(line);
    }

    // open output file
    std::ofstream output(fname_output);
    
    // compute and output
    for(int i = 0; i < Ns.size(); ++i) {
        
        
        output << "Case #" << i+1 << ": ";
        if(Ns[i] == 0) {
            output << "INSOMNIA" << std::endl;
        }
        else{
            itype N_result = find_iN(Ns[i]);
            output << N_result << std::endl;
        }
    }
    
    return(0);

}
