#include <vector>
#include <list>
#include <map>
#include <set>
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
 
int main() {
    int test_cnt;

    cin >> test_cnt;
    for(int i = 0; i < test_cnt; i++) {
        int n;
        int prev = 0;
        int max_diff = 0;
        int res1 = 0, res2 = 0;
        vector<int> tmp;
        cin >> n;
        while(n--) {
            int cur, diff;
            cin >> cur;
            tmp.push_back(cur);
            diff = prev - cur;
            if(diff > 0) {
                res1 += diff;
                max_diff = max(max_diff, diff);       
            }
            prev = cur;
        }
        int size = tmp.size(); 
        prev = tmp[0];
        for(int j = 0; j < size - 1; j++) {
            if(tmp[j] < max_diff) res2 += tmp[j]; 
            else res2 += max_diff;
        }

        tmp.clear();
        cout << "Case #" << i+1 << ": "; 
        cout << res1 << " " << res2 << endl;
    }
   
    return 0;
}
 
