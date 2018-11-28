//
//  main.cpp
//  leetcode_cpp
//
//  Created by Xingying Liu on 4/5/16.
//  Copyright © 2016 Xingying Liu. All rights reserved.
//

# include <iostream>
# include <vector>

using namespace std;


int cake(string input) {
    int count = 0;
    for (int i=1; i<input.size(); i++)
        if (input[i]!=input[i-1])
            count++;
    if (input.back()=='-')
        count++;
    return count;
}

int main(){
    int T, id = 1;
    cin>>T;
    string input;
    while (T--) {
        cout<<"Case #"<<id<<": ";
        id++;
        cin>>input;
        cout<<cake(input)<<endl;
    }
    //cout<<"hello world"<<endl;
    return 0;
}