#include <iostream>
#include <bitset>
#include <sstream>
#include <memory>
#include <limits>
#include <list>
#include <stack>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <string>
#include <vector>
#include <algorithm>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

using namespace std;

long long mod = 1000000007;

int solve() {
    string str;
    cin >> str;
    
    str.push_back('*');
    
    string s;
    
    for (int i = 1; i < str.size(); ++i) {
        if (str[i] != str[i-1]) {
            s.push_back(str[i-1]);
        }
    }
    
    if (s.size() == 1) {
        if (s[0] == '-') return 1;
        return 0;
    }
    
    stack<char> st;
    for (int i = s.size() - 1; i >=0; --i) {
        st.push(s[i]);
    }
    
    int res = 0;
    while (st.size() != 1) {
        char c1 = st.top(); st.pop();
        char c2 = st.top(); st.pop();
        
        if (c1 == '+' && c2 == '-') {
            res += 2;
        } else if (c1 == '-' && c2 == '+') {
            res += 1;
        }
        st.push('+');
    }
    
    return res;
    
}

int main() {
    std::cout.precision(15);
    std::ios_base::sync_with_stdio(false);
    
    int t;
    cin >> t;
    for (int i = 1; i <=t ; ++i) {
        cout << "Case #" << i << ": " << solve() << endl;
    }
    
    
    return 0;
}