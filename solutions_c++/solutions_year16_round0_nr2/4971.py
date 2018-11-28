//
//  b.cpp
//  
//
//  Created by liumingming on 4/10/16.
//
//

#include <stdio.h>
#include <iostream>
#include <string>
#include <cstring>
#include <string.h>
#include <algorithm>
#include <set>
#include <map>
#include <cstdlib>

using namespace std;

int main(){
//    freopen("1.txt", "r", stdin);
    int t;
    scanf("%d", &t);
    for(int i = 0; i < t; ++i){
        char str[300];
        memset(str, 0, sizeof(str));
        scanf("%s", str);
        char compressedstr[300];
        memset(compressedstr,0, sizeof(compressedstr));
        int len = strlen(str);
        //cout << len << endl;
        int j = 0, k = 0;
        int zerocounter = 0;
        while (j < len){
            char mark = str[j];
            while(j < len && j + 1 < len && str[j + 1] == str[j]){
                ++j;
            }
            ++j;
            compressedstr[k++] = mark;
            zerocounter += mark == '-'? 1: 0;
        }
        int clen = strlen(compressedstr);
        if(compressedstr[0] == '-'){
            printf("Case #%d: %d\n", i + 1,(zerocounter << 1) - 1);
        }
        else{
            //cout << (zerocounter << 1) << endl;
	    printf("Case #%d: %d\n", i + 1, (zerocounter << 1));
        }
    }
    return 0;
}
