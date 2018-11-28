//
//  main.cpp
//  Deceitful War
//
//  Created by Ignas Kancleris on 2014-04-12.
//  Copyright (c) 2014 Ignas Kancleris. All rights reserved.
//

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, const char * argv[])
{

    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        int n;
        cin >> n;
        vector<double> naomi(n,0), ken(n,0);
        for (int i = 0; i < n; i++) {
            cin >> naomi[i];
        }
        for (int i = 0; i < n; i++) {
            cin >> ken[i];
        }
        sort(naomi.begin(), naomi.end());
        sort(ken.begin(), ken.end());
        cout << "Case #" << i+1 << ": ";
        int wins = 0;
        int min = 0;
        for (int j = 0; j < n; j++) {
            if (naomi[j] > ken[min]) {
                min++;
                wins++;
                continue;
            }
            if (naomi[j] > ken[n-j+min-1]) {
                wins++;
            }
        }
        cout << wins << " ";
        wins = 0;
        for (int j = 0; j < n; j++) {
            vector<double>::iterator it = upper_bound(ken.begin(), ken.end(), naomi[j]);
            if (it == ken.end()) {
                ken.erase(ken.begin());
                wins++;
            }else{
                ken.erase(it);
            }
        }
        cout << wins << endl;
        
    }
    
    return 0;
}

