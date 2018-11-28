//
//  main1.cpp
//  CodeJam
//
//  Created by Victor Young on 4/16/16.
//  Copyright © 2016 Victor Young. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <string>
#include <deque>
using namespace std;
int main(){
    
    if(freopen("/Users/Victor/Desktop/output.txt", "w", stdout) == NULL)
        fprintf(stderr,"error redirecting stdout\n");
    if(freopen("/Users/Victor/Desktop/A-large.in", "r", stdin) == NULL)
        fprintf(stderr,"error redirecting stdin\n");

    int n;
    cin >> n;
    string temp;
    getline(std::cin,temp);
    for (int i=0; i<n; i++) {
        deque<char> que;
        getline(std::cin,temp);
        for (int j=0; j<temp.length(); j++) {
            char tempchar = temp[j];
            if (que.empty()) {
                que.push_back(tempchar);
            }
            else if (que.front()>tempchar) {
                que.push_back(tempchar);
            }
            else{
                que.push_front(tempchar);
            }
        }
        cout << "Case #"<<i+1<<": ";
        while (!que.empty()) {
            cout << que.front();
            que.pop_front();
        }
        if (i!=n-1) {
            cout << endl;
        }
        
    }
}