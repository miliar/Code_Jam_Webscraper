//
//  main.cpp
//  Problem_B._Cookie_Clicker_Alpha
//
//  Created by KoRNz on 4/12/2557 BE.
//  Copyright (c) 2557 KoRNz. All rights reserved.
//

#include <iostream>
#include <vector>
#include <sstream>
#include <string>

using namespace std;

double Solve() {
    double c = 0.0, f = 0.0 ,x = 0.0;
    cin >> c; //500
    cin >> f; //4
    cin >> x; //2000
    
    double total = 0.0;
    double buy = 0.0, notBuy = 0.0, run = 2.0;
    
    while (true) {
        buy = x/(run+f);
        notBuy = x/run;
        if(total+(c/run)+buy <  total+notBuy) {
            total += c/run; //wait for buying
            run += f;
        }
        else {
            total += notBuy;
            break;
        }
    }
    
    return total;
};

int main()
{
    //To insert number of testcases
    int n=0;
    cin >> n;
    
    vector<string> print;
    
    //To call Solve method
    double answer = 0.0;
    for (int i=0; i<n; i++) {
        answer = Solve();
        
        int num = i+1;
        ostringstream convert;
        convert << num;
        string sNum = convert.str();
        
        //store answer
        string sAnswer = std::to_string(answer);
        
        //find position of "."
        string::size_type found = sAnswer.find(".");
        
        //substring
        sAnswer = sAnswer.substr(0,found+8);
        
        print.push_back("Case #" + sNum + ": " + sAnswer + "0");

    }
    
    //to print
    for (int i=0; i<print.size(); i++) {
        cout << print[i] << endl;
    }
    return 0;
}

