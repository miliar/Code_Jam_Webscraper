#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        string data;
        cin >> data;
        int len = data.length();
        string result = "";
        result += data[0];
        for (int j = 1; j < len; j++) {
            if (data[j] >= result[0]) {
                result = data[j] + result;
            } else {
                result += data[j];
            }
        }
        cout << "Case #" << i << ": " << result << endl;
    }
	return 0;
}