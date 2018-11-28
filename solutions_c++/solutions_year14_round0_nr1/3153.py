//
//  main.cpp
//  Magic Trick
//
//  Created by Ignas Kancleris on 2014-04-12.
//  Copyright (c) 2014 Ignas Kancleris. All rights reserved.
//

#include <iostream>
#include <algorithm>

using namespace std;

int eilute[6], t, k, n, c;

int main()
{
    cin >> t;
    for (int i = 0; i < t; i++, n = 0, c = 0) {
        cin >> k;
        for (int i = 0; i < 16; i++) {
            cin >> eilute[((i/4==k-1)?i%4:4)];
        }
        cin >> k;
        for (int i = 0; i < 16; i++) {
            cin >> eilute[5];
            c += (find(eilute, eilute+4, eilute[5]) != eilute+4) && (i/4 == k-1);
            
            n = ((find(eilute, eilute+4, eilute[5]) != eilute+4) && (i/4 == k-1))?eilute[5]:n;
        }
        cout << "Case #" << i+1 << ": " << (c?(c == 1? to_string(n) : "Bad magician!"): "Volunteer cheated!") << endl;
    }
    return 0;
}

