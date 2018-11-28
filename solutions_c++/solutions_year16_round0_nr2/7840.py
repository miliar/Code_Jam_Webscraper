#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

bool isOk(string in) {
    for(int i = 0; i < in.size(); ++i)
        if(in[i] == '-') return false;
    return true;
}

int main() {

    ifstream input("file.in");
    ofstream output("test.out");

    int n;
    input >> n;

    string line;
    getline(input, line);
    for(int i = 0; i < n; ++i) {
        getline(input, line);

        int count = 0;
        while(!isOk(line)) {
            count++;

            int delta = 0;
            while(delta + 1 < line.size() && line[delta + 1] == line[0]) { delta++; }
            bool tmp[delta + 1];
            for(int ii = 0; ii < delta + 1; ++ii)
                tmp[ii] = line[ii] == '-';
            for(int ii = 0; ii < delta + 1; ++ii)
                line[ii] = tmp[delta - ii] ? '+' : '-';
        }
        cout << "Case #" << i + 1 << ": " << count << endl;
        output << "Case #" << i + 1 << ": " << count << endl;
    }
}
