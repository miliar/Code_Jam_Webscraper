#include<iostream>
#include<fstream>
#include<sstream>
#include<algorithm>
#include<vector>
#include<unordered_map>

typedef unsigned long long ull;


struct input {
    std::string S;
};

struct output {
    uint64_t N;
};

input parse(std::string line) {
    std::stringstream ss;
    ss << line;
    input I;
    I.S = line;
    return I;
}

std::string flip(std::string S, uint32_t I) {
    std::reverse(S.begin(), S.begin() + I);
    for (uint32_t i = 0; i < I; i++) {
        S[i] = (S[i] == '+') ? '-' : '+';
    }
    return S;
}

std::unordered_map<std::string, uint64_t> MAP;

uint64_t bfsolve(std::string S){
    if (std::find(S.begin(), S.end(), '-') == S.end()) {
        return 0;
    }
    if (MAP.find(S) != MAP.end()) {
        return MAP[S];
    }
    MAP[S] = -1ULL - 2;
    uint64_t best = -1ULL;
    for (uint32_t i = 1; i <= S.length(); i++) {
        std::string T = flip(S, i);
        uint64_t N = bfsolve(T) + 1;
        best = std::min(best, N);
    }
    MAP[S] = best;
    return best;
}

uint64_t gsolve(std::string S) {
    if (std::find(S.begin(), S.end(), '-') == S.end()) {
        return 0;
    }
    char first = S[0];
    char s = (first == '+') ? '-' : '+';
    uint32_t idx = std::find(S.begin(), S.end(), s) - S.begin();
    std::string T = flip(S, idx);
    return gsolve(T) + 1;
}

output solve(input I){
    output O;
    O.N = gsolve(I.S);
    return O;
}

void print(output O, uint32_t line) {
    std::cout << "Case #" << line << ": ";
    std::cout << O.N;
    std::cout << "\n";
}

int main(int argc, char* argv[]) {
    std::vector<std::string> args(argv, argv+argc);
    if (args.size() != 2)
        return 1;
    std::ifstream ifs(args[1]);
    std::string line;
    uint32_t lineNr = 0;
    while (true) {
        std::getline(ifs, line);
        if (!ifs)
            break;
        if (lineNr == 0) {
            lineNr = 1;
            continue;
        }
        input I = parse(line);
        output O = solve(I);
        print(O, lineNr++);
    }
}