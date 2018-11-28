#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main(int argc, char** argv) {
	int t;
	cin >> t;
	for(int iter = 0; iter < t; iter++) {
		cout << "Case #" << iter + 1 << ": ";
        
        string row;
        int k;
        int flip = 0;
        cin >> row >> k;
        for(int i = 0; i < row.size() - k + 1; i++) {
            if (row[i] == '-') {
                flip++;
                for(int j = i; j < i + k; j++) {
                    row[j] = (row[j] == '-') ? '+' : '-';
                }
            }
        }
        for(int i = row.size() - k + 1; i < row.size(); i++) {
            if (row[i] == '-') {
                flip = -1;
                break;
            }
        }

        if (flip >= 0) {
            cout << flip << endl;
        }
        else {
            cout << "IMPOSSIBLE" << endl;
        }
	}
	return 0;
}
