//
//  main.cpp
//  Revenge of the Pancakes
//
//  Created by hassan zanjani on 4/9/16.
//  Copyright (c) 2016 moonlab. All rights reserved.
//

#include <iostream>
#include <string.h>

using namespace std;

int main() {
    int i,j,t,n,counter,changest;
    //changest: 0:no 1:yes
    char str[100],digitst;
    cin >> t;
    for(i=0;i<t;i++) {
        cin >> str;
        n = strlen(str);
        if (n == 1) {
            if (str[0] == '-') {
                cout << "Case #" << i+1 << ": " << "1" << endl;
            } else {
                cout << "Case #" << i+1 << ": " << "0" << endl;
            }
        } else {
            digitst = str[n-1];
            counter = 0;
            changest = 0;
            for (j=n-2; j >= 0; j--) {
                if (str[j] != digitst) {
                    counter++;
                    digitst = str[j];
                    changest = 1;
                }
            }
            if (str[n-1] == '-') {
                counter ++;
            }
            cout << "Case #" << i+1 << ": " << counter << endl;
        }
    }
    return (0);
}
