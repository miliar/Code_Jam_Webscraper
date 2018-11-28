#include <iostream>
#include <string>
#include <fstream>
#include <set>

using namespace std;

int NumOfFlips(const string& pan) {
    bool sign = true;

    int flips = 0;
    for (int i = pan.length() - 1; i >= 0; --i) {
        if ((pan[i] == '+' && sign) ||
            (pan[i] == '-' && !sign)) {
            continue;
        }
        flips++;
        sign = !sign;
    }
    return flips;

}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        cerr << "Give file name\n";
        return -1;
    }
    string fn = argv[1];
    ifstream input;
    input.open(fn.c_str());
    fn = fn.append(".out.txt");
    ofstream output;
    output.open(fn);

    int num_of_problems;
    input >> num_of_problems;

    for (int p = 1; p<= num_of_problems; ++p) {
        string cakes;
        input>>cakes;
        output << "Case #" << p << ": " << NumOfFlips(cakes) << endl;

    }

    output.close();
    input.close();
    return 0;
}