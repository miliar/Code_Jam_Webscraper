//
//  main.cpp
//  GC-CountingSheep
//
//  Created by Akhil Verghese on 4/9/16.
//  Copyright © 2016 Akhil Verghese. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;

vector <int> getDigitsInNumber(int n) {
    vector <int> digits;
    while (n > 0) {
        digits.push_back(n%10);
        n/=10;
    }
    return digits;
}

int main(int argc, const char * argv[]) {
    
    int t;
    int x = 0;
    int ans, in;
    cin>>t;
    while (t--) {
        vector <bool> named(10,0);
        x++;
        cin>>in;
        ans = in;
        if (in == 0) {
            cout<<"Case #"<<x<<": "<<"INSOMNIA"<<endl;
            continue;
        }
        
        while (true) {
            vector<int> digits = getDigitsInNumber(ans);
            for (int i = 0; i < digits.size(); i++) {
                named[digits[i]] = 1;
            }
            bool done = true;
            for (int i = 0; i < named.size(); i++) {
                if (!named[i]) done = false;
            }
            if (done) break;
            ans += in;
        }
        cout<<"Case #"<<x<<": "<<ans<<endl;
    }
    return 0;
}
