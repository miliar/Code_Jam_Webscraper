#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <map>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstring>

using namespace std;

const int max_op = 101;

long long A;
long long cnt;
vector<long long> motes;

long long solve(int curSize, int moteNum) {
    if (moteNum == cnt)
        return 0;
    if (curSize > motes[moteNum])
        return solve(curSize + motes[moteNum], moteNum + 1);

    int op1 = max_op, op2 = max_op;

    if (curSize > 1) {
        op1 = 1 + solve(curSize + curSize - 1, moteNum);
    }

    op2 = 1 + solve(curSize, moteNum + 1);

    return min(op1, op2);
}

int main() {
//    freopen("test.in","r", stdin);
  //  freopen("test.out","wt", stdout);

    int T;
    cin >> T;

    for (int t = 1; t <= T; t++) {
        cin >> A >> cnt;
        motes = vector<long long>(cnt, 0);
        for (int i = 0; i < cnt; i++)
            cin >> motes[i];

        sort(motes.begin(), motes.end());

        printf("Case #%d: %lld\n", t, solve(A, 0));
    }
}
