//
//  main.cpp
//  b.cpp
//
//  Created by Duo Donald Zhao on 4/12/14.
//  Copyright (c) 2014 Duo Donald Zhao. All rights reserved.
//

#include <iostream>
#include <iomanip>
#include <cmath>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;



int main(int argc, const char * argv[])
{
    int N;
    cin >> N;
    int a, b, c, d;
    for (int i = 1; i <= N; i++){
        vector<int> v(4);
        set<int> round1, round2;
        int round1_line, round2_line;
        cin >> round1_line;
        for (int j = 1; j <= 4; j++){
            cin >> a >> b >> c >> d;
            if (j == round1_line) {
                round1.insert(a);
                round1.insert(b);
                round1.insert(c);
                round1.insert(d);
            }
            
        }
        
        cin >> round2_line;
        for (int j = 1; j <= 4; j++){
            cin >> a >> b >> c >> d;
            if (j == round2_line) {
                round2.insert(a);
                round2.insert(b);
                round2.insert(c);
                round2.insert(d);
            }
            
        }
        vector<int>::iterator it =
            set_intersection (round1.begin(), round1.end(), round2.begin(), round2.end(), v.begin());
        v.resize(it-v.begin());
        int n = (int)v.size();
        if (n == 1){
            cout << "Case #" << i << ": " << v[0] << endl;
        }
        else if (n > 1){
            cout << "Case #" << i << ": " << "Bad magician!" << endl;
        }
        else {
            cout << "Case #" << i << ": " << "Volunteer cheated!" << endl;

        }
        
    }
    return 0;
}

