//
//  main.cpp
//  Infinite House of Pancakes
//
//  Created by Daniel Hussey on 11/04/2015.
//  Copyright (c) 2015 Daniel Hussey. All rights reserved.
//

#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>

using namespace std;

int bestMinutes (vector<int> pancakes) {
    
    int minTime, time, maxStack = 0;
    
    std::sort(pancakes.begin(), pancakes.end());
    auto it = max_element(pancakes.begin(), pancakes.end());
    maxStack = *it;
    minTime = maxStack; //
    
    for( ; maxStack > 1 ; maxStack--){
        time = maxStack;
        for (int i=0; i<pancakes.size(); i++){
            time+=((pancakes[i]-1)/ maxStack);
        }
        if (time<minTime)
            minTime = time;
    }
    return minTime;
}

int main(int argc, const char * argv[]) {
    ifstream ifile("B-large.in");
    ofstream ofile("bigOutput.txt");
    string input;
    
    if (ifile.is_open()) {
        getline(ifile, input);
        int T = atoi(input.c_str());
        for (int i=1; i<=T; i++) {
            vector<int> pancakes;
            getline(ifile, input);
            int D = atoi(input.c_str());
            
            stringstream parser;
            string token;
            
            getline(ifile, input);
            parser << input;
            while (getline(parser, token, ' ') )
            {
                int P = atoi(token.c_str());
                pancakes.push_back(P);
            }
            parser.clear();
            
            //should have full pancakes vector now
            int mins = bestMinutes(pancakes);
            
            stringstream ss;
            ss << "Case #" << i << ": " << mins;
            
            if (ofile.is_open()) {
                ofile << ss.str() << "\n";
            }
            else {
                cout << "Error: ofile not open.";
            }
            ss.clear();
            pancakes.clear();
        }
    }
    
    ifile.close();
    ofile.close();
    return 0;
}