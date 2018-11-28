//
//  main.cpp
//  2015_Quali_B
//
//  Created by Jui Jung Li on 2015/4/11.
//  Copyright (c) 2015年 Jui Jung Li. All rights reserved.
//

#include <iostream>

using std::cin;
using std::cout;
using std::endl;
using std::string;
int find_min(int *P, int max){
//    printf("max is [%d]\n", max);
    if (max <= 3) {
        return max;
    }
    int n = P[max];
    
    //2
    P[max/2] +=n;
    P[(max+1)/2] +=n;
    int new_max = 0;
    for (int i=max-1;i>=0;i--){
        if (P[i]!=0){
            new_max = i;
            break;
        }
    }
//    printf("for max [%d], new max is [%d]\n", max, new_max);
    int ans = find_min(P, new_max);
//    printf("for 2 part, ans is [%d] for max [%d]\n", ans, max);
    //3
    P[max/2] -=n;
    P[(max+1)/2] -=n;
    
    P[max/3] += n;
    P[(max+1)/3] += n;
    P[(max+2)/3] += n;
    
    new_max = 0;
    for (int i=max-1;i>=0;i--){
        if (P[i]!=0){
            new_max = i;
            break;
        }
    }
    int ans3 = find_min(P, new_max);
    P[max/3] -= n;
    P[(max+1)/3] -= n;
    P[(max+2)/3] -= n;

//    printf("for 3 part, ans is [%d] for max [%d]\n", ans3, max);
    
    if ( ans3+n < ans ) {
//        printf("for max [%d] choose 3 part")
        ans = ans3+n;
    }
    if ( ans + n < max ) {
        return ans + n ;
    }
    return max;
}
int main(int argc, const char * argv[]) {
    // insert code here...
    //std::cout << "Hello, World!\n";
    int T,T_i;
    int D;
    cin >> T;
    for (T_i=1;T_i<=T;T_i++){
        cin >> D;
        int ans = 0;
        int P[1001] = {0};
        int tmp;
        int max = 0;
        for (int j=0;j<D;j++)
            P[j] = 0;
        for (int j=0;j<D;j++){
            cin >> tmp;
            P[tmp]++;
            if (tmp>max){
                max = tmp;
            }
        }
        ans = find_min(P,max);
        cout << "Case #" << T_i << ": " << ans << endl;
    }
    return 0;
}
