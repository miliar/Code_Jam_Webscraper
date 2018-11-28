#include <iostream>
#include <fstream>

using namespace std;

bool check(string s) {
    for (int i = 0; i < s.size(); ++i) {
        if (s[i] == '-') return false;
    }
    return true;
}

int main() {
    ifstream in("C:\\Users\\Cyril\\ClionProjects\\CodeJam\\file.in");
    ofstream out("C:\\Users\\Cyril\\ClionProjects\\CodeJam\\test1.out");

    unsigned n;
    in >> n;
    string line;
    getline(in, line);


    for (int i = 0; i < n; ++i) {
        getline(in, line);

        int count = 0;
        while (!check(line)) {
            count++;
            int c = 0;
            while(c + 1 < line.size() && line[c + 1] == line[0]) { c++; }

            bool list[c + 1];

            for (int k = 0; k < c +1; ++k) {
                list[k] = (line[k] == '+');
            }

            for (int j = 0; j < c + 1; ++j) {
                line[j] = list[c - j] ? '-' : '+';
            }
            cout << c << " " << line << endl;
            if (count > 9) break;
        }
        out << "Case #" << i + 1 << ": " << count << endl;
        cout << "----------------" << endl;
    }


}

