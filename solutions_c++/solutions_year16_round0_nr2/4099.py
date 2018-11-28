

#include <istream>
#include <fstream>
#include <iostream>
using namespace std;

int main() {
    int T;
    string str;
    ifstream reader("input.txt");
    ofstream writer("output.txt");
    reader >> T;
    for(int i = 0; i < T; i++) {
        reader >> str;
        int counter = 0;
        for(int j = (int)str.length() - 1; j >= 0; j--) {
            if(counter%2 == 1) (str[j] == '+') ? (str[j] = '-') : (str[j] = '+');
            if(str[j] == '-') counter++;
        }
        writer << "Case #" << i + 1 << ": " <<  counter << endl;
    }
    writer.close();
    return 0;
}