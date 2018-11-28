//
//  main1.cpp
//  CodeJam
//
//  Created by Victor Young on 4/30/16.
//  Copyright © 2016 Victor Young. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <string>
#include <deque>
using namespace std;
int bucket[30];
int result[11];

string num[11]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

//bool flag = true;
bool finalend = false;

int getIndex(char a){
    return a-'A';
}

void dfs(int start){
    for (int i = start; i<10; i++) {
        bool flag = true;
        int current[30];
        memset(current, 0, 30*sizeof(int));
        for (int j = 0; j<num[i].length(); j++) {
            current[getIndex(num[i][j])]++;
        }
        for (int j = 0; j<num[i].length(); j++) {
            if (bucket[getIndex(num[i][j])]<current[getIndex(num[i][j])]){
                flag = false;
                break;
            }
            
        }
        if (flag) {
            result[i]++;
            for (int j = 0; j<num[i].length(); j++) {
                bucket[getIndex(num[i][j])]--;
            }
            dfs(i);
            if (finalend) {
                return;
            }
            result[i]--;
            for (int j = 0; j<num[i].length(); j++) {
                result[i]--;
                bucket[getIndex(num[i][j])]++;

            }
        }
    }
    bool flag2 = true;
    for (int i=0; i<26; i++) {
        if (bucket[i]) {
            flag2 = false;
        }
    }
    if (flag2) {
        finalend = true;
    }
    
}

int main(){

    if(freopen("/Users/Victor/Desktop/output.txt", "w", stdout) == NULL)
        fprintf(stderr,"error redirecting stdout\n");
    if(freopen("/Users/Victor/Desktop/A-large.in", "r", stdin) == NULL)
        fprintf(stderr,"error redirecting stdin\n");

    int n;
    cin >> n;
//    cout << "test" << n << endl;
    for (int i =0 ; i<n; i++) {
        string temp;
        cin >> temp;
        memset(bucket, 0, 30*sizeof(int));
        memset(result, 0, 11*sizeof(int));
        finalend = false;
        for (int j = 0; j<temp.length(); j++) {
            int index = getIndex(temp[j]);
            bucket[index]++;
        }
        while(bucket[getIndex('Z')]) {
            for (int j = 0; j<num[0].size(); j++) {
                bucket[getIndex(num[0][j])]--;
            }
            result[0]++;
        }
        while(bucket[getIndex('W')]) {
            for (int j = 0; j<num[2].size(); j++) {
                bucket[getIndex(num[2][j])]--;
            }
            result[2]++;
        }
        while(bucket[getIndex('U')]) {
            for (int j = 0; j<num[4].size(); j++) {
                bucket[getIndex(num[4][j])]--;
            }
            result[4]++;
        }
        while(bucket[getIndex('X')]) {
            for (int j = 0; j<num[6].size(); j++) {
                bucket[getIndex(num[6][j])]--;
            }
            result[6]++;
        }
        dfs(0);
        cout << "Case #"<<i+1<<": ";
        for (int j = 0; j<10; j++) {
            while (result[j]--) {
                cout<<j;
            }
        }
        if (i!=n-1) {
            cout << endl;
        }
    }
    
    return 0;
}