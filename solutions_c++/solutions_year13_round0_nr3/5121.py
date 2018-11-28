
#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iterator>

#include <boost/cstdint.hpp>
#include <boost/lexical_cast.hpp>

#include "boost/multiprecision/gmp.hpp" 
#include "boost/multiprecision/cpp_int.hpp" 
 
// typedef boost::multiprecision::mpz_int BigInt; 
// typedef boost::multiprecision::uint512_t BigInt; 
typedef uint64_t BigInt;
typedef uint64_t u64;

bool isPalindrome(const std::string& s) {
    std::string r = s;
    std::reverse(r.begin(), r.end());
    return s == r;
}

bool isPalindrome(const BigInt& a) {
    std::string s = boost::lexical_cast<std::string>(a);
    return isPalindrome(s);
}

bool filterOut(const std::string& s) {
    if(s.size() > 1) {
        bool ret =  s[0] > '2' or s[s.size() - 1] > '2';
        if(!ret) {
            for(std::string::const_iterator it = s.begin(); it != s.end(); ++it) {
                if (*it > '2') return true;
            }
        } else {
            return true;
        }
    }
    
    return false;
}

// brute force, 10^14 fits 47 bits, when double has 52 bits for fraction part
int solution(u64 a, u64 b) {
    int ret = 0;
    for (u64 i=a; i<=b; ++i) {
        if (isPalindrome(i)) {
            double s = sqrt(static_cast<double>(i));
            double intPart;
            double fracPart = modf(s,&intPart);
            if( intPart == s ) {
                u64 j = static_cast<u64>(s);
                if (isPalindrome(j)) {
                    ++ret;
                }
            }
        }
    }

    return ret;
}

int cache(u64 a, u64 b, std::vector<u64> &c) {
    int ret = 0;
    for (u64 i=a; i<=b; ++i) {
        if (isPalindrome(i)) {
            double s = sqrt(static_cast<double>(i));
            double intPart;
            double fracPart = modf(s,&intPart);
            if( intPart == s ) {
                u64 j = static_cast<u64>(s);
                if (isPalindrome(j)) {
                    c.push_back(i);
                    ++ret;
                    std::cout << i << " " << std::flush;
                }
            }
        }
    }

    return ret;
}

template<typename INT>
int createCache(INT max, std::vector<INT> &c) {
    INT cur = 1;
    INT curSq = 1;
    
    c.push_back(cur);
    INT preSq = curSq;
    INT pre = cur;
    
    while (curSq <= max) {
        ++cur;
        curSq = preSq + (pre<<1); ++curSq;
        
        std::string curs = boost::lexical_cast<std::string>(cur);
#ifdef HEURISTIC
        if (! filterOut(curs))
#endif
        if (isPalindrome(curs) and isPalindrome(curSq)) {
            c.push_back(curSq);
            //std::clog << cur << " / " << curSq << " / " << max << std::endl;
        }
        
        preSq = curSq;
        pre = cur;
    }

    //std::clog << curSq << " / " << max << std::endl;
    
    return c.size();
}

int solution(BigInt a, BigInt b, const std::vector<BigInt>& aCache) {
    int ret = 0;
    for(std::vector<BigInt>::const_iterator it = aCache.begin(); it!= aCache.end(); ++it) {
        if(a <= *it) {
            if(*it <= b) {
                ++ret;
            } else {
                break;
            }
        }
    }
    return ret;
}

int main() {
    const BigInt MAX = 100000000000000; // 14 zeros
    
    // BigInt M = 10000000000; // 10 zeros
    // BigInt MAX = 1;
    // for(int i=0;i<10;++i)MAX*=M;
    
    std::vector<BigInt> mCache;
    createCache<BigInt>(MAX, mCache);
    
    std::copy(mCache.begin(), mCache.end(), std::ostream_iterator<BigInt>(std::clog," "));
    std::clog << "\n" << mCache.size() << std::endl;
    
    int n = 0;
    std::cin >> n;
    for (int i=0; i<n; ++i) {
        BigInt a,b;
        std::cin >> a >> b;
        
        int s = solution(a,b, mCache);
        printf("Case #%d: %d\n", i+1, s);
    }

    return 0;
}
