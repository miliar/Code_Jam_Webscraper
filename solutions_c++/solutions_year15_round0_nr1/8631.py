#include <iostream>
#include <vector>

using namespace std;

int main(int argc, const char *argv[])
{
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        /* code */
        int Smax;
        //vector<int> S(Smax + 1, 0);
        int S = 0;
        cin >> Smax;

        char c;
        int to_invite = 0;
        for(int j = 0; j <= Smax; ++j) {
            cin >> c;
            //S[i] = c - '0';
            int si = c - '0';

            int t = max(j - S, 0);
            to_invite += t;
            S += t;
            S += si;
        }

        cout << "Case #" << i << ": " << to_invite << endl;
    }
    return 0;
}
