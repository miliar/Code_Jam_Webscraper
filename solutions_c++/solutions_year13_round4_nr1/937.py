#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

#define MX 1000002013

int N;

long long cost(int stops) {
    if (stops <= 0) {
        return 0;
    }
    return ((long long)stops * (2 * N - stops + 1)) / 2;
}

vector<int> travel;//people who go from i to i+1, i = 1..N-1

long long best(int beg, int end, int already) {
    if (beg >= end) {
        return 0;
    }
    // find min n of passengers who travel beg-to-end
    int minind = min_element(travel.begin() + beg, travel.begin() + end) - travel.begin();
    int minn = travel[minind];
//    cout << beg << "-" << end << " = had " << already << ", minn " << minn << " at " << minind << endl;
    return ((minn - already) * cost(end - beg) + best(beg, minind, minn) + best(minind + 1, end, minn)) % MX;
}

void solve(int ind) {
    // input
    int M;
    cin >> N >> M;
    travel.assign(N + 1, 0);
    long long propercost = 0;
    for (int i = 0; i < M; ++i) {
        int o, e, p;
        cin >> o >> e >> p;
        for (int j = o; j < e; ++j) {
            travel[j] += p;
        }
        propercost = (propercost + p * cost(e - o)) % MX;
    }
/*    for (int i = 1; i <= N; ++i) {
        cout << travel[i] << " ";
    }
    cout << endl;*/
    // process
    long long badcost = best(1, N, 0);
    // output
    cout << "Case #" << ind << ": " << (MX + propercost - badcost) % MX << endl;
}

int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        solve(i);
    }
}