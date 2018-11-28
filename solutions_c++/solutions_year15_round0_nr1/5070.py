//
//  main.cpp
//  Standing Ovation
//
//  Created by Daniel Hussey on 11/04/2015.
//  Copyright (c) 2015 Daniel Hussey. All rights reserved.
//
/*
 Input
 
 The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line with Smax, the maximum shyness level of the shyest person in the audience, followed by a string of Smax + 1 single digits. The kth digit of this string (counting starting from 0) represents how many people in the audience have shyness level k. For example, the string "409" would mean that there were four audience members with Si = 0 and nine audience members with Si = 2 (and none with Si = 1 or any other value). Note that there will initially always be between 0 and 9 people with each shyness level.
 
 The string will never end in a 0. Note that this implies that there will always be at least one person in the audience.
 
 Output
 
 For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the minimum number of friends you must invite.
 */

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;

int minimumFriends (int sMax, string shyLevels) {
    int standingCount = 0;
    int invitedCount = 0;
    
    for (int i=0; i<=sMax; i++) {
        if (i>standingCount and (shyLevels[i] - '0')>0) { //Shyness is higher than people currently standing. Invite more until i=standing
            int standingDeficit = i - standingCount; //Will be at least 1
            invitedCount += standingDeficit; //Invite minimum no friends required to get current s level to stand
            standingCount += invitedCount; //Add invited people to number standing, which should make it equal to current shyness level
        }
        
        if (i<=standingCount) { //After inviting more people, there should be enough to add current shynes peoples to standingCount now
            int newStanders = shyLevels[i] - '0';
#warning check this shit ^
            standingCount += newStanders;
        }
    }
    
    return invitedCount;
}

int main(int argc, const char * argv[]) {
    std::ifstream ifile("input.txt");
    std::ofstream ofile("output.txt");
    
    if (ifile.is_open()) {
        std::string input;
        getline(ifile, input);
        int T = atoi(input.c_str());
        
        for(int i=1; i<=T; i++) {
            //Line is now: Smax SiSiSiSi
            getline(ifile, input, ' '); //Will get Smax
            int sMax = atoi(input.c_str());
            getline(ifile, input);
            string shyLevelsString = input;
#warning check ^
            int invitedCount = minimumFriends(sMax, shyLevelsString);
            
            stringstream ss;
            ss << "Case #" << i << ": " << invitedCount;
            
            if (ofile.is_open()) {
                ofile << ss.str() << "\n";
            }
            else {
                cout << "Error: ofile not open.";
            }
        }
    }
    else cout << "Error: Input ifile not open.";
    
    ifile.close();
    ofile.close();
    
    return 0;
}
