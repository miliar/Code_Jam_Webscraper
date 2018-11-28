#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

vector<char> Sort(string S) {
    vector<char> res;
    for (auto i : S) {
        if (!res.size() || i >= res[0]) {
            res.insert(res.begin(), i);
        }
        else {
            res.push_back(i);
        }
    }
    return res;
}



int main() {
    ifstream infile("A-large.in.txt");
    ofstream outfile("output.out");
    string a;
    infile >> a;
    int i = 0;
    while (infile >> a) {
        i++;
        outfile << "Case #" << i << ": ";
        vector<char> temp = Sort(a);
        for (auto s : temp) outfile << s;
        outfile << endl;
    }
}
