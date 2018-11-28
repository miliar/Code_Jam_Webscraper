#include <iostream>
#include <cstring>
#include <sstream>
#include <algorithm>
using namespace std;

const int MAXN = 1000005;
bool flag[10];
int N, T;
stringstream mystream;
long long results[MAXN];

void PrecomputeResults() {
    bool completed;
    int digits_flagged;
    for (int x = 1; x < MAXN; ++x) {
        fill(flag, flag + 10, 0);
        completed = false;
        digits_flagged = 0;
        //cerr << "x = " << x << '\n';
        for (int i = 1; !completed; ++i) {
            int multiple = i * x;
            //cerr << "multiple = " << multiple << '\n';
            mystream.clear();
            mystream.str("");
            mystream << multiple;
            string str = mystream.str();
            //cout << str << '\n';
            for (size_t k = 0; k < str.length(); ++k) {
                if (flag[str[k] - '0'] == false) {
                    ++digits_flagged;
                    //cout << str[k] - '0' << " flagged \n";
                }
                flag[str[k] - '0'] = true;
                if (digits_flagged == 10) {
                    completed = true;
                    results[x] = multiple;
                }
            }
        }
    }
}

int main() {
    PrecomputeResults();
    results[0] = -1;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cin >> N;
        cout << "Case #" << i << ": ";
        if (results[N] == -1)
            cout << "INSOMNIA";
        else
            cout << results[N];
        cout << '\n';
    }
    return 0;
}
