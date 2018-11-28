//
//  main.cpp
//  Hello
//
//  Created by PRAMOD KUMAR on 4/9/16.
//  Copyright © 2016 PRAMOD KUMAR. All rights reserved.
//

#include <iostream>
using namespace std;
int main() {
    std::string s;
    int t,count,u;
    cin>>t;
    u=t;
    while(t>0){
        cin>>s;
        count=0;
        for(int i=0;i<s.size()-1;i++)
        {
            if( (s[i] =='+' && s[i+1] =='-') || (s[i] == '-' && s[i+1]== '+'))
                count++;
            
        }
        if(s[s.length()-1] == '-')
            count++;
        cout<<"Case #"<<u-t+1<<": "<<count<<endl;
        
        t--;
    }
    return 0;
}
