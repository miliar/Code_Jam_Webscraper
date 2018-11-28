#include<iostream>
#include<fstream>
#include<sstream>
#include<array>
#include<algorithm>
#include<vector>

typedef unsigned long long ull;


struct input {
    ull N, K;
    std::vector<double> P;
};

struct output {
    double D;
};

input parse(std::string line1, std::string line2) {
    input I;
    std::stringstream ss;
    ss << line1;
    ss >> I.N >> I.K;
    std::stringstream ss2;
    ss2 << line2;
    for (ull i=0; i<I.N; i++) {
        double d;
        ss2 >> d;
        I.P.push_back(d);
    }
    return I;
}

double bfsolve(input I) {
    double best = -1;
    std::string S = std::string(I.N - I.K, '0') + std::string(I.K, '1');
    do {
        std::vector<double> P;
        for (ull i=0; i<I.N; i++) {
            if (S[i] == '1') {
                P.push_back(I.P[i]);
            }
        }
        double tie = 0;
        std::string C = std::string(I.K / 2, '0') + std::string(I.K / 2, '1');
        do {
            double ttie = 1;
            for (ull i=0; i<C.length(); i++) {
                if (C[i] == '0') {
                    ttie *= (1-P[i]);
                }
                if (C[i] == '1') {
                    ttie *= P[i];
                }
            }
            tie += ttie;
        } while(std::next_permutation(C.begin(), C.end()));
        if (tie > best) {
            best = tie;
        }
    } while(std::next_permutation(S.begin(), S.end()));
    return best;
}

output solve(input I){
    output O;
    O.D = bfsolve(I);
    return O;
}

void print(output O, uint32_t line) {
    std::cout << "Case #" << line << ": ";
    std::cout << O.D;
    std::cout << "\n";
}

int main(int argc, char* argv[]) {
    std::vector<std::string> args(argv, argv+argc);
    if (args.size() != 2)
        return 1;
    std::ifstream ifs(args[1]);
    std::string line;
    std::getline(ifs, line);
    std::stringstream ss;
    ss << line;
    ull T;
    ss >> T;
    
    for (ull lineNr=1; lineNr<=T; lineNr++) {
        std::string line1, line2;
        std::getline(ifs, line1);
        std::getline(ifs, line2);
        
        input I = parse(line1, line2);
        output O = solve(I);
        print(O, lineNr);
    }
}