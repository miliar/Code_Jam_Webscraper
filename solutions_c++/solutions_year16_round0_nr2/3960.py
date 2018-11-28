#include <iostream>
#include <fstream>
#include <string>
#include <unordered_map>

using namespace std;



int countRevenge_v1(string str) {
    size_t pos = str.rfind('-');
    if (pos==std::string::npos) return 0;
    int count = 0;
    while (pos!=std::string::npos) {
        count++;
        if (pos == 0) break;
        for (size_t i = 0 ;i <= pos; ++i) {
            str[i] = str[i] == '+' ? '-' : '+';
        }
        pos = str.rfind('-');
    }
    return count;
}

int countRevenge(string str) {
    int count = 0;
    int i = str.size() - 1;
    while (str[i] == '+') --i;
    if (i < 0) return 0;
    for (; i >= 0; --i) {
        if (str[i] != str[i+1]) count++;
    }

    return count;
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
            out << "Case #" << test_cast++ << ": " << countRevenge(line) << endl;
        }
        in.close();
        out.close();
    }
}
