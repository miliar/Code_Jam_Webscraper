#include<iostream>
#include<fstream>
#include<sstream>
#include<array>
#include<algorithm>
#include<vector>

typedef unsigned long long ull;


struct input {
    ull N, R, P, S;
};

struct output {
    std::string S;
};

input parse(std::string line) {
    input I;
    std::stringstream ss;
    ss << line;
    ss >> I.N >> I.R >> I.P >> I.S;
    return I;
}

bool play(std::string S) {
    if (S.length() == 1) {
        return true;
    }
    std::string R;
    for (ull i=0; i<S.length(); i+=2) {
        if (S[i] == S[i+1]) {
            return false;
        }
        if (S[i] == 'P' && S[i+1] == 'R') {
            R += S[i];
        }
        if (S[i+1] == 'P' && S[i] == 'R') {
            R += S[i+1];
        }
        if (S[i] == 'P' && S[i+1] == 'S') {
            R += S[i+1];
        }
        if (S[i+1] == 'P' && S[i] == 'S') {
            R += S[i];
        }
        if (S[i] == 'R' && S[i+1] == 'S') {
            R += S[i];
        }
        if (S[i+1] == 'R' && S[i] == 'S') {
            R += S[i+1];
        }
    }
    return play(R);
}

std::string bfsolve(input I) {
    std::string S = std::string(I.P, 'P') + std::string(I.R, 'R') + std::string(I.S, 'S');
    do {
      if (play(S)) {
          return S;
      }
    } while (std::next_permutation(S.begin(), S.end()));
    return "IMPOSSIBLE";
}

output solve(input I){
    output O;
    O.S = bfsolve(I);
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