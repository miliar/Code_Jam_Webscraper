/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: Alex
 *
 * Created on 2016年4月16日, 上午 9:09
 */

#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <string>

using namespace std;

/*
 * 
 */

void Solve() {
    int total;
    scanf("%d", &total);
    
    for(int i = 0; i < total; i++) {
        char buf[1024];
        scanf("%s", buf);
//        sort(buf, buf+strlen(buf));
        
        string ans = "";
        
        int len = strlen(buf);
        char largest = 'A';
        for(int j = 0; j <  len; j ++) {
            if(buf[j] >= largest) {
                largest = buf[j];
                ans = buf[j] + ans;
            }
            else {
                ans = ans + buf[j] ;
            }
            
        }
        
        printf("Case #%d: %s", i+1, ans.c_str());
        
        printf("\n");
    }

    return;
}

int main(int argc, char** argv) {
    Solve();
    
    return 0;
}

