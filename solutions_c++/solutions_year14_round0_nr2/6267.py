//
//  Template.cpp
//  CodeJam2014
//
//  Created by Ryan Wilson on 2014-04-11.
//  Copyright (c) 2014 Ryan Wilson. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <iomanip>

const std::string fileName = "/Users/ryanwilson/Desktop/CodeJam/B-large.in";
const std::string outFileName = "/Users/ryanwilson/Desktop/CodeJam/output.txt";

int main(int argc, const char * argv[]){
    std::ifstream file(fileName);
    std::ofstream output(outFileName);
    if (!file.is_open() || !output.is_open()){
        std::cout << "Cannot read file, or generate output\n";
        return -1;
    }

    int numCases;
    file >> numCases;
    
    for (int i = 0; i < numCases; ++i){
        double c, f, x;
        file >> c >> f >> x;

        double cps = 2; // cookies per second
        double numSeconds = 0;

        // See how long it'd take to get to the goal with our current cps, or with current + farm
        // If farm is faster, by a farm and do the same until it's not. (x - numCookies) is left
        while (1){
            double currentPace = x / cps;
            
            // With factory has to factor in time to get to the next factory as well!
            double toNextFactory = (c / cps);
            double nextPace = (x / (cps + f)) + toNextFactory;

            if (currentPace >= nextPace){
                // Buy that factory, add the time it'll take to grab it
                numSeconds += toNextFactory;
                cps += f;
            }
            else {
                numSeconds += currentPace;
                break;
            }
        }
        
        output.flags(output.fixed);
        output.precision(7);
        output << "Case #" << i+1 << ": " << numSeconds;
        
        if (i != (numCases - 1)){
            output << "\n";
        }
    }

    file.close();
    output.close();
    
    return 0;
}

