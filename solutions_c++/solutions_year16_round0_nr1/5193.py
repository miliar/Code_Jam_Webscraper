//
//  main.cpp
//  google code jam
//
//  Created by Eben on 2016/04/09.
//  Copyright © 2016 Eben. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <iomanip>
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

    int testCases;
    inFile >> testCases;
    
    ofstream outFile("output.txt");
  
    for (int i = 1; i <= testCases; i++ ){
        
        int givenInput;
        inFile >> givenInput;
        int lastNum = givenInput;
        
        int counter = 1;
        bool zero = 0,one = 0,two = 0,three = 0,four = 0,five = 0,six = 0,seven = 0,eight = 0,nine = 0;
        
        while ( (counter <= 1000000) && (!zero || !one || !two || !three || !four || !five || !six || !seven || !eight || !nine)){
            lastNum = counter * givenInput;
            string tempString = to_string(lastNum);
            cout << zero << one << two << three << four << five << six << seven << eight << nine << endl;
            cout << tempString << endl;
            for (int j = 0; j < tempString.length(); j++){
                switch (tempString[j]) {
                    case '0':
                        zero = true;
                        break;
                    case '1':
                        one = true;
                        break;
                    case '2':
                        two = true;
                        break;
                    case '3':
                        three = true;
                        break;
                    case '4':
                        four = true;
                        break;
                    case '5':
                        five = true;
                        break;
                    case '6':
                        six = true;
                        break;
                    case '7':
                        seven = true;
                        break;
                    case '8':
                        eight = true;
                        break;
                    case '9':
                        nine = true;
                        break;
                    default:
                        break;
                }
                
            }
            
            counter += 1;
        };
        cout << counter;
        if (counter == 1000001){
            outFile <<"Case #" << i << ": " << "INSOMNIA"<< endl;
        }else{
            outFile <<"Case #" << i << ": " << lastNum << endl;
        }
        
        
    };
    
    outFile.close();
    inFile.close();
    cout<<"finished";
    return 0;
}
