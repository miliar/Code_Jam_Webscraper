#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
    int T; cin >> T;
    for (int t = 0 ; t < T ; t++) {
        int N = 0;
        string S = "";
        cin >> N >> S;
        int sLen = S.length();
        // cout << S << " " << sLen << endl;
        int req = 0;
        int sum = 0, prev_sum = 0;
        for (int i = 0 ; i < sLen ; i++) {
            int d = int(S[i] - '0');
            sum += d;
            int r = i - prev_sum;
            if (r > req) {
                req = r;
            }
            prev_sum = sum;
        }
        cout << "Case #" << t+1 << ": " << req << endl;
    }

    return 0;
}
