#include <bits/stdc++.h>
using namespace std;

vector<int> readData(istream &in) {
    int smax;
    in >> smax;
    while (isspace(in.get())) {}
    in.unget();
    vector<int> result(smax + 1);
    for (int i = 0; i <= smax; ++i) {
        result[i] = (in.get() - '0');
    }
    return result;
}

int solve(istream &in) {
    vector<int> v = readData(in);
    int result = 0;
    int standing = 0;
    for (int i = 0; i < (int)v.size(); ++i) {
        if (v[i] == 0)
            continue;
        if (standing < i) {
            result += i - standing;
            standing = i;
        }
        standing += v[i];
    }
    return result;
}

int main() {
    ifstream in("a.txt");
    ofstream out("a_out.txt");
    int t;
    in >> t;
    for (int i = 1; i <= t; ++i) {
        out << "Case #" << i << ": " << solve(in) << '\n';
    }
}
