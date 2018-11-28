//
//  main.cpp
//  leetcode_cpp
//
//  Created by Xingying Liu on 4/5/16.
//  Copyright © 2016 Xingying Liu. All rights reserved.
//

# include <iostream>
# include <vector>
# include <unordered_map>
# include <set>
# include <unordered_set>
# include <fstream>

using namespace std;


long long int sleep(int num) {
    unordered_set<int> remain({1,2,3,4,5,6,7,8,9,0});
    long long int cur = 0, tmp;
    int unit;
    while ( !remain.empty() ) {
        cur += num;
        tmp = cur;
        while (tmp) {
            unit = tmp%(int)10;
            if (remain.count(unit))
                remain.erase(unit);
            tmp/=10;
        }
    }
    return cur;
}

int main(){
    int T, num, id = 1;
    cin>>T;
    while (T--) {
        cout<<"Case #"<<id<<": ";
        id++;
        cin>>num;
        if (num==0)
            cout<<"INSOMNIA"<<endl;
        else
            cout<<sleep(num)<<endl;
    }
    
    return 0;
}