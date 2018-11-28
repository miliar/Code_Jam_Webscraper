//
//  main.cpp
//  GoogleCodeJam2015
//
//  Created by Mats Uytterhoeven on 11/04/15.
//  Copyright (c) 2015 Mats Uytterhoeven. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, const char *argv[]) {
    string input = "A-large.in.txt";
    
    ifstream ifstr (input, ios::in);
    ofstream ofstr ("output-large.txt", ios::out);
    
    int nr_of_cases;
    ifstr >> nr_of_cases;
    
    for (int i = 1; i <= nr_of_cases; ++i) {
        int max_shyness;
        ifstr >> max_shyness;
        
        string temp;
        ifstr >> temp;
        
        int total = 0;
        int nr_of_friends_needed = 0;
        
        // Need at least one person with 0 shyness to get it all started
        if (temp[0] - '0' == 0) {
            nr_of_friends_needed++;
            total += 1;
        }
        
        total += temp[0] - '0';
        
        for (int j = 1; j <= max_shyness; ++j) {
            int nr_of_people = temp[j] - '0';
            
            if (nr_of_people != 0 && total < j) {
                nr_of_friends_needed += j - total;
                total += j - total;
            }
            
            total += nr_of_people;
        }
        
        ofstr << "Case #" << i << ": " << nr_of_friends_needed << endl;
        
    }
    
    ifstr.close();
    ofstr.close();
    
    return 0;
}


