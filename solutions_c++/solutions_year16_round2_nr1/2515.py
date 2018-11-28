//
//  main.cpp
//  GCJ
//
//  Created by 陶源 on 4/9/16.
//  Copyright © 2016 daisynowhere. All rights reserved.
//

#include <iostream>
#include <stdio.h>
#include <math.h>
#include <set>
#include <string>
using namespace std;
int main() {
    int T;
    //string digits[10]={"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};
    //z,e,r,o,n,t,w,h,f,u,i,v,s,x,g
    //z,w,x,g
    int sum[15];
    int len;
    int cnt[10];
    string S;
    freopen("/Users/daisy/Documents/GCJ/A-large.in","r",stdin);
    freopen("/Users/daisy/Documents/GCJ/GCJ/A-large.out","w",stdout);
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cin >> S;
        len = S.length();
        for (int j = 0; j < 15; ++j) {
            sum[j] = 0;
        }
        for (int j = 0; j < 10; ++j) {
            cnt[j] = 0;
        }
        for (int j = 0; j < len; ++j) {
            switch (S[j]) {
                case 'Z': //0
                    sum[0]++;break;
                case 'E': //0,1,3,5,7,9
                    sum[1]++;break;
                case 'R': //0,3,4
                    sum[2]++;break;
                case 'O': //0,1,2,4
                    sum[3]++;break;
                case 'N': //1,7,9
                    sum[4]++;break;
                case 'T': //2,3,8
                    sum[5]++;break;
                case 'W': //2
                    sum[6]++;break;
                case 'H': //3,8
                    sum[7]++;break;
                case 'F': //4,5
                    sum[8]++;break;
                case 'U': //4
                    sum[9]++;break;
                case 'I': //5,6,8,9
                    sum[10]++;break;
                case 'V': //5,7
                    sum[11]++;break;
                case 'S': //6,7
                    sum[12]++;break;
                case 'X': //6
                    sum[13]++;break;
                case 'G': //8
                    sum[14]++;break;
                default:
                    break; //0,2,4,6,8,1,3,5,7,9
            }
        }
        cnt[0] = sum[0];
        cnt[2] = sum[6];
        cnt[4] = sum[9];
        cnt[6] = sum[13];
        cnt[8] = sum[14];
        cnt[1] = sum[3]-sum[0]-sum[6]-sum[9];
        cnt[3] = sum[7]-sum[14];
        cnt[5] = sum[8]-sum[9];
        cnt[7] = sum[12]-sum[13];
        cnt[9] = sum[10]- cnt[5]-cnt[6]-cnt[8];
        cout << "Case #" << i <<": ";
        for (int j = 0; j<10; j++) {
            while (cnt[j]) {
                cnt[j]--;
                cout << j;
            }
        }
        cout << endl;
    }
    return 0;
}
