
#include <iostream>
#include <string>

#include <gmpxx.h>

bool is_pal(std::string s) {

    std::string::iterator fr = s.begin();
    std::string::iterator bk = s.end();
    --bk;

    while (fr <= bk) {

        if (*fr != *bk) return false;

        ++fr;
        --bk;
    }

    return true;

}

int main () {

    size_t num_cases = 0;

    std::cin >> num_cases;

    for (size_t i = 0; i < num_cases; ++i) {
   
        mpz_class a,b;

        std::cin >> a;
        std::cin >> b;

        size_t num = 0;

        for (mpz_class j = a; j <= b; ++j) {
        
            std::string s = j.get_str();
            
            if (is_pal(s)) {
                
                if (mpz_perfect_square_p(j.get_mpz_t())) {

                    mpz_class r = sqrt(j);

                    s = r.get_str();
                    if (is_pal(s)) {
                        ++num;
                    }
                }
            
            }
        }
        
        
        std::cout << "Case #" << i+1 << ": " << num << std::endl;
    }

    return 0;
}
