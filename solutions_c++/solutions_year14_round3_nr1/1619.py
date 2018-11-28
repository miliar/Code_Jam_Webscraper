#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <memory>
#include <thread>
#include <numeric>
#include <future>
#include <limits>

#include <boost/lexical_cast.hpp>
#include <boost/math/common_factor_rt.hpp>

using namespace boost::math; 

unsigned log2(unsigned x)
{   
    unsigned l = 0;
    while (x > 1) {
        x /= 2;
        ++l;
    }
    return l;
}

unsigned l2p(unsigned x)
{
    unsigned L2p = 1;
    while (2 * L2p < x) {
        L2p *= 2;
    }
    return L2p;
}

unsigned g2p(unsigned x)
{
    return x & (~x+1);
}

int f(unsigned P, unsigned Q)
{
    unsigned GCD = gcd(P, Q);
    P /= GCD;
    Q /= GCD;
    unsigned QP = g2p(Q);
    //std::cerr << "Q = " << Q << ", QP = " << QP << std::endl;
    unsigned LQP = log2(QP);
    if (QP != Q || LQP >= 40) {
        return -1;
    } 
    
    auto L2p = log2(l2p(P));
    return LQP - L2p;
}

int main()
{
    auto& in = std::cin;
    auto& out = std::cout;

    size_t T;
    in >> T;
    
    for (size_t t = 0; t < T; ++t) {
        std::string line;
        in >> line;
        unsigned P = boost::lexical_cast<unsigned>(
                        line.substr(0, line.find('/')));
        
        unsigned Q = boost::lexical_cast<unsigned>(
                        line.substr(line.find('/') + 1));
        
        int r = f(P, Q);
        if (r >= 0) {
            out << "Case #" << (t + 1) << ": " << r << std::endl;
        } else {
            out << "Case #" << (t + 1) << ": " << "impossible" << std::endl;
        }

    }

    return 0;
}

