//
//  main.cpp
//  codeJam2015
//
//  Created by Francesco Infante on 11/04/15.
//  Copyright (c) 2015 Francesco Infante. All rights reserved.
//

#include <fstream>

using namespace std;

int main(int argc, const char * argv[]) {
    ofstream output;
    ifstream input;
    input.open("input.in");
    output.open("output.out");
    
    int t;
    input >> t;
    
    for (int test = 1; test<=t; test++) {
        int size = 0;
        input >> size;
        long long result = 0;
        long long available = 0;
        string s;
        
        input >> s;
        
        for (int i = 0; i<s.length(); i++) {
            int shyPeople = s[i]-'0';
            if (shyPeople == 0) {
                if (available == 0) {
                    result++;
                } else {
                    available--;
                }
            }
            if (shyPeople > 1) {
                available+=shyPeople-1;
            }
        }
        
        output << "Case #" << test << ": " << result << "\n";
    }
    
    
    input.close();
    output.close();
    return 0;
}
