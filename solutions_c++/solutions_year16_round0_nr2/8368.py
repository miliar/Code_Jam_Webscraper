//
//  pancakes.cpp
//  
//
//  Created by Will Sawyer on 4/9/16.
//
//

#include <stdio.h>
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <map>
#include <climits>
#include <algorithm>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

int main() {
    int t, n, ret;
    string pancakes = "";
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        int flips = 0;
        bool plusYet = false;
        cin >> pancakes;
        
        for(int j=0; j<pancakes.length(); j++){
            if(pancakes[j] == '+'){
                if(!plusYet && j > 0 && pancakes[j-1] == '-')
                    flips++;
                if(j<pancakes.length()-1 && pancakes[j+1] == '-')
                    flips+=2;
                plusYet = true;
            }
        }
        if(!plusYet)
            flips = 1;
        
        cout << "Case #" << i << ": " << flips << endl;
    }
    return 0;
}


       
                 
                 
                 
                 
                 
