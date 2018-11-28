#include <iostream>
#include <ostream>

#include <deque>
#include <list>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

#include <string>
#include <sstream>

using namespace std;

static bool debug = false;

#define P(v) if (debug) cout << #v << ": " << v << endl;
#define O(i, v) cout << "Case #" << i + 1 << ": " << v << endl;

template <typename T>
void printc(const T& container)
{
    for (const auto& i: container) {
        cout << " " << i;
    }
    cout << endl;
}

#define PC(c) if (debug) printc(container);


void calc(vector<int> *inp)
{
    vector<int>& in = *inp;
    int sum = 0;
    do {
        sum = 0;
        int max = -1;
        int secondMax = -1;
        P(in.size())
        for (size_t j=0; j<in.size(); ++j) {
            sum += in[j];
            if (max == -1 || (in[j] != 0 && in[j] >= in[max])) {
                if (max != -1) {
                    secondMax = max;
                }
                max = j;
            }
        P(sum) P(max) P(secondMax)
        }
        if (in[secondMax] > sum - in[secondMax] - 1) {
            cout << " " << (char)('A' + max) << (char)('A' + secondMax);
            in[max] -= 1;
            in[secondMax] -= 1;
            sum -= 2;
        }
        else {
            cout << " " << (char)('A' + max);
            in[max] -= 1;
            sum -= 1;
        }
    } while (sum > 0);
}


int main()
{
    int T = 0;
    cin >> T;
    P(T);
    for (int i=0; i < T; ++i) {
        int N = 0;
        cin >> N;
        P(N);
        vector<int> in(N);
        for (int j=0; j < N; ++j) {
            cin >> in[j];
            P(in[j])
        }
        cout << "Case #" << i + 1 << ":";
        calc(&in);
        cout << endl;
    }

    return 0;
}
