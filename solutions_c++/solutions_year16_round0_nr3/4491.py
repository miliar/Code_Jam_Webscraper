using namespace std;

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstdint>
#include <sstream>

uint64_t nTests, length, cases;

void init(vector<uint64_t>& v) {
    for (uint64_t i=0; i<length-2; i++) {
        v[i] == 0;
    }
}

vector<uint64_t> convertToBinary(uint64_t num){
    vector<uint64_t> res;
    res.resize(length-2);
    init(res);
    uint64_t i=0;

    while (num != 0) {
        res[i] = num % 2;
        num = num/2;
        i++;
    }
    return res;
}

uint64_t power(uint64_t base, uint64_t exp) {
    if (exp == 0) {
        return 1;
    } else {
        return base * power(base, exp-1);
    }
}

string printVector(vector<uint64_t>& num) {
    string res;
    for (int i=num.size()-1; i>=0; i--) {
        ostringstream oss;
        oss << num[i];
        res += oss.str();
    }

    return res;
}

string printFactors(vector<uint64_t>& fact) {
    string res = "";
    for (uint64_t i=0; i<9; i++) {
        ostringstream oss;
        oss << fact[i];
        res = res + oss.str() + " ";
    }

    return res;
}

uint64_t convertToBase(vector<uint64_t>& num, uint64_t base) {
    uint64_t res = 1;
    uint64_t i;
    for (i=0; i<length-2; i++) {
        res += num[i] * power(base, i+1);
    }
    res += power(base, i+1);
    return res;
}

uint64_t isPrimeBase(vector<uint64_t>& num, uint64_t base) {
    uint64_t converted = convertToBase(num, base);

    if (converted % 3 == 0){
        return 3;
    } else {
        uint64_t i = 5;
        while (i*i <= converted) {
            if (converted % i == 0) {
                return i;
            } else if (converted % (i+2) == 0) {
                return i + 2;
            }
            i += 6;
        }
        return -1;
    }
}

int main(int argc, char* argv[]) {

    fstream in;
    in.open(argv[1], fstream::in);
    in >> nTests >> length >> cases;

    fstream out;
    out.open("output.txt", fstream::out);
    out << "Case #1:" << endl;

    uint64_t pos = 0;

    for (uint64_t i = 0; i < power(2, length-2); i++) {
        vector<uint64_t> num = convertToBinary(i);
        vector<uint64_t> factors;
        for (uint64_t j = 2; j<= 10; j++) {
            uint64_t tmp = isPrimeBase(num, j);
            if (tmp == -1) {
                break;
            } else {
                factors.push_back(tmp);
            }
        }

        if (factors.size() == 9) {
            out << "1" << printVector(num) << "1 ";
            out << printFactors(factors) << endl;
            pos++;
            if (pos == cases) {
                break;
            }
        }

    }

    return 0;
}
