#include <string>
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <vector>
#include <sstream>
#include <math.h>
#include <iterator>
#include <algorithm>
using namespace std;

void parse(string s, vector<string> &v) {
    istringstream buf(s);
    for(string token; getline(buf, token, ' '); )
        v.push_back(token);
    copy(v.begin(), v.end(), ostream_iterator<string>(cout, "."));
    cout << '\n';
}
bool is_palindrome(int n) {
    int num = n;
    int rev = 0;
    int dig = 0;
    while (num > 0) {
        dig = num % 10;
        rev = rev * 10 + dig;
        num = num / 10;
    }
    return n == rev;
}

int main(int argc, char* argv[]) {
    string filename = argv[1];
    ifstream input_file(filename.c_str());
    if (input_file.is_open()) {
        string line;
        getline(input_file, line);
        vector<int> results;
        while (input_file.good()) {
            int num_palindromes = 0;
            getline(input_file, line);
            vector<string> split;
            parse(line, split);
            if (split.size() == 0) continue;
            for (int i = atoi(split[0].c_str()); i <= atoi(split[1].c_str()); ++i) {
                double i_dub = double(i);
                if (sqrt(double(i)) != floor(sqrt(double(i)))) continue;
                if (is_palindrome(i) && is_palindrome(sqrt(double(i))))
                    ++num_palindromes;
            }
            results.push_back(num_palindromes);
        }
        input_file.close();
        ofstream out("resultsb.txt");
        if (out.is_open()) {
            for (int i = 0; i < results.size(); ++i) {
                stringstream ss;
                ss << "Case #" << i + 1 << ": " << results[i] << endl;
                out << ss.str();
            }
            out.close();
        }
    }
    return 0;
}