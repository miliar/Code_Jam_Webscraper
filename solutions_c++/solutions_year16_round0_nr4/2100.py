//
//  main.cpp
//  code-jam-4
//
//  Created by Ryan on 4/9/16.
//  Copyright © 2016 Ryan. All rights reserved.
//

#include <iostream>
using namespace std;
int main(int argc, const char * argv[]) {
    // insert code here...
    int T,K,C,S;
    cin >> T;
    for(int i=0; i<T; i++){
        cin >> K >> C >> S;
        printf("Case #%d:", i+1);
        for(int j=0; j<K; j++) cout << " " << j+1;
        cout << endl;
    }
    return 0;
}
