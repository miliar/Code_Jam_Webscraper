#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int solve() {
    int s_max;
    string nums;
    
    cin >> s_max;
    cin >> nums;
    
    vector<int> s_to_people(s_max + 1, 0);
    for (int i = 0; i < nums.size(); ++i) {
        s_to_people[i] = nums[i] - '0';
    }
    vector<int> sums(s_max + 1, 0);
    sums[0] = s_to_people[0];
    int res = 0;
    for (int i = 1; i <= s_max; ++i) {
        if (sums[i - 1] < i && s_to_people[i] > 0) {
            res += i - sums[i - 1];
            sums[i - 1] = i;
        }
        sums[i] = sums[i - 1] + s_to_people[i];
    }
    return res;
}


int main() {
    
    int t;
    cin >> t;
    
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": " << solve() << endl;
    }
    
    return 0;
}
