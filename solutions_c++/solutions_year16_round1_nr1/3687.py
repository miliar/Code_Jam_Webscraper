

#include <vector>
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
        string strTemp;
        strTemp = str[0];
        for(int j = 1; j < (int)str.length(); j++) {
            if(str[j] >= strTemp[0])
                strTemp = str[j] + strTemp;
            else
                strTemp = strTemp + str[j];
        }
        writer << "Case #" << i + 1 << ": " << strTemp << endl;
    }
    writer.close();
    return 0;
}