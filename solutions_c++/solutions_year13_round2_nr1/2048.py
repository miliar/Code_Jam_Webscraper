#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cstring>
#include <cmath>

using namespace std;

int T, t, N, n, mote;
long long A;
int result;
vector<int> motes;

int solve(long long a, int pos, int ops) {
    while(pos<N && motes[pos]<a) { // A eats all possible motes starting in pos
        a += motes[pos];
        ++pos;
    }
    if(pos==N) return ops;
    // A can't eat mote in pos
    int ops1 = solve(a, pos+1, ops+1); // removing mote in pos
    int nextA = a;
    while(nextA <= motes[pos]) {
        nextA += nextA-1;
        ++ops;
    }
    int ops2 = solve(nextA, pos, ops); // adding a new mote, and eating it
    return min(ops1, ops2);
}

int main() {
    cin >> T; // number of test cases
    for(t=1; t<=T; ++t) { // for each test case:
        result = 0;
        motes.clear();
        cin >> A >> N;
        for(n=0; n<N; ++n) {
            cin >> mote;
            motes.push_back(mote);
        }
        sort(motes.begin(), motes.end());
        if(A==1) result=N; // we delete all
        else {
            result = solve(A, 0, 0);
        }
        cout << "Case #" << t << ": " << result << endl;
    }
    return 0;
}