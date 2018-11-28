//
//  main.cpp
//  c
//
//  Created by ram on 09/04/16.
//  Copyright © 2016 mac. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <vector>
#include <array>
#include <string>
#include <math.h>
#include <algorithm>

using namespace std;

static unsigned long long int arr[9] = {0,0,0,0,0,0,0,0,0};
static bool found;

bool isPrime (unsigned long long int num)
{
    if (num <=1)
        return false;
    else if (num == 2)
        return true;
    else if (num % 2 == 0)
        return false;
    else
    {
        bool prime = true;
        unsigned long long int divisor = 3;
        double num_d = static_cast<double>(num);
        unsigned long long int upperLimit = static_cast<unsigned long long int>(sqrt(num_d) +1);
        
        while (divisor <= upperLimit)
        {
            if (num % divisor == 0)
                prime = false;
            divisor +=2;
        }
        return prime;
    }
}

bool check(string s){
    found = true;
    //int load = 0;
    for (int u = 2; u<=10; u++) {
        unsigned long long int aa = 0;
        for (int i = 0; i<16; i++) {
            if (s[i] == '1') {
                aa = aa + pow(u,15 - i);
            }
    
        }
        arr[u-2] = aa;
        
    }
    for (int all = 0; all<9; all++) {
        if (isPrime(arr[all])) {
            found = false;
        }
    }
    if (found) {
        for (int game = 0; game<9; game++) {
            for (int count = 2; count<arr[game]; count++) {
                if (arr[game]%count == 0) {
                    arr[game] = count;
                }
            }
        }
    }
    return found;
}

/*void solve(string s){
    
    for (int u = 2; u<=10; u++) {
        unsigned long long int aa = 0;
        for (int i = 0; i<16; i++) {
            if (s[i] == '1') {
                aa = aa + pow(u,15 - i);
            }
        }
        arr[u-2] = aa;
    }
    
}*/

int main(){
    freopen("output.txt", "w", stdout);
    cout<<"Case #1:"<<endl;
    vector<string> vec;
    vec.reserve(100);
    int z = 50;
    //int ans = 1;
    string s = "1000000000000001";
    for (int a = 0; a<=1; a++) {
        if (a == 0) {
            s[1] = '0';
        }
        else{
            s[1] = '1';
        }
        for (int b = 0; b<=1; b++) {
            if (b == 0) {
                s[2] = '0';
            }
            else{
                s[2] = '1';
            }
            for (int c = 0; c<=1; c++) {
                if (c == 0) {
                    s[3] = '0';
                }
                else{
                    s[4] = '1';
                }
                for (int d = 0; d<=1; d++) {
                    if (d == 0) {
                        s[4] = '0';
                    }
                    else{
                        s[4] = '1';
                    }
                    for (int e = 0; e<=1; e++) {
                        if (e == 0) {
                            s[5] = '0';
                        }
                        else{
                            s[5] = '1';
                        }
                        for (int f = 0; f<=1; f++) {
                            if (f == 0) {
                                s[6] = '0';
                            }
                            else{
                                s[6] = '1';
                            }
                            for (int g = 0; g<=1; g++) {
                                if (g == 0) {
                                    s[7] = '0';
                                }
                                else{
                                    s[7] = '1';
                                }
                                for (int h = 0; h<=1; h++) {
                                    if (h == 0) {
                                        s[8] = '0';
                                    }
                                    else{
                                        s[8] = '1';
                                    }
                                    for (int i = 0; i<=1; i++) {
                                        if (i == 0) {
                                            s[9] = '0';
                                        }
                                        else{
                                            s[9] = '1';
                                        }
                                        for (int j = 0; j<=1; j++) {
                                            if (j == 0) {
                                                s[10] = '0';
                                            }
                                            else{
                                                s[10] = '1';
                                            }
                                            for (int k = 0; k<=1; k++) {
                                                if (k == 0) {
                                                    s[11] = '0';
                                                }
                                                else{
                                                    s[11] = '1';
                                                }
                                                for (int l = 0; l<=1; l++) {
                                                    if (l == 0) {
                                                        s[12] = '0';
                                                    }
                                                    else{
                                                        s[12] = '1';
                                                    }
                                                    for (int m = 0; m<=1; m++) {
                                                        if (m == 0) {
                                                            s[13] = '0';
                                                        }
                                                        else{
                                                            s[13] = '1';
                                                        }
                                                        for (int n = 0; n<=1; n++) {
                                                            if (n == 0) {
                                                                s[14] = '0';
                                                            }
                                                            else{
                                                                s[14] = '1';
                                                            }
                                                            
                                                           if (z>0 && check(s)) {
                                                                cout<<s;
                                                               
                                                                for (int kr = 0; kr<9; kr++) {
                                                                    cout<<" "<<arr[kr];
                                                                }
                                                                cout<<endl;
                                                               
                                                                z--;
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    return 0;
}