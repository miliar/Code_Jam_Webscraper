#include <iostream>
#include <string>
#include <vector>
using namespace std;

int solve(int smax, string input) {
    int noshy = 0;
    int nfriend = 0;
    for (int i=0; i<=smax; i++) {
        int si = input[i] - '0';
        if (noshy < i) {
            nfriend += i-noshy;
            noshy = i;
        }
        noshy += si;
    }
    return nfriend;
}

int main() {
    int T;
    cin >> T;
    int smax;
    string input;
    vector<int> solution(T, 0);
    for (int i=0; i<T; i++) {
        cin >> smax >> input;
        cout << "Case #" << i+1 << ": " << solve(smax, input) << endl;
    }

    return 0;
}
