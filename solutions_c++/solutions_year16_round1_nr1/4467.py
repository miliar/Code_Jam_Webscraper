#include <iostream>
#include <string>
#include <fstream>

using namespace std;

string last_word(string s) {
    // cout << "s: " << s << endl;
    string res = "";
    res += s[0];
    for (int i = 1; i < s.size(); ++i) {
        if (s[i] > res[0]) res = s[i] + res;
        else if (s[i] == res[0]) {
            if (s[i] > res.back()) res = s[i] + res;
            else res += s[i];
        } else res =  res + s[i];
    }
    return res;
}

int main(int argc, char* argv[]) {
    ifstream in(argv[1]);
    ofstream out(argv[2]);
    if (in.is_open()) {
        string line;
        int num_test_case;
        getline(in, line);
        num_test_case = stoi(line);
        cout << "num_test_case: " << num_test_case << endl;
        int num;
        int test_cast = 1;
        while (num_test_case-- && getline(in, line)) {
            // istringstream iss(line);

            out << "Case #" << test_cast++ << ": " << last_word(line) << endl;
        }
        in.close();
        out.close();
    }
}
