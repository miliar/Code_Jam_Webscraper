//
//  main.cpp
//  Revenge of the Pancakes
//
//  Created by Nabil SHF on 4/9/16.
//  Copyright © 2016 Nabil SHF. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <cstring>
#include <sstream>
#include <string>
using namespace std;

typedef long long int ll;

int main(){
    int t;
    string s;
    scanf ("%d",&t);
    for (int l = 1;l<=t;++l){
        cin>>s;
        int n = (int)s.size();
        int i = 0;
        for (;i<n;++i){
            if (s[i]!='+') break;
        }
        
        ll cnt = 0;
        while (i<n){
            if (s[i]=='+'){
                cnt++;
                int j = i+1;
                for (;j<n;++j){
                    if (s[j]!='+') break;
                }
                i = j;
            }
            i++;
        }
        if (s[n-1]=='+') cnt--;
        ll sol = cnt*2;
        sol++;
        if (s[0]=='+') sol++;
        printf ("Case #%d: ",l);
        cout<<sol<<endl;
    }
    
    
    
    return 0;
}