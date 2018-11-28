#include <set>
#include <map>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <list>
#include <cassert>
#include <climits>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <fstream>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <stdexcept>

using namespace std;

bool isP(long long a) {
    string s;
    long long b = a;
    while(b != 0) {
        s += ('0' + b%10);
        b /= 10;
    }
//    reverse(s.begin(), s.end());
    for(int i = 0; i < s.size()/2; i++) {
        if(s[i] != s[s.size()-1-i]) {
            return false;
        }
    }

    return true;
}

vector<long long> genSmall(long long n) {
    vector<long long> nums;
    for(int i = 1; i*i < n+1; i++) {
        if(isP(i) && isP(i*i)) {
            nums.push_back(i*i);
        }
    }

    return nums;
}

long long countP(long long A, long long B, vector<long long> &nums) {
    long long lcv = 0;
//    cout << nums[lcv] << endl;
    while(A > nums[lcv] && lcv != nums.size()) {
        lcv++;
    }
//    cout << lcv << " " << A << endl;
    long long total = 0;
    while(B >= nums[lcv] && lcv != nums.size()) {
        lcv++;
        total++;
    }

    return total;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    long long T;
    cin >> T;

    vector<long long> nums = genSmall(10000000);
    for(long long c = 1; c < T+1; c++) {
        long long A, B;
        cin >> A >> B;
        cout << "Case #" << c << ": " << countP(A,B,nums) << endl;
    }

//    for(int i = 0; i < nums.size(); i++) {
//        cout << nums[i] << " " << sqrt(nums[i]) << endl;
//    }

    return 0;
}

