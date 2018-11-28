#include <iostream>
#include <fstream>
#include <sstream>
#include <set>
#include <vector>

using namespace std;

int main(int argc, char * argv[]) {
    ifstream ifile(argv[1]);

    string text = "";
    int counter = -1, row = -2, round1 = 1;
    set<string> nums;
    vector<string> results;
    while (getline(ifile, text)) {
        stringstream ss(text);

        if (counter == 0) {
            ss >> row;
        }
        else if (counter == row && round1) {
            string n;
            while (ss >> n) {
                nums.insert(n);
            }

            round1 = 0;
            row = -2;
        }
        else if (counter == row && !round1) {
            bool valid = true;
            string n, found = "-1";
            while (ss >> n) {
                if (nums.count(n)) {
                    if (found == "-1") 
                        found = n;
                    else { // Multiple results
                        results.push_back("Bad magician!");
                        valid = false;
                        break;
                    }
                }
            }
            if (valid) {
                if (found == "-1") // No results
                    results.push_back("Volunteer cheated!");
                else { // 1 possible number
                    results.push_back(found);
                }
            }

            round1 = 1;
            row = -2;
            nums.clear();
        }

        if (counter == 4)
            counter = 0;
        else
            ++counter;
    }
    ifile.close();

    ofstream ofile(argv[2]);
    for (unsigned int i = 0; i < results.size(); ++i) {
        ofile << "Case #" << (i + 1) << ": " << results[i] << "\n";
    }
    ofile.close();

    return 0;
}