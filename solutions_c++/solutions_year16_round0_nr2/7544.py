#include <iostream>
using namespace std;

int main() {
	int t;
	cin >> t;
	string data;
	for (int i = 1; i <= t; i++) {
	    cin >> data;
	    char c[] = {'-', '+'};
	    int ind = 0;
	    int len = data.length();
	    int cnt = 0;
	    for (int j = len-1; j >= 0; j--) {
	        if (data[j] == c[ind]) {
	            ind = (ind + 1)%2;
	            cnt++;
	        }
	    }
	    cout << "Case #" << i << ": " << cnt << endl;
	}
	return 0;
}
