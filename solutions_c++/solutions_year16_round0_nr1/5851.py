#include <iostream>
#include <fstream>
#include <set>

using namespace std;

set<int> extract_digits(int n) {
    int d;
    set<int> res;
    while (n >= 10) {
        d = n % 10;
        res.insert(n % 10);
        n = n / 10;
    }
    if (n != 0)
        res.insert(n);
    return res;
}

void calc_sheep(int i, int k, ofstream &output_file, bool newline) {
    set<int> seen_digits;
    output_file << "Case #" << i << ": ";
    if (k == 0) {
        output_file << "INSOMNIA";
    }
    else {
        int s = 0;
        while (seen_digits.size() < 10) {
            s += k;
            set<int> digits = extract_digits(s);
            for (auto d = digits.begin(); d != digits.end(); ++d)
                seen_digits.insert(*d);

//        output_file << s << " named, seen digits: ";
//        for (auto d = seen_digits.begin(); d != seen_digits.end(); ++d)
//            output_file << *d << " ";
//        output_file << "\n";
        }
    output_file << s;
    }
    if (newline)
        output_file << "\n";
}

int main(int argc, char *argv[]) {
    ifstream inputFile;
    ofstream outputFile;
    inputFile.open("/home/ars/ClionProjects/ForTests/input.txt");
    outputFile.open("/home/ars/ClionProjects/ForTests/output.txt");
    if (inputFile.fail()) {
        cout << "Failed to open file\n";
    }
    int N, k;
    inputFile >> N;
    for (int i = 1; i <= N; i++) {
        inputFile >> k;
        if (i == N)
            calc_sheep(i, k, outputFile, false);
        else
            calc_sheep(i, k, outputFile, true);

    }
    while (inputFile >> N) {
        printf("%d ", N);
    }

    cout << "number of tests:" << N;
}