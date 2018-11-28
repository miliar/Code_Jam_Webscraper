//
//  A.cpp
//  
//
//  Created by Jerry Peng on 4/10/16.
//
//

#include <bits/stdc++.h>
using namespace std;

int main (){
    freopen ("output.txt", "w", stdout);
    int T; cin >> T;
    string temp = "";
    string output = "";
    string temp2 = "";
    for (int zz = 1; zz <= T; zz++){
        temp = "";
        output = "";
        cout << "Case #" << zz << ": ";
        cin >> temp;
        output += temp[0];
        for (int i = 1; i < temp.length(); i++){
            temp2 = temp[i];
        if ( ((int)temp[i]) > ((int)output[0]) || ((int)temp[i]) == ((int)output[0])){
            output.insert(0, temp2);
        } else {
            output += temp2;
        }
    }
    cout << output << endl;
}
}
