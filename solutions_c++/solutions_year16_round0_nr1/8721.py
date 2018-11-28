//
//  Crit A.cpp
//  
//
//  Created by Jerry Peng on 4/8/16.
//
//

#include <fstream>
#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
//Checks if number in in a certain array
bool inArray(int tocheck, vector<int> numbers){
    if(find(numbers.begin(), numbers.end(), tocheck) != numbers.end()) {
        return true;
    }
    return false;
}
//win condition
bool check(vector<int> digits){
    for ( int chk = 0; chk < 10; chk++ ){
        if (!inArray(chk, digits)){
            return false;
        }
    }
    return true;
}

int main() {
    freopen("output.txt","w",stdout);
    int T; cin >> T;
    for (int zz = 1; zz <= T; zz++){
        cout << "Case #" << zz << ": ";
        int i = 1;
        int N; cin >> N;
        vector<int> seen;
        seen.clear();
        int number;
        if (N == 0){
            cout << "INSOMNIA\n";
        } else {
            while (!check(seen)){
                number = N * i;
                string test = to_string(number);
                for ( char num : test ){
                    if (!inArray(num, seen)){
                        seen.push_back(num - '0');
                    }
                }
                i++;
            }
            cout << to_string(number) << "\n";
        }
    }
}