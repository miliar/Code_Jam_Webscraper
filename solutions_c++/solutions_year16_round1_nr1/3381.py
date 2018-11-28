#include <iostream>
#include <fstream>
#include <sstream>
#include <queue>
#include <string>
#include <cstring>
#include <list>

using namespace std;

string process_line(string);

int main(int argc, char **argv) {

    ifstream input_file(argv[1]);
    if (input_file.is_open()) {

        string line;
        int num_tests;

        /* read number of test cases */
        getline(input_file, line);
        num_tests = stoi(line);
        //cout << "num test cases " << num_tests << endl;

        /* process lines */
        int i;
        for (i = 0; i < num_tests; i++) {

            /* read number of price labels */
            getline(input_file, line);

            cout << "Case #" << to_string(i+1) << ": " << process_line(line) << endl;
        }

        input_file.close();
        return 0;
    }


    cout << "failed to open file: " << argv[1] << endl;
    return 1;
}

string process_line(string line) {
    string output = "";
    output += line[0];
    int i;
    for (i = 1; i < line.length(); i++) {
        if ( line[i] >= output[0] ) {
            output = line[i] + output;
        }
        else {
            output = output + line[i];
        }
    }

    return output;
}
