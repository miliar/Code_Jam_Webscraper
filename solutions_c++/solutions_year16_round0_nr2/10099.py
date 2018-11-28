//
//  main.cpp
//  pB
//
//  Created by Victor Huang on 2016/4/10.
//  Copyright © 2016年 Victor Huang. All rights reserved.
//

#include <iostream>
using namespace std;

int main() {
    int T;
    string s;
    cin >> T;
    for(int tc=1; tc<=T; tc++){
        int flips = 0;
        cin >> s;
        
        while(1){
            int last;
            
            last = -1;
            if(s[0]=='-'){
                for(int i=0; i<s.size(); i++){
                    if(s[i]=='+'){
                        last = i;
                        break;
                    }
                }
                if(last==-1){
                    flips += 1;
                    break;
                }
                
                for(int i=0; i<last; i++){
                    s[i] = '+';
                }
                flips += 1;
            }
            
            last = -1;
            for(int i=0; i<s.size(); i++){
                if(s[i]=='-'){
                    last = i;
                    break;
                }
            }
            if(last==-1){
                break;
            }
            for(int i=0; i<last; i++){
                s[i] = '-';
            }
            flips += 1;
        }
        
        cout << "Case #" << tc << ": " << flips << endl;
    }
    
    return 0;
}
