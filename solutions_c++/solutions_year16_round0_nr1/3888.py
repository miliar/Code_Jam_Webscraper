//
//  main.cpp
//  A
//
//  Created by Andrey Cherevko on 4/9/16.
//  Copyright © 2016 Andrey Cherevko. All rights reserved.
//

#include <iostream>

using namespace std;

bool digits[10];

bool parseAndCheck (int n) {
	 while (n > 0) {
        digits[n % 10] = true;
        n /= 10;
    }
    bool ans = true;
    for (int i = 0; i < 10; i++) {
        if (!digits[i])
            ans = false;
    }
    return ans;
}

int main(int argc, const char * argv[]) {
    
    freopen ("inputlarge.txt", "r", stdin);
	 
	 freopen ("outputlarge.txt", "w", stdout);
	 int t;
    cin >> t;
    for (int tt = 0; tt < t; tt++) {
        int n;
        cin >> n;
        bool flag = false;
        cout << "Case #" << tt + 1 << ": ";
        for (int i = 1; i <= 100; i++) {
            if (parseAndCheck(n * i)) {
                cout << i * n << endl;
                flag = true;
                break;
            }
        }

        if (!flag)
            cout << "INSOMNIA" << endl;

        for (int i = 0; i < 10; i++)
            digits[i] = false;

    }
    return 0;
}
