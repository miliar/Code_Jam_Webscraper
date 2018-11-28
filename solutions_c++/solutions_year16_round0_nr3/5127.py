//
//  main.cpp
//  jamcoin
//
//  Created by 綦纪 on 4/10/16.
//  Copyright © 2016 Zeno. All rights reserved.
//

#include <iostream>
#include <string>
using namespace std;
int out[9] = {3, 2, 5, 2, 7, 2, 3, 2, 11};
string str = "10000000000000000000000000000001";
string change(){
    int length = str.length();
    char temp[length];
    for (int i = 0; i < str.length(); i ++) {
        strcpy(temp, str.c_str());;
    }
    
    if (temp[length-1] == '0') {
        temp[length-1] = '1';
    }
    else{
        for (int j = length-1; j >= 0; j --) {
            if (temp[j] == '1') {
                temp[j] = '0';
            }
            else{
                temp[j] = '1';
                break;
            }
        }
    }
    if (temp[length-1] == '0') {
        temp[length-1] = '1';
    }
    else{
        for (int j = length-1; j >= 0; j --) {
            if (temp[j] == '1') {
                temp[j] = '0';
            }
            else{
                temp[j] = '1';
                break;
            }
        }
    }
    str.assign(temp);
    return str;
}
bool test(string str){
    int length = str.length();
    char temp[length];
    int flag = 0;
    for (int i = 0; i < str.length(); i ++) {
        strcpy(temp, str.c_str());;
    }
    for (int i = 0; i < 32; i ++) {
        if (temp[i] == '1' && i%2 == 0)
            flag ++;
        else if(temp[i] == '1'&& i%2 == 1)
            flag --;
    }
    if (flag == 0) {
        return true;
    }
    else
        return false;
}
void output(string str){
    cout << str << " ";
    for (int i = 0; i < 8; i ++) {
        cout << out[i] << " ";
    }
    cout << out[8] << endl;
}
int main(int argc, const char * argv[]) {
    int l,m,n;
    cin >> l >> m >> n;
    cout << "Case #1:" << endl;
    for (int  i = 0; i < 500; ) {
        if (test(str) == true) {
            output(str);
            i ++;
            change();
            }
        else
            change();
    }
    return 0;
}
