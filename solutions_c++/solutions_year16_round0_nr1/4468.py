//
//  main.cpp
//  Counting Sheep
//
//  Created by Qiu Xin on 9/4/16.
//  Copyright © 2016 Qiu Xin. All rights reserved.
//

#include <iostream>
#include <unordered_set>
using namespace std;




int main(int argc, const char * argv[]) {
    // insert code here...
    int runNum;
    cin >> runNum;
    unordered_set<int> store;
    for (int i=1;i<=runNum;i++)
    {
        int num=0, cur, digit, base;
        store.clear();
        cin >> base;
        if (base==0)
        {
            cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
            continue;
        }
        while (store.size()!=10)
        {
            num+=base;
            cur=num;
            while (cur!=0)
            {
                digit=cur%10;
                store.insert(digit);
                cur/=10;
            }
        }
        cout<<"Case #"<<i<<": "<<num<<endl;
    }
    return 0;
}
