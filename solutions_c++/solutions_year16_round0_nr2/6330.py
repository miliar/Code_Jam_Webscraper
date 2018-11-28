//
//  test.cpp
//
//
//  Created by Jonathan Beltran on 4/8/16.
//
//

#include <stdlib.h>
#include <iostream>
#include <stdio.h>
#include <string>
#include <map>
#include <fstream>
#include <functional>
#include <climits>
#include <vector>
#include <queue>
#include <list>
#include <algorithm>
#include <bitset>         // std::bitset


using namespace std;



int main(){

    int t;
    cin >> t;

    for(int i = 0; i < t; i++){
      string x;
      cin >> x;

      vector<char> vi;

      for(int j = 0; j < x.length(); j++){

        vi.push_back(x[j]);

        if(j > 0 && vi.back() == x[j - 1]){
          vi.pop_back();
        }
      }
        if(vi.back() == '+'){
          vi.pop_back();
        }
        cout << "Case #" << i+1 << ": " << vi.size() << endl;
    }



}
