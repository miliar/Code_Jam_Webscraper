#include<iostream>
#include<fstream>
#include<sstream>
#include<array>
#include<algorithm>
#include<vector>

typedef unsigned long long ull;


struct input {
    uint64_t N;
};

struct output {
    std::string S;
};

input parse(std::string line) {
    std::stringstream ss;
    ss << line;
    input I;
    
    ss >> I.N;
    
    return I;
}

output solve(input I){
    output O;
    std::stringstream ss;
    
    O.S = "INSOMNIA";
    if (I.N == 0) {
        return O;
    }
    
    std::array<bool, 10> seen = {0};
    
    for (uint64_t i = 1; i < 10000; i++) {
        uint64_t K = I.N*i;
        std::stringstream ss;
        ss << K;
        std::string S = ss.str();
        for (uint32_t j = 0; j < S.length(); j++) {
            seen[S[j]-'0'] = 1;
        }
        if (std::find(seen.begin(), seen.end(), 0)==seen.end()) {
            O.S = S;
            return O;
        }
    }
    
    return O;
}

void print(output O, uint32_t line) {
    std::cout << "Case #" << line << ": ";
    std::cout << O.S;
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
            lineNr++;
            continue;
        }
        input I = parse(line);
        output O = solve(I);
        print(O, lineNr++);
    }
}