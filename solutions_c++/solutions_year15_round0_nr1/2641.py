//
//  main.cpp
//  2015_Quali
//
//  Created by Jui Jung Li on 2015/4/11.
//  Copyright (c) 2015年 Jui Jung Li. All rights reserved.
//

#include <iostream>

using std::cin;
using std::cout;
using std::endl;
using std::string;

int main(int argc, const char * argv[]) {
    // insert code here...
    //std::cout << "Hello, World!\n";
    int T,T_i;
    int ans;
    int Smax;
    int j;
    int total;
    string str;
    cin >> T;
    for (T_i=1;T_i<=T;T_i++){
        ans = 0;
        total = 0;
        cin >> Smax >> str;
        for (j=0;j<=Smax;j++){
            //cout << "j is " << j << ", " << str[j] << endl;
            if (total + ans < j) {
                ans = j- total;
            }
            total += (str[j]-'0');
        }
        cout << "Case #" << T_i << ": " << ans << endl;
    }
    return 0;
}
