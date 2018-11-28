//
//  main.cpp
//  Code Jam
//
//  Created by Haitham Khedr on 4/11/15.
//  Copyright (c) 2015 Haitham Khedr. All rights reserved.
//

#include <iostream>
#include<string>
#include<cstdio>
#include<vector>
using namespace std;

int main() {
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int n=0;
    cin>>n;
    int k=1;
    int maxAud;
    
    while(k<=n){
        int standing=0;
        int needed=0;

    cout<<"Case #"<<k<<": ";
    string input;
    vector<int> shyness;
    cin>>maxAud>>input;        
    for(int i=0;i<input.size();i++)
        shyness.push_back(input[i]-'0');
        
    if(shyness.size()==1){
        needed=0;
        cout<<needed<<endl;
        k++;
    }
    else{
        for (int i=0; i<shyness.size(); i++) {
            if (standing<=i && shyness[i]!=0) {
                needed+=(i-standing);
                standing+=(i-standing)+shyness[i];
               
            }
            else
                standing+=shyness[i];
        }
        
        cout<<needed<<endl;
         k=k+1;
    }
       
    }
    
    
    
}
