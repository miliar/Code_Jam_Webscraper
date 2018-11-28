//
//  main.cpp
//  CodeJam1
//
//  Created by Aayush Goel on 4/8/16.
//  Copyright © 2016 Aayush Goel. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;

int countTo(int N){
    int seen[10];
    
    for(int j=0; j<10; j++){
        seen[j] = 0;
    }
    
    int cur = 0;
    int test, flag;
    for(int i=1; i<2000; i++ ){
        cur +=N;
        //cout << "T "<<cur<< ": ";
        test=cur;
        while(test>0){
            int digit = test%10;
            seen[digit]=1;
            test/=10;
        }
        flag = 1;
        for(int j=0; j<10; j++){
            flag = flag&seen[j];
            //cout <<seen[j];
        }
        //cout<<endl;
        if(flag){
            return (cur);
        }
    }
    return -1;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    int t,x;
    vector<int> N;
    
    cin >> t;
    for(int i=0; i<t; i++){
        cin >> x;
        N.push_back(x);
    }
    
    string str;
    for(int i=1; i<=N.size(); i++){
        int out = countTo(N[i-1]);
        if(out==-1) str = "INSOMNIA";
        else str = to_string(out);
        cout<< "Case #" << i <<": " <<str<< endl;
    }
    
    return 0;
}
