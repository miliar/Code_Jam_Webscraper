#include<iostream>
#include<fstream>
#include<sstream>
#include<algorithm>
#include<vector>

typedef unsigned long long ull;


struct input {
    uint32_t K, C, S;
};

struct output {
    std::vector<uint32_t> I;
};

input parse(std::string line) {
    std::stringstream ss;
    ss << line;
    input I;
    ss >> I.K >> I.C >> I.S;
    return I;
}

std::string gen(std::string B, uint32_t C) {
    uint32_t K = B.length();
    std::string R = B;
    for (uint32_t i = 0; i < C - 1; i++) {
        std::string nB;
        for (uint32_t j = 0; j < R.length(); j++) {
            if (R[j] == 'G') {
                nB += std::string(K, 'G');
            }
            else {
                nB += B;
            }
        }
        R = nB;
    }
    return R;
}

std::string intToBase(uint32_t K, uint32_t N) {
    std::string R(K, 'G');
    uint32_t i = K-1;
    while (N) {
        R[i] = (N%2) ? 'L' : 'G';
        i--;
        N /= 2;
    }
    return R;
}

void genAll(uint32_t K, uint32_t C) {
    for (uint32_t i = 0; i < (1ULL<<K); i++) {
        std::string B = intToBase(K, i);
        std::cout << B << " " << gen(B, C) << "\n";
    }
}

output solve(input I){
    output O;
    O.I.resize(I.K);
    for (uint32_t i = 0; i < I.K; i++) {
        O.I[i] = i + 1;
    }
    return O;
}

void print(output O, uint32_t line) {
    std::cout << "Case #" << line << ": ";
    if (O.I.empty()) {
        std::cout << "IMPOSSIBLE";
    }
    for (auto i : O.I) {
        std::cout << i << " ";
    }
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



