//
//  main.cpp
//  googleJam
//
//  Created by Nguyen Viet Trung on 3/29/16.
//  Copyright © 2016 Nguyen Viet Trung. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <istream>
#include <string>
#include <sstream>
#include <algorithm>    // std::set_intersection, std::sort
#include <vector>       // std::vector
#include <iomanip>
#include <math.h>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <list>
#include <complex>
#include <stack>
#include <cmath>
#include <iostream>
#include <sstream>
#include <cctype>
#include <cstdlib>
#include <utility>
#include <bitset>
#include <assert.h>
#include <stdio.h>      /* printf, NULL */
#include <stdlib.h>
using namespace std;


//
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
int main(int argc, const char * argv[]) {
    // insert code here...
    ifstream input;
    input.open("input.txt");
    
    ofstream output;
    output.open("output.txt");
    int T;
    input >> T;
    for (int t = 1; t <= T; t++) {
        string S;
        input >> S;
        string result = "";
        int count[100] = {0};
        int countResult[10] = {0};
        for (int i = 0; i < S.length(); i++)
        {
            count[S[i]]++;
        }
        if (count['Z'] > 0)
        {
            int temp = count['Z'];
            count['Z'] -= temp;
            count['E'] -= temp;
            count['R'] -= temp;
            count['O'] -= temp;
            countResult[0] = temp;
        }
        if (count['U'] > 0)
        {
            int temp = count['U'];
            count['F'] -= temp;
            count['O'] -= temp;
            count['U'] -= temp;
            count['R'] -= temp;
            countResult[4] = temp;
        }
        if (count['W'] > 0)
        {
            int temp = count['W'];
            count['T'] -= temp;
            count['W'] -= temp;
            count['O'] -= temp;
            countResult[2] = temp;
        }
        if (count['X'] > 0)
        {
            int temp = count['X'];
            count['S'] -= temp;
            count['I'] -= temp;
            count['X'] -= temp;
            countResult[6] = temp;
        }
        if (count['G'] > 0)
        {
            int temp = count['G'];
            count['E'] -= temp;
            count['I'] -= temp;
            count['G'] -= temp;
            count['H'] -= temp;
            count['T'] -= temp;
            countResult[8] = temp;
        }
        if (count['R'] > 0)
        {
            int temp = count['R'];
            count['T'] -= temp;
            count['H'] -= temp;
            count['R'] -= temp;
            count['E'] -= temp;
            count['E'] -= temp;
            countResult[3] = temp;
        }
        if (count['O'] > 0)
        {
            int temp = count['O'];
            count['O'] -= temp;
            count['N'] -= temp;
            count['E'] -= temp;
            countResult[1] = temp;
        }
        if (count['F'] > 0)
        {
            int temp = count['F'];
            count['F'] -= temp;
            count['I'] -= temp;
            count['V'] -= temp;
            count['E'] -= temp;
            countResult[5] = temp;
        }
        if (count['V'] > 0)
        {
            int temp = count['V'];
            count['S'] -= temp;
            count['E'] -= temp;
            count['V'] -= temp;
            count['E'] -= temp;
            count['N'] -= temp;
            countResult[7] = temp;
        }
        if (count['N'] > 0)
        {
            int temp = count['N'];
            temp  = temp/2;
            count['N'] -= temp;
            count['I'] -= temp;
            count['N'] -= temp;
            count['E'] -= temp;
            countResult[9] = temp;
        }
        for (int i = 0; i < 10; i++)
        {
            for (int j = 0; j < countResult[i]; j++)
            {
                result += to_string(i);
            }
        }
        output << "Case #" << t << ": " << result << endl;
    }
    
    
    input.close();
    return 0;
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
