//
//  ProblemB.cpp
//  codejam2015
//
//  Created by sambaiz on 2015/04/11.
//  Copyright (c) 2015年 sambaiz. All rights reserved.
//

#include <iostream>
using namespace std;

string reduce(string str){
    string now = "1"; //std::string
    bool plus = true;
    if(str[0] == '-'){
        plus = false;
        str = str.substr(1);
    }
    for(int i = 0; i < str.size(); i++){
        if(now == "1"){
            now = str[i];
        }else if(now == "i"){
            if(str[i] == 'i'){ // charの比較だから''
                now = "1";
                plus = !plus;
            }else if(str[i] == 'j'){
                now = "k";
            }else if(str[i] == 'k'){
                now = "j";
                plus = !plus;
            }
        }else if(now == "j"){
            if(str[i] == 'i'){
                now = "k";
                plus = !plus;
            }else if(str[i] == 'j'){
                now = "1";
                plus = !plus;
            }else if(str[i] == 'k'){
                now = "i";
            }
        }else if(now == "k"){
            if(str[i] == 'i'){
                now = "j";
            }else if(str[i] == 'j'){
                now = "i";
                plus = !plus;
            }else if(str[i] == 'k'){
                now = "1";
                plus = !plus;
            }
        }
    }

    if(plus){
        return now;
    }else{
        return "-" + now;
    }
}

string* reduce_reverse_history(string str){
    string* ret = (string *)malloc(sizeof(string) * 10001);
    string now = "1"; //std::string
    bool plus = true;
    if(str[0] == '-'){
        plus = false;
        str = str.substr(1);
    }
    for(int i = str.size() - 1; i >= 0; i--){
        if(plus){
            ret[i + 1] = now;
        }else{
            ret[i + 1] = "-" + now;
        }
        if(now == "1"){
            now = str[i];
        }else if(str[i] == 'i'){
            if(now == "i"){
                now = "1";
                plus = !plus;
            }else if(now == "j"){
                now = "k";
            }else if(now == "k"){
                now = "j";
                plus = !plus;
            }
        }else if(str[i] == 'j'){
            if(now == "i"){
                now = "k";
                plus = !plus;
            }else if(now == "j"){
                now = "1";
                plus = !plus;
            }else if(now == "k"){
                now = "i";
            }
        }else if(str[i] == 'k'){
            if(now == "i"){
                now = "j";
            }else if(now == "j"){
                now = "i";
                plus = !plus;
            }else if(now == "k"){
                now = "1";
                plus = !plus;
            }
        }
    }
    
    if(plus){
        ret[0] = now;
    }else{
        ret[0] = "-" + now;
    }
    return ret;
}

int main() {
    // case数
    int c_n = 0;
    // l文字数, をx回繰り返す
    int l, x;
    string str;
    bool condition;
    
    // 標準入力より入力
    scanf("%d", &c_n);
    for(int n = 0; n < c_n; n++){
        condition = false;
        scanf("%d %d", &l, &x);
        cin >> str;
        string base = str;
        for(int i = 1; i < x; i++){
            str += base;
        }
        if(str.size() >= 3){ //3つに分けようがないなら論外
            // i番目とj番目で分割する
            string memo;
            string* memo2;
            for(int j = 2; j < str.size(); j++){
                if(reduce(str.substr(j)) != "k") continue;
                memo = "";
                memo2 = reduce_reverse_history(str.substr(1,j-1));
                for(int i = 1; i < j; i++){
                    memo = reduce(memo + str[i-1]);
                    if(memo == "i" && memo2[i-1] == "j"){
                        condition = true;
                        break;
                    }
                }
                free(memo2);
                if(condition) break;
            }
        }
        
        // 標準出力へ出力
        if(condition){
            printf("Case #%d: YES\n", n + 1);
        }else{
            printf("Case #%d: NO\n", n + 1);
        }
    }
}