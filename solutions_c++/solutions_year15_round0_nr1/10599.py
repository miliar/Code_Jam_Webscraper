//
//  main.cpp
//  GCJ
//
//  Created by JinYu on 4/11/15.
//  Copyright (c) 2015 mainLogic. All rights reserved.
//

#include <iostream>
#include <string>
using namespace std;
int main(int argc, const char * argv[]) {
    
    
    int T;
    cin>>T;
    int k = 0;
    while (k<T) {
        int n;
        cin>>n;
        string s;
        cin>>s;
        int clap_number = 0;
        int should_invite = 0;
        for (int i=0; i<=n; i++) {
            
            if (clap_number<i&&(s[i] - '0')!=0) {
                should_invite +=(i - clap_number);
                clap_number+= should_invite;
            }
            clap_number += s[i] - '0';
            
        }
        cout<<"Case #"<<k+1<<":"<<" "<<should_invite<<endl;
        k++;
    }
    
    return 0;
}
