#include <iostream>
#include <cstdint>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_set>

using namespace std;

uint64_t getMinDivisor(uint64_t num) {
	long breakNum = ceil(sqrt(num));
	if (num == 2) { return num;}
	for (uint64_t i = 2; i <= breakNum; i++) {
		if (num % i == 0) {
			return i;
		}
	}
	return num;
}

uint64_t stringToBase(const string& s, int base) {
    uint64_t sum = 0;
    uint64_t mult = 1;
    for (int i = s.length() - 1; i >= 0; --i) {
        sum += (s[i] - '0') * mult;
        mult *= base;
    }
    return sum;
}

vector<uint64_t> getDivisorVector(const string& s) {
    vector<uint64_t> v;
    for (uint64_t i = 2; i <= 10; ++i) {
        // Convert string to current base
        uint64_t curr = stringToBase(s, i);
        uint64_t div = getMinDivisor(curr);
        // If it's ever prime, clear the vector and return
        if (div == curr) {
            v.clear();
            return v;
        }
        // Add it to the vector
        v.push_back(div);
    }
    return v;
}

// INPUT: T = 1, N: lenght, J: number of outputs
int main() {
    int T;
    cin >> T;
    int N, J;
    cin >> N >> J;
    cout << "Case #1:" << endl;
    //N = 6; J = 3;
    int cnt = 0;
    for (int j = 0; j < 262144; ++j) {
        // Pad with 0s 
        string s(N - 2, '0');

        // Iterate over the existing bits and set
        // the corresponding ones
        for (int i = 0; i < N - 2; ++i) {
            s[N - 2 - i - 1] = (j & (1 << i)) ? '1' : '0';
        }
        s = "1"s + s + "1"s;

        // Generate the candidate string
        vector<uint64_t> v1 = getDivisorVector(s);
        if (!v1.empty()) {
            cout << s << " ";
            //cout << "_" << j << "_";
            for (int i = 0; i < v1.size(); ++i) {
                if (i == v1.size() - 1) {
                    cout << v1[i] << endl;
                } else {
                    cout << v1[i] << " ";
                }
            }
            cnt++;
        }
        if (cnt == J) {
            break;
        }
    }
}
