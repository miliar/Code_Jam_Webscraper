#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <cstring>

using namespace std;


void alg() {
    int result(0);
    int magicNumber;
    int lineNum(0);
    string line;
    vector<int> nums;
    
    cin >> lineNum;
    getline(cin, line);
    for (int i(1); i <= 4; ++i) {
        if (i == lineNum) {
            for (int j(1); j <= 4; ++j) {
                int num = 0;
                cin >> num;
                nums.push_back(num);
            }
        }
        getline(cin, line);
    }
  
    cin >> lineNum;
    getline(cin, line);
    for (int i(1); i <= 4; ++i) {
        if (i == lineNum) {
            for (int j(1); j <= 4; ++j) {
                int num = 0;
                cin >> num;
                if(num == nums[0] || num == nums[1] || num == nums[2] || num == nums[3]) {
                    magicNumber = num;
                    ++result;
                }
            }
        }
        getline(cin, line);
    }
    
    
    switch (result) {
        case 0:
            cout << "Volunteer cheated!" << endl;
            break;
        case 1:
            cout << magicNumber << endl;
            break;
        default:
            cout << "Bad magician!" << endl;
            break;
    }
}

int main() {
    int n_cases(0);
    cin >> n_cases;
    
    for (int test_case = 1; test_case <= n_cases; test_case++) {
      cout << "Case #" << test_case << ": ";
      alg();
    }

    return EXIT_SUCCESS;
}
