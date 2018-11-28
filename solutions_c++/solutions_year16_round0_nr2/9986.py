/*******************************************************************************
    Copyright (C) 2014-2016 Wright State University - All Rights Reserved
    Daniel P. Foose - Maintainer/Lead Developer

    This file is part of Vespucci.

    Vespucci is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Vespucci is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Vespucci.  If not, see <http://www.gnu.org/licenses/>.
*******************************************************************************/
#include <iostream>
#include <fstream>
#include <list>
#include <vector>


using namespace std;

string FlipStack(string stack, uint substack_bottom)
{
    string new_stack = stack;
    for (uint i = 0; i < substack_bottom; ++i){
        if (stack[i] == '-') new_stack[i] = '+';
        if (stack[i] == '+') new_stack[i] = '-';
    }
    return new_stack;
}


int main(int argc, char *argv[])
{
    if (argc != 2)
        return 1;
    string infilename(argv[1]);
    ifstream infile(infilename);
    string current_line;
    std::getline(infile, current_line);
    uint current_line_ind = 1;
    while (std::getline(infile, current_line)){
        uint flip_count = 0;
        for (int i = current_line.size() - 1; i >= 0; --i){
            if (current_line[i] == '-'){
                current_line = FlipStack(current_line, i);
                ++flip_count;
            }
        }
        cout << "Case #" << current_line_ind << ": " << flip_count << endl;
        ++current_line_ind;
    }
    return 0;
}
