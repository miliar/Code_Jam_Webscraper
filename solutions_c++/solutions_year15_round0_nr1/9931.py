//
//  main.cpp
//  codejam
//
//  Created by Iulian Popescu on 11/04/15.
//  Copyright (c) 2015 Iulian Popescu. All rights reserved.
//

#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <fstream>

using namespace std;


int main(int argc, const char * argv[]) {
    int T, index;
    cin >> T;
    index = 0;
    
    vector<pair<int, int>> solution;
    while (index <T) {
        
        int max_shyness;
        string peoples_shyness;
        cin >> max_shyness >> peoples_shyness;
        
        int number_of_friends = 0, total_peoples = peoples_shyness[0] - '0';
        for (int i = 1; i <= max_shyness; ++i) {
            if (peoples_shyness[i] - '0' != 0) {
                if (i > total_peoples) {
                    number_of_friends += i - total_peoples;
                    total_peoples += number_of_friends + (peoples_shyness[i] - '0');
                } else {
                    total_peoples += (peoples_shyness[i] - '0');
                }
            }
        }
        
        ++index;
        solution.push_back(make_pair(index, number_of_friends));
        cout << "Case #" << index <<": " << number_of_friends << "\n";

    }
    
    string output_file_path = "/Users/iulian_popescu/Desktop/solution1-small";
    ofstream fout(output_file_path);
    for (int i = 0; i < solution.size(); ++i) {
           fout << "Case #" << solution[i].first<<": " << solution[i].second << "\n";
    }
    return 0;
}

