//
//  main.cpp
//  2015_Quali_D
//
//  Created by Jui Jung Li on 2015/4/12.
//  Copyright (c) 2015年 Jui Jung Li. All rights reserved.
//

#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main(int argc, const char * argv[]) {
    // insert code here...
    //std::cout << "Hello, World!\n";
    int T,T_i;
    cin >> T;
    for (T_i=1;T_i<=T;T_i++){
        int X,R,C;
        int ans = 0;
        cin >> X >> R >> C;
        if (R>C){
            int tmp = R;
            R= C;
            C= tmp;
        }
        // R<=C
        if (X==1){
            ans = 0;
        }
        else if (X==2){
            ans = ((R*C)%2==0)? 0 : 1;
        }
        else if (X==3){
            ans = (R==1 || C==1 || (R*C)%3!=0)? 1 : 0;
        }
        else if (X==4){
            
            if (R<=2){
                ans =1;
            }
            else if (R==3 && C==3) {
                ans = 1;
            }
            else {
                ans = 0;
            }
        }
        cout << "Case #" << T_i << ": " << (ans==0?"GABRIEL":"RICHARD") << endl;
    }
    return 0;
}
