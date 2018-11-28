//
//  main.cpp
//  Counting-Sheep
//
//  Created by hassan zanjani on 4/9/16.
//  Copyright (c) 2016 moonlab. All rights reserved.
//

#include <iostream>

using namespace std;

int main() {
    int t,i,j,n,sum,counter,digi;
    cin >> t;
    for(i=0;i<t;i++) {
        cin >> n;
        if (n == 0) {
            cout << "Case #1: INSOMNIA" << endl;
        } else {
            counter = 0;
            int digits[10] = {0};
            do {
                counter++;
                sum = counter*n;
                do {
                    digi = sum%10;
                    digits[digi] = 1;
//                    cout << "digit" << digi << "-" << counter << endl;
                    sum /= 10;
                } while (sum > 0);
                sum = 0;
                for(j=0;j<10;j++) {
                    sum += digits[j];
                }
            } while (sum != 10);
            cout << "Case #" << i+1 << ": " << counter*n << endl;
        }
    }
    return (0);
}
