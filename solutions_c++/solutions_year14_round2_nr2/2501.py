#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>
using namespace std;

#define U64 unsigned long long

struct testcase {
    U64 a, b, k;
};

vector<testcase*> cases;

bool readFile();
void writeFile(vector<string*> towrite);

U64 solve(testcase *tc) {
    U64 result = 0;
    U64 a = tc->a;
    U64 b = tc->b;
    U64 k = tc->k;
    for(U64 i = 0; i < a; i++) {
        for(U64 j = 0; j < b; j++) {
            if((i & j) < k)
                result++;
        }
    }
    /*if(k < a && k < b) {
        result += b * k;
        result += (a-k) * k;
    }
    else if(k < a) {
        result +=
    }
    else {
        
    }*/
    return result;
}

int main(int argc, char **argv) {
    readFile();

    vector<string*> towrite;

    for(int i = 0; i < cases.size(); i++) {
        U64 result = solve(cases[i]);

        stringstream stream;

        stream << "Case #" << i+1 << ": " << result;

        string *s = new string( stream.str() );
        towrite.push_back(s);
    }

    writeFile(towrite);

    return 0;
}


//-------------------------------Helper Functions-------------------------------


bool readFile() {
    std::string line;
    std::ifstream cfile("lottery.in");

    if(cfile.is_open()) {
        getline(cfile, line);
        int num = std::stoi(line);
        for(int i = 0; i < num; i++) {
            getline(cfile, line);
            testcase *loaded = new testcase();
            std::string::size_type sz = 0;
            loaded->a = std::stoull(line, &sz);
            line = line.substr(sz);
            loaded->b = std::stoull(line, &sz);
            line = line.substr(sz);
            loaded->k = std::stoull(line, &sz);

            cases.push_back(loaded);
        }
        cfile.close();
    }
    else return false;

    return true;
}

void writeFile(vector<string*> towrite) {
    ofstream out;
    out.open("lottery.out");
    for(unsigned int i = 0; i < towrite.size(); i++) {
        out << *towrite[i] << endl;
    }
    out.close();
}
