//  main.cpp
//  Qualification Round A
//
//  Created by 苏炜 on 2016/4/9.

#include <iostream>
#include <vector>
#include <string>
#include <sstream>

class number {
public:
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
    
    number & operator+=(const number & num) {
        int i = 0, adder = 0;
        for (; i < num._data.size(); ++i) {
            if (_data.size() <= i) {
                _data.push_back(0);
            }
            _data[i] += (num._data[i] + adder);
            adder = _data[i] / 10;
            _data[i] %= 10;
        }
        while (adder > 0) {
            if (_data.size() <= i) {
                _data.push_back(0);
            }
            _data[i] += adder;
            adder = _data[i] / 10;
            _data[i] %= 10;
            ++i;
        }
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
    std::vector<unsigned char> _data;
};

class ext_number : public number {
public:
    ext_number(std::string strNumber) : number(strNumber) {
        _shown[0] = _shown[1] = _shown[2] = _shown[3] = _shown[4]
            = _shown[5] = _shown[6] = _shown[7] = _shown[8] = _shown[9] = false;
    }
    bool check() {
        for (auto it = _data.begin(); it != _data.end(); ++it) {
            _shown[*it] = true;
        }
        return _shown[0] && _shown[1] && _shown[2] && _shown[3] && _shown[4]
            && _shown[5] && _shown[6] && _shown[7] && _shown[8] && _shown[9];
    }
    
protected:
    bool _shown[10];
};

int main() {
    int T = 0;
    std::cin >> T;
    for (int t = 1; t <= T; ++t) {
        std::string strN;
        std::cin >> strN;
        
        // trim left zeros
        auto pos = strN.find_first_not_of('0');
        if (pos == std::string::npos) {
            std::cout << "Case #" << t << ": INSOMNIA" << std::endl;
            continue;
        }
        strN = strN.substr(pos);
        
        // calc
        number N(strN);
        ext_number n(strN);
        while (!n.check()) {
            n += N;
        }
        
        std::cout << "Case #" << t << ": " << n.str() << std::endl;
    }
    return 0;
}
