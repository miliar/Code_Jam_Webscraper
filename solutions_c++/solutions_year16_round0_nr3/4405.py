#include <cassert>
#include <array>
#include <cmath>
#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <bitset>

using namespace std;

template <typename T>
void format(int caseId, T &&str, unsigned long nbits) {
    cout << "Case #" << ++caseId << ":" << endl;
    for (auto &sol : str) {
        unsigned long s = sol.back();
        sol.pop_back();
        if (nbits == 6)
            cout << bitset<6>(s);
        else if (nbits == 16)
            cout << bitset<16>(s);
        else if (nbits == 32)
            cout << bitset<32>(s);
        else if (nbits == 19)
            cout << bitset<19>(s);
        else cout << s;
        for (auto div : sol) {
            cout << " " << div;
        }
        cout << endl;
    }
}

template <typename T>
bool cond(T &&data) {
    for (auto b : data)
        if (!b)
            return false;
    return true;
}

template <typename T>
void update(T &&data, unsigned long long num) {
    int first = 0;
    int last = num - 1;
    while (first < last) {
        std::swap(data[first], data[last]);
        data[first] = !data[first];
        data[last] = !data[last];
        ++first;
        --last;
    }
    if (first == last) {
        data[first] = !data[first];
    }
}

unsigned long convert(unsigned long sol, unsigned long base) {
    unsigned long res = sol & 1;
    unsigned long rank = 1;
    sol = sol >> 1;
    while (sol) {
        if (sol & 1)
            res += pow(base, rank);
        ++rank;
        sol = sol >> 1;
    }
    return res;
}

unsigned long findDiv(unsigned long val) {
    unsigned long max = sqrt(val) + 1;
    for (unsigned long i = 3; i < max; ++i)
        if (val % i == 0)
            return i;
    return val;
}

vector<unsigned long> solution(unsigned long& sol) {
    vector<unsigned long> res;
    while (res.size() != 9) {
        sol += 2;
        res.clear();
        for (unsigned long base = 2; base <= 10; ++base) {
            unsigned long val = convert(sol, base);
            unsigned long div = findDiv(val);
            if (div == val)
                break;
            res.push_back(div);
        }
    }
    res.push_back(sol);
    return res;
}

template <typename T>
void check(T &&res) {
    for (auto &vect : res) {
        unsigned long v = vect.back();
        for (unsigned long i = 2; i <= 10; ++i) {
            unsigned long div = vect[i-2];
            unsigned long n = convert(v, i);
            assert( n % div == 0 );
            if ( n % div != 0 ) {
                exit(1);
            }
        }
    }
}

template <typename T>
void play(int caseId, T nbits, T nsol) {
    vector<vector<unsigned long>> res;
    unsigned long sol = (1 << (nbits - 1)) + 1 - 2;
    while (res.size() != nsol) {
        res.push_back(solution(sol));
    }
    
    //for (auto &vect : res) {
    //    unsigned long v = vect.back();
    //    cout << v << endl;
    //    for (unsigned long i = 2; i <= 10; ++i)
    //        cout << convert(v, i) << " ";
    //    cout << endl;
    //}
    //check(res);
    format(caseId, res, nbits);
}

int main(int argc, char *argv[]) {
    if (argc == 1)
        return 1;
    ifstream f(argv[1]);

    int nLines;
    f >> nLines;
    for (int i = 0; i < nLines; ++i) {
        unsigned long nbits;
        unsigned long nsol;
        f >> nbits;
        f >> nsol;
        play(i, nbits, nsol);
    }
}
