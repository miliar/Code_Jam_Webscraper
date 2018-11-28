//
//  main.cpp
//  Code Jam 2016
//
//  Created by Cody Weber on 4/9/16.
//  Copyright © 2016 Cody. All rights reserved.
//

#include <iostream>
#include <vector>
#include <fstream>

int main(int argc, const char * argv[]) {
    
    std::ofstream fout;
    fout.open("codejam.txt",  std::ios::app);
    
    
    std::ifstream fin;
    fin.open("A-large.in");
    
    typedef std::vector<int> vec;
    
    int T = 0;
    fin >> T;
    
    int n = 0;
    
    for (int x=0; x < T; ++x) {
        fin >> n;
        
        if (n == 0) {
            fout << "Case #" << x + 1 << ": " << "INSOMNIA" << '\n';
            continue;
        }
        
        vec array(0);
        
        for(int i=0; i<10; ++i) {
            array.push_back(i);
        }
        
        int multiple = 1;
        int number;
        
        while (array.size() > 0) {
            
            number = n * multiple;
    
            while (number > 0) {
                int digit = number%10;
                number /= 10;
                
                if(std::find(array.begin(), array.end(), digit) != array.end()) {
                    array.erase(std::remove(array.begin(), array.end(), digit), array.end());
                }
            }
            
            if (array.size() != 0) {
                ++multiple;
            }
        }
        
        
        fout << "Case #" << x + 1 << ": " << n * multiple;
        fout << '\n';
        
    }
    
    fout.close();
    
    return 0;
}
