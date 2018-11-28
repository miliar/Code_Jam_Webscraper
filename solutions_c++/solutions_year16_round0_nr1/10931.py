//
//  main.cpp
//  GCJ2016
//
//  Created by Varun Varadarajan on 4/9/16.
//  Copyright © 2016 Varun Varadarajan. All rights reserved.
//

#include <iostream>

using namespace std;

int SEEN_COUNT = 0;
bool SEEN[11] = {false};

void checkDigits(long long N) {
    long long temp = N;
    while(temp != 0) {
        int digit = temp%10;
        if(SEEN[digit+1] == 0) {
            SEEN[digit+1] = 1;
            SEEN_COUNT += 1;
        }
        temp = temp/10;
    }
}

void init() {
    SEEN_COUNT = 0;
    for(int i=0; i<11; i++) SEEN[i] = false;
}

long long getAnswer(long long N) {
    init();
    checkDigits(N);
    if(SEEN_COUNT == 9) return N;
    for(long x=2;;x++) {
        checkDigits(N*x);
        if(SEEN_COUNT >= 10) return N*x;
    }
}

int main(int argc, const char * argv[]) {
    // insert code here...
    int T;
    cin>>T;
    int i = 1;
    while (T--) {
        long long N;
        cin>>N;
        if(N==0) cout<<"Case #"<<i++<<": INSOMNIA"<<endl;
        else cout<<"Case #"<<i++<<": "<<getAnswer(N)<<endl;
    }
    
    return 0;
}
