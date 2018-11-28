//
//  main.cpp
//  B
//
//  Created by Andrey Cherevko on 4/9/16.
//  Copyright © 2016 Andrey Cherevko. All rights reserved.
//

#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
	 freopen ("inputlarge.txt", "r", stdin);
	 freopen ("outputlarge.txt", "w", stdout);
	 int t;
    cin >> t;
    string s;
    for (int tt = 0; tt < t; tt++) {
        cin >> s;
        int ans = 0;
        int n = (int)s.length();
        for (int i = 1; i < n; i++) {
            if (s[i] != s[i - 1])
                ans++;
        }
        if (s[n - 1] == '-')
            ans++;
        printf ("Case #%d: %d\n", tt + 1, ans);
    }
    return 0;
}
