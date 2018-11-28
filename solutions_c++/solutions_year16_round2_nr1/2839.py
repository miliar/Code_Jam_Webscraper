//
//  main.cpp
//  getting the digits
//
//  Created by HuMing on 4/30/16.
//  Copyright © 2016 HuMing. All rights reserved.
//

//
//  main.cpp
//  revengeofpancake
//
//  Created by HuMing on 4/9/16.
//  Copyright © 2016 HuMing. All rights reserved.
//

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include<iostream>
using namespace std;
typedef long long ll;

int main(){
    FILE *fin = freopen("A-large.in", "r", stdin);
    assert( fin!=NULL );
    FILE *fout = freopen("A-large-out.txt", "w", stdout);
    ll T;
    cin >> T;
    for(ll t = 1; t <= T; t++){

        string str;
        cin>>str;
        size_t zero = count(str.begin(), str.end(), 'Z');
        size_t two = count(str.begin(), str.end(), 'W');
        size_t four = count(str.begin(), str.end(), 'U');
        size_t six = count(str.begin(), str.end(), 'X');
        size_t eight = count(str.begin(),str.end(),'G');
        size_t one= count(str.begin(),str.end(),'O')-zero-two-four;
        size_t three= count(str.begin(),str.end(),'R')-zero-four;
        size_t five= count(str.begin(),str.end(),'F')-four;
        size_t seven= count(str.begin(),str.end(),'S')-six;
        size_t nine= count(str.begin(),str.end(),'I')-five-six-eight;
        cout << "Case #" << t << ": ";
        for (int i=0;i<zero;i++){
            cout<<'0';
        }
        for (int i=0;i<one;i++){
            cout<<'1';
        }
        for (int i=0;i<two;i++){
            cout<<'2';
        }
        for (int i=0;i<three;i++){
            cout<<'3';
        }
        for (int i=0;i<four;i++){
            cout<<'4';
        }
        for (int i=0;i<five;i++){
            cout<<'5';
        }
        for (int i=0;i<six;i++){
            cout<<'6';
        }
        for (int i=0;i<seven;i++){
            cout<<'7';
        }
        for (int i=0;i<eight;i++){
            cout<<'8';
        }
        for (int i=0;i<nine;i++){
            cout<<'9';
        }
        cout<<endl;
    }
}
