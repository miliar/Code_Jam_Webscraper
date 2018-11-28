//
//  gentest.cpp
//  AimRed
//
//  Created by Vivek Dhiman on 4/9/16.
//  Copyright (c) 2016 Vivek Dhiman. All rights reserved.
//
#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <unordered_map>
#include <algorithm>
#include <stdio.h>      /* printf, scanf, puts, NULL */
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */
using namespace std;


int main(){
    int t ;
    cin >> t;
    for(int _t=1; _t<=t; _t++){
        cout << "Case #" << _t << ": ";
        long long K, C, S;
        cin >> K >> C >> S;
        for(int i=1; i<=K; i++){
            cout << i << " ";
        }
        cout << endl;
    }
    return 0;
}

