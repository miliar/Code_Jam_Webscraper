#include <bits/stdc++.h>

using namespace std;

vector<int> readData(istream &in) {
    int d;
    in >> d;
    vector<int> data(d);
    for (int i = 0; i < d; ++i) {
        in >> data[i];
    }
    return data;
}

template <class Cont>
int len(const Cont &c) {
    return static_cast<int>(c.size());
}

int solve(istream &in) {
    vector<int> cakes = readData(in);
    int answer = *max_element(cakes.begin(), cakes.end());
    for (int i = 1; i < answer; ++i) {
        int additionalDays = 0;
        for (int j = 0; j < len(cakes); ++j)
            additionalDays += (cakes[j] - 1) / i;
        if (answer > additionalDays + i)
            answer = additionalDays + i;
    }
    return answer;
}


int main() {
    ifstream in("b.txt");
    ofstream out("b_out.txt");
    //ostream &out = cout;
    int t;
    in >> t;
    for (int i = 1; i <= t; ++i) {
        out << "Case #" << i << ": " << solve(in) << '\n';
    }
}

