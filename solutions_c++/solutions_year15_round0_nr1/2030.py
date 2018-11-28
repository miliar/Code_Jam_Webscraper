#include <set>
#include <map>
#include <iostream>
#include <fstream>
using namespace std;

string path = "/home/nicolai/work/CLionProjects/untitled/";

int main() {
    int n;
    ifstream in(path + "input.txt");
    ofstream out(path + "output.txt");
    in >> n;
    for (int i = 0; i < n; i++) {
        int m;
        in >> m;
        string str;
        in >> str;
        int sm = 0, add = 0;
        for (int j = 0; j <= m; j++) {
            if (sm + add < j)
                add = j - sm;
            sm += str[j] - '0';
        }
        out << "Case #" << i + 1 << ": " << add << endl;
    }
    return 0;
}

