//

//  main.cpp

//  test

//

//  Created by Hui Xu on 3/22/16.

//  Copyright © 2016 Hui Xu. All rights reserved.

//




#include <iostream>

#include <vector>

using namespace std;

typedef unsigned long long int LLI;

#define _Test_

int main(int argc, const char * argv[]) {
#ifdef _Test_
    freopen("/Users/huixu/Desktop/APACTEST/test/test/A-large1.in", "r", stdin);
    freopen("/Users/huixu/Desktop/APACTEST/test/test/A-large1.out", "w", stdout);
#endif
    
    int T;
    cin>>T;
    string S;
    for (int t=0; t<T; t++) {
        cin>>S;
        //char schar = S[0];
        int scharInd = 0;
        for (int i=1; i<S.length(); i++) {
            if (S[i]>=S[scharInd]) {
                char temp = S[i];
                //scharInd以后到整体往后移动，再把S[i]放到scharInd
                for (int j=i-1; j>=scharInd; j--) {
                    S[j+1]=S[j];
                }
                S[scharInd] = temp;
            }
        }
        cout<<"Case #"<<t+1<<": "<<S<<endl;
    }
    return 0;
}

