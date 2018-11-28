//
//  main.cpp
//  StandingOvation
//
//  Created by Anas Saeed on 11/04/2015.
//  Copyright (c) 2015 Anas Saeed. All rights reserved.
//

#include <iostream>
#include <fstream>
int main(int argc, const char * argv[]) {
    // insert code here...
    std::ifstream reader;
    reader.open("test.txt");
    std::ofstream writer;
    writer.open("output.txt");
    std::string oneline;
    std::getline(reader,oneline);
    int times = atoi(oneline.c_str());
    for (int i = 1; i < times+1; i++) {
        std::getline(reader,oneline);
        int max = 0;
        std::string temp;
        bool whcih  = true;
        for ( auto x: oneline){
            if (x ==' ') {
                max = atoi(temp.c_str());
                temp = "";
                continue;
            }
            temp+=x;
        }
        int array[max];
        for ( auto & x:array){
            x = 0;
        }
        int totalPeople = 0;
        int needed = 0;
        for (int j = 0;j < temp.length();j++){
            if (temp[j] == '0') {
//                std::cout <<"here";
                continue;
            }
            if (totalPeople <j) {
                needed+= (j-totalPeople);
                totalPeople+=(j-totalPeople);
//                std::cout << totalPeople << " " <<temp[j] << " " <<j << " " << needed << "\n";
            }
            std::string temp1 =""+ temp[j];
            totalPeople +=temp[j] -48;
//            std::cout << totalPeople << " "<< temp[j] -48 ;
        }
        writer << "Case #" << i <<": " << needed <<"\n";
        std::cout << "Case #" << i <<": " << needed <<"\n";
    }
//    std::cout << "Hello, World!\n";
    return 0;
}
