#include <iostream>
#include <string>
#include <algorithm>
#include <cassert>
#include <fstream>
#include <vector>
using namespace std;

int main() {
	ifstream fin("B-large.in");
	ofstream fout("B-large.txt");
    int T;
    fin >> T;
    for(int j = 1; j <= T; j++) {
        string str;
        fin >> str;
        int min = 0;
        if(str[0] == '-' || str.length() > 1)
            min++;
        for(int i = 1; i < str.length(); i++) {
            if(str[i] != str[i-1])
                min++;
        }
        if(str[str.length()-1] == '+' && str.length() > 1)
            min--;
        fout << "Case #" << j << ": " << min << endl;
    }
    return 0;
}
