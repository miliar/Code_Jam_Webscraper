#include <iostream>
#include <fstream>
using namespace std;

int membersNeeded(int n, string s) {
    if (n == 0)
        return 0;
    int num_needed = 0;
    int offset = s[0] - '0';
    for (int i = 1; i <= n; i++) {
        int temp = i - offset;;
        int digit_num = s[i] - '0';
        if (temp > 0) {
            num_needed += temp;
        }
        offset += (temp > 0 ? temp : 0) + digit_num;
    }
    return num_needed;
}

int main(){
    ifstream infile("A-large.in", ios::in);
    ofstream outfile("A-large.out", ios::out);
    int n;
    infile >> n;
    for (int i = 0; i < n; i++) {
        int a;
        string b;
        infile >> a >> b;
        int c = membersNeeded(a, b);
        outfile << "Case #" << i + 1 << ": " << c << endl;
    }

    return 0;
}
