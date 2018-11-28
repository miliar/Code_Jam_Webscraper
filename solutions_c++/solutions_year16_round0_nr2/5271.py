//
//  main.cpp
//  pancakes
//
//  Created by Eben on 2016/04/09.
//  Copyright © 2016 Eben. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>

using namespace std;
int main() {
    
    ifstream inFile;
    cout << "Give the file name: ";
    string fileName;
    cin >> fileName;
    
    inFile.open(fileName.c_str());
    if (!inFile){
        cout << "file" << fileName << " not found" << endl;
        return 0;
    }
    ofstream outFile("output.txt");
    
    int numberOfCases ;
    inFile >> numberOfCases ;

    
    for (int i = 1; i <=numberOfCases; i++){
        int steps = 0;
        string tempString, finalString;
        inFile >> tempString;
        finalString = tempString;
        cout <<"test"<< tempString << endl;
        int pos = 0,neg = 0;
        
//        for (int i = 0; i<tempString.length(); i++) {
//            if (tempString[i] == '+'){
//                pos += 1;
//            } else {
//                neg += 1;
//            }
//        }
//        if (neg > pos && neg != pos){
//            for (int i = 0; i<tempString.length(); i++) {
//                if (tempString[i] == '+'){
//                    finalString[i] = '-';
//                } else {
//                    finalString[i] = '+';
//                }
//            }
//            steps += 1;
//        }
        tempString = finalString;
        cout << "test" << finalString << endl;
        int found = tempString.find_first_not_of(finalString[0]);

        while (found != std::string::npos){
            for (int i = 0; i < found ; i++){
                if (tempString[i] == '+'){
                    finalString[i] = '-';
                } else {
                    finalString[i] = '+';
                }
            }
            
            tempString = finalString;
            cout << "test" << finalString << endl;
            int tempFound = found;
            found = tempString.find_first_not_of(finalString[0]);
            steps += 1;
           
        }
        pos = 0;
        neg = 0;
        for (int i = 0; i<tempString.length(); i++) {
            if (tempString[i] == '+'){
                pos += 1;
            } else {
                neg += 1;
            }
        }
        if (neg > pos && neg != pos){
            for (int i = 0; i<tempString.length(); i++) {
                if (tempString[i] == '+'){
                    finalString[i] = '-';
                } else {
                    finalString[i] = '+';
                }
            }
            tempString = finalString;
            cout << "test" << finalString << endl;

            steps += 1;
        }

        outFile << "Case #"<< i <<": "<< steps<< endl;
        cout<< "Case #"<< i <<": "<< steps << endl;
    }
    
    
    
    
    
    return 0;
}
