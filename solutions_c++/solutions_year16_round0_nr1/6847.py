//
//  sleepcount.cpp
//  nn
//
//  Created by Haoru Zhao on 4/8/16.
//  Copyright © 2016 Haoru Zhao. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;


long countSheep(int num){
    if(num == 0){
        return -1;
    }
    
    int bitmask = 0;
    int i = 1;
    long temp = num;
    
    while( bitmask != 0x03FF){
        
        temp = (i++) * num;
        
        while(temp){
            bitmask |= 1 << (temp % 10);
            temp = temp/10;
        }
        
    }
    return  (--i) * num;
}

int main(){
    
    int n, argv;
    cin >> n;
    for(int i = 1; i <= n; ++i){
        cin >> argv;
        long ret = countSheep(argv);
        if(ret == -1){
            cout << "Case #" << i <<": INSOMNIA" <<endl;
        }else{
            cout << "Case #" << i <<": " << ret << endl;
        }
    }
}
