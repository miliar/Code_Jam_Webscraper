#include <iostream> 
#include <string>
#include <vector>
#include <cmath>
#include <boost/algorithm/string.hpp>
#include <gmpxx.h>
#include "frac.hpp"

std::string getCleaningSeq(int length, int comp, int students) {
        if ((students < length && comp == 1) || students < (float)length/2) {
                return "IMPOSSIBLE";
        }
        if (length == 1) return "1";

        std::string sequence = "";
        
        if (comp == 1) {
                for (int i=1; i<=length; i+=1) {
                        sequence += " " + std::to_string(i);
                }
                boost::algorithm::trim(sequence);
                return sequence;
        }
        mpz_class r;
        for (int i=1; i<length; i += 2) {
            mpz_ui_pow_ui (r.get_mpz_t(), length, comp-1);
            r = r*(i-1) + i + 1;
            sequence += " " + r.get_str();
        }

        if (length % 2 == 1) {
                mpz_ui_pow_ui (r.get_mpz_t(), length, comp);
                sequence += " " + r.get_str();
        }

        boost::algorithm::trim(sequence);
        return sequence;

}
