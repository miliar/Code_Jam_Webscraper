//
//  main.cpp
//  pA
//
//  Created by Victor Huang on 2016/4/10.
//  Copyright © 2016年 Victor Huang. All rights reserved.
//

#include <iostream>
using namespace std;

int main() {
    int T, N;
    cin >> T;
    for(int tc=1; tc<=T; tc++){
        cin >> N;
        bool cnt[10] = {0}, allFound = 0;
        long long int lastNumber = N;
        
        for(int k=1; k<=100000; k++){
            long long int kN = k*N;
            long long int kN0 = kN;
            while(kN){
                cnt[kN%10] |= 1;
                kN /= 10;
            }
            allFound = 1;
            for(int i=0; i<=9; i++)
                allFound &= cnt[i];
            
            if(allFound){
                lastNumber = kN0;
                break;
            }
        }
        
        if(allFound)
            cout << "Case #" << tc << ": " << lastNumber << endl;
        else
            cout << "Case #" << tc << ": " << "INSOMNIA" << endl;
    }
    
    return 0;
}
