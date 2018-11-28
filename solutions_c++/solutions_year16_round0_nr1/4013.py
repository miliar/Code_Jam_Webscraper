

#include <vector>
#include <istream>
#include <fstream>
#include <iostream>
using namespace std;

bool check(vector<bool> digits) {
    bool c = true;
    for(int i = 0; i < 10; i++) {
        if(digits[i] == false)
            c = false;
    }
    return c;
}

void mark(vector<bool>& digits, int num) {
    while(num != 0) {
        int index = num%10;
        num /= 10;
        digits[index] = true;
    }
}

int main() {
    int T, N;
    ifstream reader("input.txt");
    ofstream writer("output.txt");
    reader >> T;
    for(int i = 0; i < T; i++) {
        vector<bool> digits(10, false);
        reader >> N;
        if(N == 0)
            writer << "Case #" << i + 1 << ": " <<  "INSOMNIA" << endl;
        else {
            int j = 1;
            while(!check(digits))
                mark(digits, N*(j++));
            writer << "Case #" << i + 1 << ": " <<  N*(j - 1) << endl;
        }
    }
    writer.close();
    return 0;
}