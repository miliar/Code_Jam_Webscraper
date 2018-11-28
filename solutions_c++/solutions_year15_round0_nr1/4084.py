#include <iostream>
#include <string>

using namespace std;

void solve(int testcase);

int main() {
    int N;
    cin >> N;
    for(int i=0; i<N; ++i)
        solve(i+1);
}

void solve(int testcase) {
    unsigned shymax;
    cin >> shymax;
    string shycounts;
    cin >> shycounts;
    unsigned sum = 0;
    unsigned needed = 0;
    for(int i = 0; i<=shymax; ++i){
        unsigned numi = (char)shycounts[i] - '0';
        if(sum < i) {
            unsigned add = i - sum;
            needed += add;
            sum += add;
        }
        sum += numi;
    }
    cout << "Case #" << testcase << ": " << needed << endl;
}
