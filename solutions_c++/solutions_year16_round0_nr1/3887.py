#include <iostream>
#include <vector>

using namespace std;

bool judge(vector<int> hash) {
    for (int i = 0; i < hash.size(); i++)
        if (hash[i] == 0) return false;
    return true;
};

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    vector<int> hash(10);
    int n;
    cin >> n;
    int caseNum = n;
    while (n--) {
        int num;
        cin >> num;
        for (int i = 1; i <= 100; i++) {
            int now = num * i;
            while (now) {
                int digit = now % 10;
                now /= 10;
                if (hash[digit] == 0) hash[digit] = 1;
            }
            if (judge(hash)) {
                cout << "Case #" << caseNum - n << ": " << num * i << endl;
                break;
            }
        }
        if (!judge(hash)) cout << "Case #" << caseNum - n << ": INSOMNIA\n";
        for (int i = 0; i < 10; i++) hash[i] = 0;
    }
    return 0;
}