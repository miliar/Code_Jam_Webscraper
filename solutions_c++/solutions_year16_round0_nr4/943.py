//  main.cpp
//  Qualification Round D
//
//  Created by 苏炜 on 2016/4/9.

#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>

class number {
public:
    number() {
        _data.push_back(0);
    }
    
    number(std::string strNumber) {
        if (strNumber.empty()) {
            _data.push_back(0);
        } else {
            std::string::iterator it = strNumber.end();
            for (--it; it != strNumber.begin(); --it) {
                _data.push_back(*it - '0');
            }
            _data.push_back(*it - '0');
        }
    }
    
    number & operator=(const unsigned long num) {
        long n = num;
        _data.clear();
        if (n == 0) {
            _data.push_back(0);
        } else {
            while (n > 0) {
                _data.push_back(n % 10);
                n /= 10;
            }
        }
        return *this;
    }
    
    number & operator+=(const number & num) {
        add(_data, num._data);
        return *this;
    }
    
    number & operator*=(const int num) {
        int n = num;
        if (n == 0) {
            return operator=(0);
        }
        int pos = 0;
        data_t result;
        result.push_back(0);
        while (n > 0) {
            int digit = n % 10;
            data_t sub_result;
            copy(sub_result, _data);
            multiply_by_digit(sub_result, digit);
            move_digit(sub_result, pos);
            add(result, sub_result);
            ++pos;
            n /= 10;
        }
        copy(_data, result);
        return *this;
    }
    
    std::string str() {
        std::ostringstream oss;
        auto it = _data.end();
        for (--it; it != _data.begin(); --it) {
            oss << (int)*it;
        }
        oss << (int)*it;
        return oss.str();
    }
    
protected:
    typedef std::vector<unsigned char> data_t;
    data_t _data;
    
    static void copy(data_t & dst, const data_t & src) {
        dst.clear();
        for (auto it = src.begin(); it != src.end(); ++it) {
            dst.push_back(*it);
        }
    }
    
    static void add(data_t & dst, const data_t & src) {
        int i = 0, adder = 0;
        for (; i < src.size(); ++i) {
            if (dst.size() <= i) {
                dst.push_back(0);
            }
            dst[i] += (src[i] + adder);
            adder = dst[i] / 10;
            dst[i] %= 10;
        }
        while (adder > 0) {
            if (dst.size() <= i) {
                dst.push_back(0);
            }
            dst[i] += adder;
            adder = dst[i] / 10;
            dst[i] %= 10;
            ++i;
        }
    }
    
    static void multiply_by_digit(data_t & dst, const int digit) {
        int adder = 0;
        for (auto it = dst.begin(); it != dst.end(); ++it) {
            *it = *it * digit + adder;
            adder = *it / 10;
            *it %= 10;
        }
        if (adder > 0) {
            dst.push_back(adder);
        }
    }
    
    static void move_digit(data_t & dst, const int digit) {
        if (digit == 0) {
            return;
        }
        for (int i = 0; i < digit; ++i) {
            dst.push_back(0);
        }
        for (long i = dst.size() - digit - 1; i >= 0; --i) {
            dst[i + digit] = dst[i];
        }
        for (int i = 0; i < digit; ++i) {
            dst[i] = 0;
        }
    }
};

int main() {
    int T = 0;
    std::cin >> T;
    for (int t = 1; t <= T; ++t) {
        int K = 0, C = 0, S = 0;
        std::cin >> K >> C >> S;
        
        if (S < (float)K / (float)C) {
            std::cout << "Case #" << t << ": IMPOSSIBLE" << std::endl;
            continue;
        }
        
        // generate pow
        std::vector<number> pow_of_K;
        for (int i = 0; i < C; ++i) {
            if (i == 0) {
                number pow;
                pow = 1;
                pow_of_K.push_back(pow);
            } else {
                number pow(pow_of_K[i - 1]);
                pow *= K;
                pow_of_K.push_back(pow);
            }
        }
        
        std::cout << "Case #" << t << ":";
        number result;
        result = 1;
        int counter = 0;
        for (int i = 1; i <= K; ++i) {
            number n(pow_of_K[counter]);
            n *= (i - 1);
            result += n;
            ++counter;
            if (counter == C) {
                std::cout << ' ' << result.str();
                result = 1;
                counter = 0;
            }
        }
        if (counter > 0) {
            if (K <= C) {
                std::cout << ' ' << result.str();
            } else {
                for (int i = K - counter; i <= K - C + 1; ++i, ++counter) {
                    number n(pow_of_K[counter]);
                    n *= (i - 1);
                    result += n;
                }
                std::cout << ' ' << result.str();
            }
        }
        std::cout << std::endl;
    }
    return 0;
}
