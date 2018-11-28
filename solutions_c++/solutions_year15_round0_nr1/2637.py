#include <stdio.h>
#include <iostream>
#include <fstream>
#define MAX (1001)

using namespace std;

int t, n;
string s;

int main(){
    ifstream in;
    in.open("in.txt");
    ofstream out;
    out.open("out.txt");
    in >> t;
    for (int i = 0 ; i < t ; ++i) {
        in >> n >> s;
        int sum = 0;
        int result = 0;
        for (int j = 0 ; j < n + 1 ; ++j) {
            if (sum < j) {
                result += j - sum;
                sum = j;
            }
            sum += s[j] - '0';
        }
        out << "Case #" << i + 1 << ": " << result << endl;
    }
    in.close();
    out.close();
}