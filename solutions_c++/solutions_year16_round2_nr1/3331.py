//
//  main.cpp
//  CodeJamRound1A
//
//  Created by Eben on 2016/04/15.
//  Copyright © 2016 Eben. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;
string output = "";
int nine(string &tempString){
    unsigned long foundz9 = tempString.find('N');
    unsigned long founde9 = tempString.find('I');
    long n = count(tempString.begin(), tempString.end(), 'N');
    unsigned long foundo9 = tempString.find('E');
    
    if( founde9 != std::string::npos  && foundo9 != std::string::npos && n >= 2){
        tempString.erase(foundz9 , 1);
        unsigned long founde = tempString.find('I');
        tempString.erase(founde , 1);
        
        unsigned long foundr = tempString.find('N');
        
        tempString.erase(foundr , 1);
        unsigned long foundo = tempString.find('E');
        tempString.erase(foundo , 1);
        output += "9";
        return 9;

     
    }else {
        return -1;
    }

}

int eight(string &tempString){
    unsigned long foundz8 = tempString.find('E');
    unsigned long founde8 = tempString.find('I');
    unsigned long foundr8 = tempString.find('G');
    unsigned long foundo8 = tempString.find('H');
    unsigned long foundp8 = tempString.find('T');
    
    if(foundz8 != std::string::npos && founde8 != std::string::npos && foundr8 != std::string::npos  && foundo8 != std::string::npos&& foundp8 != std::string::npos){

        tempString.erase(foundz8 , 1);
        
        unsigned long founde = tempString.find('I');
        tempString.erase(founde , 1);
        
        unsigned long foundr = tempString.find('G');
        tempString.erase(foundr , 1);
        
        unsigned long foundo = tempString.find('H');
        tempString.erase(foundo , 1);
        unsigned long foundp = tempString.find('T');
        tempString.erase(foundp , 1);
                output += "8";
        return 8;
    }
    else {
        return -1;
    }
    
}
int seven(string &tempString){
    unsigned long foundz7 = tempString.find('S');
    unsigned long foundr7 = tempString.find('V');
    unsigned long foundp7 = tempString.find('N');
    long se = count(tempString.begin(), tempString.end(), 'E');
    
    if(foundz7 != std::string::npos && foundr7 != std::string::npos  && foundp7 != std::string::npos && se >= 2){
        tempString.erase(foundz7 , 1);
        
        unsigned long founde = tempString.find('E');
        tempString.erase(founde , 1);
        
        unsigned long foundr = tempString.find('V');
        tempString.erase(foundr , 1);
        
        unsigned long foundo = tempString.find('E');
        tempString.erase(foundo , 1);
        
        unsigned long foundp = tempString.find('N');
        tempString.erase(foundp , 1);
                output += "7";
        return 7;
    }
    else {
        return -1;
    }

}

int six(string &tempString){
    unsigned long foundz6 = tempString.find('S');
    unsigned long founde6 = tempString.find('I');
    unsigned long foundr6 = tempString.find('X');
    
    
    if(foundz6 != std::string::npos && founde6 != std::string::npos && foundr6 != std::string::npos ){
        tempString.erase(foundz6 , 1);
        
        unsigned long founde = tempString.find('I');
        tempString.erase(founde , 1);
        
        unsigned long foundr = tempString.find('X');
        tempString.erase(foundr , 1);
                output += "6";
        return 6;
    }
    else {
        return -1;
    }

}


int five(string &tempString){
    unsigned long foundz5 = tempString.find('F');
    unsigned long founde5 = tempString.find('I');
    unsigned long foundr5 = tempString.find('V');
    unsigned long foundo5 = tempString.find('E');
    
    if(foundz5 != std::string::npos && founde5 != std::string::npos && foundr5 != std::string::npos && foundo5 != std::string::npos){

        tempString.erase(foundz5 , 1);
        
        unsigned long founde = tempString.find('I');
        tempString.erase(founde , 1);
        
        unsigned long foundr = tempString.find('V');
        tempString.erase(foundr , 1);
        
        unsigned long foundo = tempString.find('E');
        tempString.erase(foundo , 1);
                output += "5";
        return 5;
    }
    else {
        return -1;
    }
    
}

int four(string &tempString){
    unsigned long foundz4 = tempString.find('F');
    unsigned long founde4 = tempString.find('O');
    unsigned long foundr4 = tempString.find('U');
    unsigned long foundo4 = tempString.find('R');
    
    
    if(foundz4 != std::string::npos && founde4 != std::string::npos && foundr4 != std::string::npos && foundo4 != std::string::npos){
        tempString.erase(foundz4 , 1);
        
        unsigned long founde4 = tempString.find('O');
        tempString.erase(founde4 , 1);
        
        unsigned long foundr4 = tempString.find('U');
        tempString.erase(foundr4 , 1);
        
        unsigned long foundo4 = tempString.find('R');
        tempString.erase(foundo4 , 1);
                output += "4";
        return 4;
    }
    else {
        return -1;
    }
    
}
int three(string &tempString){
    unsigned long foundz3 = tempString.find('T');
    unsigned long founde3 = tempString.find('H');
    unsigned long foundr3 = tempString.find('R');
    long e = count(tempString.begin(), tempString.end(), 'E');
    
    if(foundz3 != std::string::npos && founde3 != std::string::npos && foundr3 != std::string::npos && e >= 2){
        tempString.erase(foundz3 , 1);
        unsigned long founde3 = tempString.find('H');
        tempString.erase(founde3 , 1);
        
        unsigned long foundr3 = tempString.find('R');
        tempString.erase(foundr3 , 1);
        
        unsigned long foundo3 = tempString.find('E');
        tempString.erase(foundo3 , 1);
        
        unsigned long foundp3 = tempString.find('E');
        tempString.erase(foundp3 , 1);
                output += "3";
        return 3;
    }
    else {
        return -1;
    }
    
}
int two(string &tempString){
    unsigned long foundz2 = tempString.find('T');
    unsigned long founde2 = tempString.find('W');
    unsigned long foundr2 = tempString.find('O');
    
    
    if(foundz2 != std::string::npos && founde2 != std::string::npos && foundr2 != std::string::npos ){
        tempString.erase(foundz2 , 1);
        
        unsigned long founde2 = tempString.find('W');
        
        tempString.erase(founde2 , 1);
        unsigned long foundr2 = tempString.find('O');
        tempString.erase(foundr2 , 1);
                output += "2";
        return 2;
    }
    else {
        return -1;
    }
    
}

int one(string &tempString){
    unsigned long foundo1 = tempString.find('O');
    unsigned long foundn1 = tempString.find('N');
    unsigned long founde1 = tempString.find('E');
    
    if(foundo1 != std::string::npos && foundn1 != std::string::npos && founde1 != std::string::npos){
        tempString.erase(foundo1 , 1);
        foundn1 = tempString.find('N');
        tempString.erase(foundn1 , 1);
        
        founde1 = tempString.find('E');
        tempString.erase(founde1 , 1);
                output += "1";
        return 1;
    }

    else {
        return -1;
    }
    
}
int zero(string &tempString){
    unsigned long foundz = tempString.find('Z');
    unsigned long founde = tempString.find('E');
    unsigned long foundr = tempString.find('R');
    unsigned long foundo = tempString.find('O');
    
    if(foundz != std::string::npos && founde != std::string::npos && foundr != std::string::npos && foundo != std::string::npos){

        tempString.erase(foundz , 1);
        founde = tempString.find('E');
        tempString.erase(founde , 1);
        foundr = tempString.find('R');
        tempString.erase(foundr , 1);
        foundo = tempString.find('O');
        tempString.erase(foundo , 1);
                output += "0";
        return 0;
    }
    else {
        return -1;
    }
    
}




int main() {
    cout << "start";
    ifstream inFile;
    inFile.open("in1.txt");//fileName.c_str());
    if (!inFile){
        cout << "file" << "in.txt" << " not found" << endl;
        return 0;
    }
    
    int testCases;
    inFile >> testCases;
    ofstream outFile("output1.txt");
    bool notfound = false;
    for (int i = 1; i <= testCases; i++ ){
        string  tempString;
        inFile >> tempString;
        cout << "case : " << i << endl;
        outFile <<"Case #" << i << ": ";
        cout << tempString << endl;
        string copy = tempString;
        
        while (tempString.length() > 0 && !notfound){
            while (zero(tempString)!=-1) {
                
            }
            while (two(tempString)!=-1) {
                
            }
            while (four(tempString)!=-1) {
                
            }
            while (five(tempString)!=-1) {
                
            }
            while (three(tempString)!=-1) {
                
            }
            while (six(tempString)!=-1) {
                
            }
            while (seven(tempString)!=-1) {
                
            }
            while (eight(tempString)!=-1) {
                
            }
            while (nine(tempString)!=-1) {
                
            }
            while (one(tempString)!=-1) {
                
            }
            one(tempString);
            two(tempString) ;
            three(tempString);
            four(tempString);
            five(tempString);
            six(tempString);
            seven(tempString);
            eight(tempString);
            nine(tempString);
            zero(tempString);
            
            
            
            
            
//            if (
//                one(tempString)== -1 &&
//                two(tempString) == -1 &&
//                three(tempString)== -1 &&
//                four(tempString)== -1 &&
//                five(tempString)== -1 &&
//                six(tempString)== -1 &&
//                seven(tempString)== -1 &&
//                eight(tempString)== -1 &&
//                nine(tempString)== -1 &&
//                zero(tempString)== -1){
////                tempString = copy;
////                output = "";
//                if(
//                   
//                zero(tempString)== -1 &&
//                nine(tempString)== -1 &&
//                eight(tempString)== -1 &&
//                seven(tempString)== -1 &&
//                six(tempString)== -1 &&
//                five(tempString)== -1 &&
//                four(tempString)== -1 &&
//                three(tempString)== -1 &&
//                two(tempString) == -1 &&
//                one(tempString)== -1 ){
//                    
//                    three(tempString);
//                    two(tempString);
//                    one(tempString);
//                   }
//                
//            }
//            cout << tempString << endl;
            
        }
        sort(output.begin(), output.end());
        outFile << output;
        cout << output << endl;
        cout << output.length() << endl;

        output = "";
        outFile << endl;
        
    }
    outFile.close();
    inFile.close();
    cout<<"finished";
    return 0;
}
