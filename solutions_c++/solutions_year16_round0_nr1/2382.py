#include <iostream>
#include <string>
#include <fstream>
#include <set>

using namespace std;

long long LastNumber(long long orgnum) {
    set<int> all_digits;

    long long curnum = 0;
    while (all_digits.size() < 10) {
        curnum += orgnum;
        long long num = curnum;
        while (num != 0 && all_digits.size() < 10) {
            all_digits.insert(num % 10);
            num /= 10;
        }
    }
    return curnum;
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
        int num;
        input>>num;
        output << "Case #" << p << ": ";

        if (num == 0) {
            output << "INSOMNIA";
        } else {
            output << LastNumber(num);
        }
        output<<endl;

    }

    output.close();
    input.close();
    return 0;
}