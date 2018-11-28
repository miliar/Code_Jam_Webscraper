//
//  main.cpp
//  CodeJam2014_MagicTrick
//
//  Created by Neurosion on 4/12/14.
//  Copyright (c) 2014 Neurosion Development. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <array>

namespace
{
    std::array<int, 4> get_row(std::ifstream& input, int selection)
    {
        char buffer[20];
        std::array<int, 4> retval;
        for (int j = 1; j <= 4; ++j) {
            if (j == selection) {
                for (int k = 0; k < 4; ++k) {
                    input >> retval[k];
                }
                std::sort(retval.begin(), retval.end());
            }
            input.getline(buffer, 20); // Clear the line
        }
        
        return retval;
    }
}

int main(int argc, const char * argv[])
{
    std::ifstream input("/Users/neurosion/Documents/Projects/CodeJam2014_MagicTrick/A-small-attempt0.in");
    std::ofstream output("/Users/neurosion/Documents/Projects/CodeJam2014_MagicTrick/output.dat");
    
    int test_case_count;
    input >> test_case_count;
    for (int i = 1; i <= test_case_count; ++i) {
        char buffer[20];
        
        int first_answer;
        input >> first_answer;
        input.getline(buffer, 20);
        std::array<int, 4> first_row = get_row(input, first_answer);
        
        int second_answer;
        input >> second_answer;
        input.getline(buffer, 20);
        std::array<int, 4> second_row = get_row(input, second_answer);
        
        output << "Case #" << i << ": ";
        std::array<int, 4> common_answer;
        switch (std::set_intersection(first_row.begin(), first_row.end(), second_row.begin(), second_row.end(), common_answer.begin()) - common_answer.begin()) {
            case 0:
                output << "Volunteer cheated!" << "\n";
                break;
            case 1:
                output << common_answer[0] << "\n";
                break;
            default:
                output << "Bad magician!" << "\n";
        }
    }
    
    input.close();
    output.close();

    return 0;
}

