//
//  main.cpp
//  1
//
//  Created by Wanjia He on 4/30/16.
//  Copyright © 2016 Wanjia He. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(int argc, const char * argv[]) {
    ifstream fin("1.in");   ofstream fout("1.out");
    int t, i, now, j, l;
    string s, ans;
    int num[30], ans_num[30];
    fin >> t;
    for (l=1; l<=t; l++){
        fin >> s;
        for (i=0; i<30; i++){
            num[i] = 0;
            ans_num[i] = 0;
        }
        for (i=0; i<s.length(); i++)
            num[s[i] - int('A') + 1]++;
        ans = "";
        if (num[26] > 0){
            ans_num[0] += num[26];
            num[3] -= num[26];
            num[18] -= num[26];
            num[15] -= num[26];
            num[26] = 0;
        }
        if (num[23] > 0){
            ans_num[2] += num[23];
            num[20] -= num[23];
            num[15] -= num[23];
            num[23] = 0;
        }
        if (num[21] >0){
            ans_num[4] += num[21];
            num[6] -= num[21];
            num[15] -= num[21];
            num[18] -= num[21];
            num[21] = 0;
        }
        if (num[18] >0){
            ans_num[3] += num[18];
            num[20] -= num[18];
            num[8] -= num[18];
            num[5] -= 2 * num[18];
            num[18] = 0;
        }
        if (num[6] >0){
            ans_num[5] += num[6];
            num[9] -= num[6];
            num[22] -= num[6];
            num[5] -= num[6];
            num[6] = 0;
        }
        if (num[15] >0){
            ans_num[1] += num[15];
            num[14] -= num[15];
            num[5] -= num[15];
            num[15] = 0;
        }
        if (num[24] >0){
            ans_num[6] += num[24];
            num[9] -= num[24];
            num[19] -= num[24];
            num[24] = 0;
        }
        if (num[19] >0){
            ans_num[7] += num[19];
            num[22] -= num[19];
            num[14] -= num[19];
            num[5] -= 2 * num[19];
            num[19] = 0;
        }
        if (num[7] >0){
            ans_num[8] += num[7];
            num[9] -= num[7];
            num[8] -= num[7];
            num[5] -= num[7];
            num[20] -= num[7];
            num[7] = 0;
        }
        if (num[9] >0){
            ans_num[9] += num[9];
        }
        for (i=0; i<10; i++){
            for (j=0; j<ans_num[i]; j++)
                ans += char(i+int('0'));
        }
        fout << "Case #" << l << ": " << ans << endl;
    }
    return 0;
}
