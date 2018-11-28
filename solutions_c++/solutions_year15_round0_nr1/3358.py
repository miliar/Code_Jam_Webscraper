#include <bits/stdc++.h>

using namespace std;

ifstream in;
ofstream out;

int solve() {

    int smax; in >> smax;

    string str; in >> str;

    int add = 0;
    int current = str[0] - '0';

    for (int i = 1; i < str.size(); i++) {
        if (current < i) {
            add += i - current;
            current = i + str[i] - '0';
        }
        else {
            current = current + str[i] - '0';
        }
    }

    return add;

}

int main() {

    in.open("C:\\Users\\Alex\\ClionProjects\\GoogleCodeJam\\input.txt");
    out.open("C:\\Users\\Alex\\ClionProjects\\GoogleCodeJam\\output.txt");

    int t; in >> t;

    for (int i = 0; i < t; i++)  {
        out << "Case #" << i + 1 << ": " << solve() << endl;
    }

    return 0;
}