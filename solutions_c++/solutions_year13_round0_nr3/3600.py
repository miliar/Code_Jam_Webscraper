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
#include <fstream>

using namespace std;

class Solution {
public:
    Solution() {
        input = freopen("data.in" , "r" , stdin);
        output = freopen("data.out" , "w" , stdout);
    }

    void solve() {
        int T;
        cin >> T;
        for(int i = 1; i <= T; i++)  {
            cout << "Case #" << i << ": " << solveCase() << endl;
        }
    }

private:
    int solveCase() {
        long long A, B;
        cin >> A >> B;
        long long num = A;
        int res = 0;
        while (num <= B) {
            long long root = sqrt(num);
            if (root*root == num && isPalindrome(num) && isPalindrome(root))
                res++;
            num++;
        }
        return res;
    }

    bool isPalindrome(long long x) {
        if (x < 0) return false;
        long long d = 1;
        while (x / d >= 10) d *= 10; 
        while (x != 0) {
            long long l = x / d;
            long long r = x % 10; 
            if (l != r) return false;
            x = (x % d) / 10; 
            d /= 100;
        }   
        return true;
    }   

    long long sqrt(long long x) {
        if(x < 2) return x;
        long long l = 0;
        long long u = 1 + (x / 2); 
        while(l+1 < u) {
            long long m = l + (u - l) / 2;
            long long p = m * m;
            if (p == x)
                return m;
            if(p > x)
                u = m;
            else
                l = m;
        }   
        return l;
    }

    FILE * input;
    FILE * output;
};

int main() {
    Solution sol;
    sol.solve();
}
