//
//  jamcoin.cpp
//  codejam
//
//  Created by Adam Bielski on 09.04.2016.
//  Copyright © 2016 Adam Bielski. All rights reserved.
//

#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <unordered_set>

using std::cin;
using std::cout;
using std::string;

long long powers[9][32];

void init_powers() {
    for (int i=2; i<=10; ++i) {
        powers[i-2][0] = 1;
        for (int j=1; j<32; ++j) {
            powers[i-2][j] = powers[i-2][j-1] * i;
        }
    }
}

long long coinjam_divisor(long long k) {
    if (k%2==0)
        return 2;
    if (k%3==0)
        return 3;
    if (k%5==0)
        return 5;
    int i=7;
    int w = sqrt(k);
    while (i<w) {
        if (k%i == 0)
            return i;
        i+=4;
        if (k%i == 0)
            return i;
        i+=2;
    }
    return -1;
}

long long convert(string in, long long base) {
    const char* chars = in.c_str();
    long long result = chars[in.size()-1] == '0' ? 0 : 1;
    for (int i = in.size()-2; i>=0; --i) {
        if (chars[i] == '1')
            result += powers[base-2][in.size() - i - 1];
    }
    return result;
}

string random_coinjam(int len) {
    string a = "1";
    for (int i=1; i<len-1; ++i)
        a += ((double)rand())/RAND_MAX > 0.5 ? '1' : '0';
    a += '1';
    return a;
}

std::vector<std::pair<std::string, std::vector<long long>>>  solve(int N, int J) {
    srand(47);
    std::vector<std::pair<std::string, std::vector<long long>>> result;
    std::unordered_set<string> generated;
    while (result.size() < J) {
        string testcoin;
        while (generated.count(testcoin = random_coinjam(N))) {}
        generated.insert(testcoin);
        std::vector<long long> divisors;
        for (int i=2; i<=10; ++i) {
            long long w = coinjam_divisor(convert(testcoin, i));
            if (w==-1LL)
                break;
            divisors.push_back(w);
        }
        if (divisors.size() == 9)
            result.push_back(std::make_pair(testcoin, divisors));
    }
    return result;
}

std::vector<std::pair<std::string, std::vector<long long>>>  solve2N(int N, int J) {
    if (N%2==1) {
        // it's for N%2==0 and N<=36 and N>18 something
        // throw exception!
        return std::vector<std::pair<std::string, std::vector<long long>>>();
    }
    N/=2;
    std::vector<std::pair<std::string, std::vector<long long>>> tmp_res = solve(N, J);
    std::vector<std::pair<std::string, std::vector<long long>>> result;
    for (auto& r: tmp_res) {
        result.push_back(make_pair(r.first+r.first, r.second));
    }
    return result;
}


int main(int argc, char** argv) {
    init_powers();
    int N;
    cin >> N;
    for (int i=0; i<N; ++i) {
        int N, J;
        cin >> N >> J;
        std::vector<std::pair<std::string, std::vector<long long>>> result;
        if (N > 18) {
            result = solve2N(N, J);
        }
        else result = solve(N,J);
        cout << "Case #" << i+1 <<":"<< std::endl;
        for (auto& p: result) {
            cout << p.first << " " << p.second[0];
            for (int i=1; i<p.second.size(); ++i) {
                cout << " " << p.second[i];
            }
            cout << std::endl;
        }
    }
    return 0;
}