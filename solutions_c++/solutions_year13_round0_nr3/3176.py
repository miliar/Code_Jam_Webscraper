#include <cmath>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <vector>
using namespace std;


bool is_palindrome(double number) {
    std::stringstream ss;
    ss << number << setprecision(0);
    std::string nstr(ss.str());

    for (int i=0; i<nstr.length(); i++)
        if (nstr[i] != nstr[nstr.length()-1-i]) return false;
    return true;
}


int main(int argc, char **argv) {

    ifstream testf(argv[1]);
    string line;
    stringstream linestream;
    int num_tests;

    getline(testf, line);
    linestream.str(line);
    linestream >> num_tests;

    double a,b;
    for (int t=0; t<num_tests; t++) {
        getline(testf, line);
        linestream.clear();
        linestream.str(line);
        linestream >> a >> b;

        double lower_sqrt = ceil(sqrt(a));
        double upper_sqrt = floor(sqrt(b));

        int fair_amount = 0;
        for (double i=lower_sqrt; i<=upper_sqrt; i+=1.0) {
            if (is_palindrome(i)) {
                double squared_number = round(i * i);
                if (is_palindrome(squared_number)) {
                    fair_amount++;
                }
            }
        }

        cout << "Case #" << t+1 << ": " << fair_amount << endl;
    }

    return 0;
}

