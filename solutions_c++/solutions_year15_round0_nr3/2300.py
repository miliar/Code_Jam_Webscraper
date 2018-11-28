//
//  main.cpp
//  2015_Quali_C
//
//  Created by Jui Jung Li on 2015/4/12.
//  Copyright (c) 2015年 Jui Jung Li. All rights reserved.
//

#include <iostream>

using std::cin;
using std::cout;
using std::endl;
using std::string;

char multi(int &sign, char pre, int sign2, char post){
    sign *= sign2;
    if (pre == '1'){
        pre = post;
    }
    else if (pre == 'i'){
        if ( post == 'i'){
            sign *= -1;
            pre = '1';
        }
        if ( post == 'j'){
            pre = 'k';
        }
        if ( post == 'k'){
            sign *= -1;
            pre = 'j';
        }
    }
    else if (pre == 'j'){
        if ( post == 'i'){
            sign *= -1;
            pre = 'k';
        }
        if ( post == 'j'){
            sign *= -1;
            pre = '1';
        }
        if ( post == 'k'){
            pre = 'i';
        }
    }
    else if (pre == 'k'){
        if ( post == 'i'){
            pre = 'j';
        }
        if ( post == 'j'){
            sign *= -1;
            pre = 'i';
        }
        if ( post == 'k'){
            sign *= -1;
            pre = '1';
        }
    }
    return pre;
}
int main(int argc, const char * argv[]) {
    // insert code here...
    //std::cout << "Hello, World!\n";
    int T,T_i;
    cin >> T;
    for (T_i=1;T_i<=T;T_i++){
        int L, X;
        int ans = 0;
        int sign1;
        char pre,post;
        string str;
        cin >> L >> X >> str;
        sign1 = 1;
        pre = str[0];
        for (int j=1;j<str.length();j++){
            post = str[j];
            pre = multi(sign1,pre,1,post);
        }
//        printf("sign is [%d], pre is [%c]\n", sign1,pre);
        
        char final = pre;
        int  final_sign = sign1;
        for (int j=1;j<X;j++){
            final = multi(final_sign,final,sign1, pre);
        }
//        printf("sign is [%d], pre is [%c] after x cycles\n", final_sign,final);
        if (final_sign == -1 && final == '1'){
//            ans = 1;
            string final_str = str;
            for (int j=1;j<X;j++){
                final_str.append(str);
            }
//            cout << "final_str is " << final_str << endl;
            pre = '1';
            sign1 = 1;
            int j;
            for (j=0;j<final_str.length();j++){
                pre = multi(sign1,pre,1,final_str[j]);
                if (sign1 == 1 && pre == 'i'){
                    break;
                }
            }
            //cout << "first j is " << j << endl;
            if (j<final_str.length()){
                int start = j+1;
                pre = '1';
                sign1 = 1;
                for (j=start;j<final_str.length();j++){
                    pre = multi(sign1,pre,1,final_str[j]);
                    if (sign1 == 1 && pre == 'j'){
                        break;
                    }
                    
                }
                //cout << "2nd j is " << j << endl;
                
                if (j<final_str.length()){
                    ans = 1;
                }
            }
            
        }
        cout << "Case #" << T_i << ": ";
        cout << (ans==0?"NO":"YES");
        cout << endl;
    
    }
    return 0;
}
