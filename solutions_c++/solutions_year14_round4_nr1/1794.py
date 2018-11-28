//
//  main.cpp
//  CodeJam
//
//  Created by Jayvic on 14-5-31.
//  Copyright (c) 2014年 Jayvic. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <cstring>
#include <stack>

using namespace std;

int a[10010];
bool b[10010];

int solve(void)
{
    int n;
    int s;
    cin >> n >> s;
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }
    sort(a, a + n);
    
    stack<int> sp;
    while (!sp.empty()) {
        sp.pop();
    }
    memset(b, 0, sizeof(b));
    int ans = 0;
    int p = 0;
    for (int i = n - 1; i >= 0; --i) {
        if (!b[i]) {
            for (; p < i; ++p) {
                if (a[p] + a[i] <= s && !b[p]) {
                    sp.push(p);
                } else {
                    break;
                }
            }
            if (!sp.empty() && sp.top() == i) {
                sp.pop();
            }
            if (sp.empty()) {
                ++ans;
                b[i] = true;
            }
            else
            {
                ++ans;
                b[sp.top()] = true;
                b[i] = true;
                sp.pop();
            }
        }
    }
    return ans;
}

int main()
{
    // insert code here...
    int numTest;
    cin >> numTest;
    for (int testCase = 1; testCase <= numTest; ++testCase) {
        cout << "Case #" << testCase << ": " << solve() << endl;
    }
    return 0;
}

