//
//  main.cpp
//  prob2
//
//  Created by Juan Pablo Peñaloza Botero on 4/8/16.
//  Copyright © 2016 Juan Pablo Peñaloza Botero. All rights reserved.
//

#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    
    int t = 0;
    
    cin >> t;
    
    for (int i =1; i <= t; i++) {
        string str;
        cin >> str;
        int cont = 0;
        bool flag;
        if (str[0] == '+') {
            flag = false;
        } else {
            flag = true;
        }
        for (int j = 0; j < str.size(); j++) {
            if (str[j] == '-' && flag) {
                cont++;
                flag = false;
            }
            if (str[j] == '+' && !flag) {
                if (j != str.size() - 1 && str[j+1] == '-') {
                    cont++;
                    flag = true;
                }
            }
        }
        cout <<"Case #" << i<<": " << cont << endl;
    }
    return 0;
}
