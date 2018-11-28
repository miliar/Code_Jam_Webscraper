#include <iostream>
#include <vector>

using namespace std;

bool check(vector<int> const& v) {
    for (int i = 0; i < 10; ++i) {
        if (v[i] == 0)
            return false;
    }
    return true;
}

void get_nums(int n, vector<int> &v) {
    while (n > 0) { 
        v[n % 10]++;
        n /= 10;
    }
}

int main() {
    int cases;
    cin >> cases;

    for (int i = 0; i  < cases; ++i) {
        int n, count = 1;
        cin >> n;
        if (!n) {
            cout << "Case #" << i + 1 << ": INSOMNIA" << endl;
            continue;
        }
        
        vector<int> frequency (10);
        while (!check(frequency)) {
            get_nums(n * count, frequency);
            count++;
        }
        cout << "Case #" << i + 1 << ": " << n * (count - 1) << endl;
    }     
    return 0;
}
