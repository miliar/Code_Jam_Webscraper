#include<iostream>
#include<fstream>
#include<string>
#include<map>
#include<vector>

#define ii pair<int, int>
#define PB push_back
#define isLeap(x) (((x) % 4 == 0 && (x) % 100 != 0) || ((x) % 400 == 0))

using namespace std;

int nTest, n, times[10000], ans1, ans2, cases;

int main() {
    freopen("Inputs.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> nTest;

    while(nTest--) {
        cin >> n;
        ans1 = ans2 = 0;
        for(int i = 0; i < n; i++) cin >> times[i];

        for(int i = 1; i < n; i++) ans1 += (times[i - 1] > times[i] ? times[i - 1] - times[i] : 0);

        int eat = 0;
        for(int i = 1; i < n; i++) eat = max(times[i - 1]- times[i], eat);

        //cout << eat << endl;

        for(int i = 0; i < n-1; i++) ans2 += min(eat, times[i]);

        cout << "Case #" << ++cases << ": " << ans1 << " " << ans2 << "\n";


    }
}

