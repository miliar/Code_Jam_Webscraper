#include <iostream>
#include <cstring>
#include <climits>

using namespace std;

void solve(int n) {
    if(n == 0) {
        cout << "INSOMNIA";
        return ;
    }
    bool table[10];
    int cnt = 0;
    memset(table, 0, sizeof(table));
    unsigned long long prod = 1;
    for (long long i = 1; i < INT64_MAX / n ; ++i) {
        prod = i * n;
        long long t = prod;
        while(t) {
            int r = t % 10;
            if(!table[r]) {
                cnt++;
                table[r] = true;
            }
            t /= 10;
        }
        if(cnt == 10) {
            cout << prod;
            return ;
        }
    }
    cout<< "INSOMNIA";
}

int main(int argc, char *argv[]) {
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        int N;
        cin >> N;
        cout << "Case #" << i + 1 << ": ";
        solve(N);
        cout << endl;
    }
    return 0;
}
