//
//  main.cpp
//  GoogleCodeJamCpp
//
//  Created by Mo-kun on 4/11/15.
//  Copyright (c) 2015 Mohammad Al-Kamel. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, const char * argv[]) {
    
    ifstream file;
    file.open ("A-large.in.txt");
    ofstream outFile ("ALarge.out.txt");
    
    if(file.is_open()){
        
        int tries, maxShy;
        string s;
        file >> tries;
        int x = 1;
        while (x <= tries) {
            
            file >> maxShy;
            file >> s;
            
            if (maxShy == 0) {
                outFile << "Case #" << x <<": 0\n";
                x++;
                continue;
            }
            
            int a, peopleAlreadyThere = 0, peopleToCome = 0, totalPeople = peopleToCome + peopleAlreadyThere;
            
            for (int i = 0; i <= s.length() - 1; i++) {
                
                
                a = (int)s[i] % 48;
                
                if (peopleToCome >= maxShy || totalPeople >= maxShy) {
                    break;
                }
                
                if (i == 0 && a == 0){
                    peopleToCome++;
                }
                
                totalPeople = peopleAlreadyThere + peopleToCome;
                
                if ( a > 0 ){
                    if (totalPeople < i){
                        peopleToCome += i - totalPeople;
                    }
                }
                
                peopleAlreadyThere += a;
            }
            
            if (peopleToCome > 0) {
                outFile << "Case #" << x <<": " << peopleToCome << "\n";
            } else {
                outFile << "Case #" << x <<": 0\n";
            }
            x++;
            
        }
    } else {
        cout << "Error";
    }
    
    
    
    return 0;
}
