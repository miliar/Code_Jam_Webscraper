//
//  countingSheep.cpp
//  
//
//  Created by Will Sawyer on 4/9/16.
//
//

#include <stdio.h>
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text

int main() {
    long long n, t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cin >> n;
        bool tracker[10] = {false};
        long long digitsSeen = 0, current = 0, mult = 1;
        if(n==0){
            cout << "Case #" << i << ": " << "INSOMNIA" << endl;
            continue;
        }
        
        while(digitsSeen != 10){
            current = mult*n;
            while(current!=0){
                if(!tracker[current%10]){
                    tracker[current%10] = true;
                    digitsSeen++;
                }
                current/=10;
            }
            mult++;
        }
        
        
        cout << "Case #" << i << ": " << (n*(mult-1)) << endl;
    }
    return 0;
}