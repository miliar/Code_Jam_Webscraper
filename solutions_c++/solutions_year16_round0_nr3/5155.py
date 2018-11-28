




#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>


#define SIZE_LARGE_INTEGER 3




typedef uint64_t cointype;      // set equal



template <typename I> 
I ipow(I x, I n) {
    I y = 1;
    for(I i = 1; i <= n; ++i) {
        y *= x;
    }
    return(y);
}



class LargeUInt {
    
public:
    std::vector<uint32_t> val;
    
    LargeUInt(int size);
    LargeUInt(int size, uint32_t x);
    
    void add(LargeUInt x);
    void multiply(uint32_t x);
    uint32_t mod(uint32_t div);
};

LargeUInt::LargeUInt(int size): val(size,0) {}

LargeUInt::LargeUInt(int size, uint32_t x): val(size,0) {
    val.back() = x;
}


void LargeUInt::add(LargeUInt x) {  // attention: x must be of same size as val
    
    uint32_t carrier = 0;
    for(int i = val.size()-1; i >= 0; --i) {
        uint64_t sum = static_cast<uint64_t>(val[i]) + static_cast<uint64_t>(x.val[i]) + static_cast<uint64_t>(carrier);
        val[i] = sum;
        carrier = sum >> 32;
    }
    
}

void LargeUInt::multiply(uint32_t x) {
    
    uint32_t carrier = 0;
    for(int i = val.size()-1; i >= 0; --i) {
        uint64_t product = static_cast<uint64_t>(val[i]) * static_cast<uint64_t>(x) + static_cast<uint64_t>(carrier);
        val[i] = product;
        carrier = product >> 32;
    }
    
}


uint32_t LargeUInt::mod(uint32_t div) {
    
    uint64_t rest = 0;
    for(int i = 0; i < val.size(); ++i) {
        
        rest = rest << 32;
        rest +=  val[i];
        rest = rest % static_cast<uint64_t>(div);
    }
    
    return(rest);
    
}



LargeUInt coin_as_base_n(cointype coin, uint32_t n) {
    
    LargeUInt y(SIZE_LARGE_INTEGER);
    LargeUInt significance(SIZE_LARGE_INTEGER, 1);
    
    for(int i = 0; i < sizeof(cointype)*8; ++i) {
        // get i_th bit of coin
        bool bit_i = (coin & ( static_cast<cointype>(1) << i )) >> i;
        if(bit_i) {
            y.add(significance);
        }
        significance.multiply(n);
    }
    
    return(y);
    
}




std::string coin_to_str(cointype coin) {
    
    std::string coinstr = "";
    bool flag_start = false;
    
    for(int i = sizeof(cointype)*8 - 1; i >= 0 ; --i) {
        bool bit_i = (coin & ( static_cast<cointype>(1) << i )) >> i;
        if(bit_i) {
            coinstr.append("1");
            flag_start = flag_start || true;
        }
        else if(flag_start) {
            coinstr.append("0");
        }
    }
    
    return(coinstr);
}



uint32_t find_divisor(LargeUInt x, uint32_t div_max) {
    
    for(uint32_t div = 2; div <= div_max; ++div) { // no check fo div < x/2 (operator missing)
        if(x.mod(div) == 0) {
            return(div);
        }
    }
    return(0);
    
}



bool find_divisors(cointype coin, std::vector<uint32_t> &divisors, uint32_t div_max) { 
    
    for(uint32_t i = 0; i < 9; ++i) {
        uint32_t base = i + 2;
        
        // convert to base
        LargeUInt coin_base_n = coin_as_base_n(coin, base);
        uint32_t div = find_divisor(coin_base_n, div_max);
        
        if(div > 1) {
            divisors[i] = div;
        }
        else {
            return(false);
        }
    }
    
    return(true);
    
}




int main(int argc, char* argv[]) {


    std::string fname_input = argv[1];
    std::string fname_output = argv[2];
    uint32_t div_max = std::stoi(argv[3]);      // maximum value of divisor to search for

    int N = 0;
    int J = 0;
    
    // read input
    std::ifstream input(fname_input);
    if(! input.good()) {
        std::cerr << "Error: could not read input file" << std::endl;
        exit(1);
    }
    
    // read file
    std::string line;
    std::getline(input, line);
    int n = std::stoi(line);
    if(n != 1) {
        std::cerr << "Error: unexpected number of cases in input file" << std::endl;
        exit(1);
    }
    std::getline(input, line);
    std::stringstream sline(line);
    sline >> N;
    sline >> J;
    

    
    std::cout << "parameters: " << std::endl;
    std::cout << "  N = " << N << std::endl;
    std::cout << "  J = " << J << std::endl;
    std::cout << "  div_max = << " << div_max << std::endl;
    
    
        
    std::vector<cointype> coins(J,0);
    std::vector<std::vector<uint32_t> > all_divisors(J,std::vector<uint32_t>(9,0));
    
    int j = 0;
    cointype coin = ipow<cointype>(2,N-1) + 1;    // lower bound
    cointype coin_max = ipow<cointype>(2,N) - 1;
    
    while(j < J) {
        
        std::vector<uint32_t> divisors(9,0);
        bool divs_ok = find_divisors(coin, divisors, div_max);
        if(divs_ok) {
            coins[j] = coin;
            all_divisors[j] = divisors;
            std::cout << "found coin j = " << j  << "  coin = " << coin << "  coinstr = " << coin_to_str(coin) << std::endl;
            for(int i = 0; i < 9; ++i) {
                std::cout << "  div base " << i+2 << ":   coin " << coin_as_base_n(coin, i+2).val.back() << "  " << divisors[i] << std::endl;
            }
            ++j;
        }
        
        coin += 2;
        
        if(coin > coin_max) {
            std::cerr << "exceeded upper limit of coins with given N, but not enought jamcoins found. (try again with higher value for div_max)";
            return(1);
        }
        
    }
    
    
    // output to file
    std::ofstream output(fname_output);
    
    output << "Case #1:" << std::endl;
    for(int i = 0; i < J; ++i) {
        output << coin_to_str(coins[i]);
        for(int k = 0; k < 9; ++k) {
            output << " " << all_divisors[i][k];
        }
        output << std::endl;
    }
    
    
    



    return(0);
}
