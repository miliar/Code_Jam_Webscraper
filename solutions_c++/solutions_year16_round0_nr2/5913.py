#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void pancakes(int i, const string &line, ofstream &output_file) {
    output_file << "Case #" << i << ": ";
    int s = 0;
    bool is_start = true;
    bool is_in_sad = false;
    for (auto pancake : line) {
        if (is_start) {
            if (pancake == '-') {
                s += 1;
                is_in_sad = true;
            }
            is_start = false;

        }
        else {
            if (pancake == '+') {
                is_in_sad = false;
            }
            else if (pancake == '-' && !is_in_sad) {
                s += 2;
                is_in_sad = true;
            }
        }
    }
    output_file << s << "\n";
}

int main(int argc, char *argv[]) {
    ifstream input_file;
    ofstream output_file;
    input_file.open("/home/ars/ClionProjects/ForTests/input.txt");
    output_file.open("/home/ars/ClionProjects/ForTests/output.txt");
    if (input_file.fail()) {
        cout << "Failed to open file\n";
    }

    int T;
    input_file >> T;
    string line;
    getline(input_file, line); // eat newline after T
    for (int i = 1; i <= T; i++) {
        getline(input_file, line);
        pancakes(i, line, output_file);

    }

    return 0;
}