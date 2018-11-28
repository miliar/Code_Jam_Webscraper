#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    int num;
    cin >> num;
    for (int x=1; x<num+1; x++) {
        int N;
        cin >> N;
        if (N == 0) {
            cout << "Case #" << x << ": INSOMNIA" << endl;
        } else {
            int n = N;
            bool done = false;
            vector<bool> seen;
            for (int i=0; i<10; i++) {
                seen.push_back(false);
            }
            while (true) {
                string s_n = to_string(n);
                for (int i=0; i<s_n.length(); i++) {
                    int a = s_n[i]-48;
                    seen[a] = true;
                }
                bool test = true;
                for (int i=0; i<10; i++) {
                    if (seen[i] == false) {
                        test = false;
                    }
                }
                if (test) {
                    cout << "Case #" << x << ": " << n << endl;
                    break;
                }
                n += N;
            }
        }
    }
}
