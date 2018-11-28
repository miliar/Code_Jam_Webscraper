//
//  main.cpp
//  round1
//
//  Created by wangdongfang on 15/4/11.
//  Copyright (c) 2015年 _. All rights reserved.
//

#include <iostream>
using std::cin;
using std::cout;
using std::endl;

int audience_num [1005];
int S_max;

void find(int round) {
    int ans = 0;
    int current_stand = audience_num[0];
    for (int i = 1; i <= S_max; i++) { // level i
        if (current_stand >= i) {
            current_stand += audience_num[i];
        } else if (current_stand < i && audience_num[i] > 0){
            ans = ans + (i - current_stand);
            current_stand = current_stand + audience_num[i]+ i - current_stand;
        }
    }
    cout << "Case #" << round << ": " << ans << endl;
}

int main() {

    int T;
  
    cin >> T;
    
    
    for (int i = 0; i < T; i++) {
       
        cin >> S_max;
        for (int j = 0; j <= S_max; j++) {
            char num;
            cin >> num;
            audience_num[j] = num - '0';
        }
        find(i+1);
    }
    return 0;
}
