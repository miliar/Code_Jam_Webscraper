//
//  main.cpp
//  DumbTest
//
//  Created by Churu Tang on 9/25/14.
//  Copyright (c) 2014 Churu Tang. All rights reserved.
//

#include <iostream>
#include <utility>
#include <stdio.h>
#include <string>
#include <vector>
#include <stack>
#include <algorithm>

#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <cstdlib>

using namespace std;

    int main() {
        int lines;
        cin >> lines;
        cout << lines << endl;
        for (int i = 0; i < lines; ++ i) {
            int arrayLen;

            cin >> arrayLen;
            vector<int> array(arrayLen + 1, 0);
            
            for (int j = 0; j <= arrayLen; ++ j) {
                char tmp;
                cin >> tmp;
                array[j] = atoi(&tmp);
  
            }
            int friendNum = 0;
            int audiences = 0;
            for (int j = 0; j <= array.size(); ++ j) {
                if (j > (audiences + friendNum)) {
                    friendNum += (j - (audiences+ friendNum));
                }
                audiences += array[j];
            }
            cout << "Case #" << i+1 << ": " << friendNum << endl;
        }
        return 0;
    }
