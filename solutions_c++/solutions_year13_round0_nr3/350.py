#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

vector<string> number[105];

int get_min(int len, string s) {
    for (int i = 0; i < number[len].size(); i++) {
        if (number[len][i] >= s) {
            return number[len].size() - i;
        }
    }
    return 0;
}

int get_max(int len, string s) {
    for (int i = 0; i < number[len].size(); i++) {
        if (number[len][i] > s) {
            return i;
        }
    }
    return number[len].size();
}

int main() {
    ifstream numberStream("number.txt");
    while (!numberStream.eof()) {
        string s;
        getline(numberStream, s);
        number[s.length()].push_back(s);
    }
    numberStream.close();
    freopen("C-large-2.in", "r", stdin);
    freopen("c_large_out.txt", "w", stdout);
    
    
    int t;
    cin >> t;
    for (int task = 1; task <= t; task++) {
        string a, b;
        cin >> a >> b;
        int ans = 0;
        if (a.length() == b.length()) {
            int len = a.length();
            for (int i = 0; i < number[len].size(); i++) {
                if (a <= number[len][i] && number[len][i] <= b) {
                    ans++;
                }
            }
        } else {
            ans += get_min(a.length(), a);
            for (int j = a.length() + 1; j < b.length(); j++) {
                ans += number[j].size();
            }
            ans += get_max(b.length(), b);
        }
        cout << "Case #" << task <<": " << ans << endl;
    }

    return 0;
}
