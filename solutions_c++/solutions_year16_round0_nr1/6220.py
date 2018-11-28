//
//  main.cpp
//  a
//
//  Created by ram on 09/04/16.
//  Copyright © 2016 mac. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <vector>
#include <array>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

int main(){
    freopen("A-large.in.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t,n,temp;
    cin>>t;
    vector<int> vec;
    for (int i = 1; i<=t ; i++) {
        cout<<"Case #"<<i<<": ";
        cin>>n;
        for (int ar = 0; ar<10; ar++) {
            vec.push_back(ar);
        }
        if (n == 0) {
            cout<<"INSOMNIA"<<endl;
        }
        else{
            int a = 1;
            while (vec.size() != 0) {
                temp = n*a;
                int temp1 = temp;
                do {
                    int digit = temp1 % 10;
                    //cout<<digit<<endl;
                    if (find(vec.begin(),vec.end(),digit) != vec.end()) {
                        size_t k = distance(vec.begin(), find(vec.begin(),vec.end(),digit));
                        vec.erase(vec.begin() + k);
                    }
                    temp1= temp1/10;
                } while (temp1 > 0);
                a++;
            }
            cout<<temp<<endl;
        }
        vec.clear();
    }
    return 0;
}
