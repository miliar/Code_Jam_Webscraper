#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstdint>

#define TRACE(cmd)
//#define TRACE(cmd) cmd

typedef intmax_t Int;

std::string solve(const std::string& s);

int main() {
    int T;
    std::cin >> T;
    for (int t=1; t<=T; ++t) {
        std::string p;
        std::cin >> p;
        std::cout << "Case #" << t << ": " << solve(p) << std::endl;
    }
    return 0;
}

std::string normalize(const std::string& s) {
    std::string normalized;
    char c = '?';
    for (int i=0; i<s.size(); ++i) {
        char p = c;
        c = s[i];
        if (c != p) normalized.push_back(c);
    }
    return normalized;
}

std::string int2str(int i) {
    std::stringstream s;
    s << i;
    return s.str();
}
/*
struct Solution {
    std::map<std::string, int> cache;
    Solution() {
        cache["+"] = 0;
        cache["-"] = 1;
        cache["-+"] = 1;
        cache["+-"] = 2;
        cache["+-+"] = 2;
        cache["-+-"] = 3;
    }
    std::string solve(const std::string& s) {
        std::string n = normalize(s);
        if (cache.count(n) > 0) {
            return int2str(cache[n]);
        }
        std::string smaller = 
        int ret = s.back() == '+' ? solve
    }
};


// 1. only normalized version matters -- alternating groups change anything
// 2. if normalized form ends with '+', solve for string withouth last '+'
//    the same number is the solution, because we come to it by '-'+ (<- regex +)
//    so last flip matches with last '+'
// 3. simple algorith resulting in the same result is flip first group untill all '+'

*/
std::string solve(const std::string& s) {
    //static Solution s;      
    std::string n = normalize(s);
    return int2str(n.size() + (n.back() == '+' ? -1 : 0));
}

// +-+-
// -+--
// ++-+
// --++
// ++++
//
// +-+-
// --+-
// +++-
// ----
// ++++
//
//
// +--+
// ---+
// ++++
//
// +--+
// ++-+
// ---+
// ++++
//
// -+-+
// ++-+
// ---+
// ++++
//
// -+-+
// +-++
// --++
// ++++
//
// +-+-+
// --+-+
// +++-+
// ----+
// +++++
//
// +-+-+
// -+--+
// ++--+
// ----+
// +++++
//
//
//
