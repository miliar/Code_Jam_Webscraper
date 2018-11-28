//
//  main.cpp
//  jam
//
//  Created by mac  on 14-4-12.
//  Copyright (c) 2014年 mac . All rights reserved.
//

#include <iostream>
#include "vector"
#include<fstream>
#include <iomanip>
using namespace std;


int main()
{

    ifstream fin("input.txt");
    ofstream fout("output.txt");
	int t;
	fin >> t;
	while (t--) {
        
        double c, f, x;
        fin >> c >> f >> x;
        int buynum = 0;
        vector<double> time;
        time.push_back(c/2);
        while (x / (f * (buynum+1) + 2) < (x - c)/(f * buynum + 2)) {

            buynum++;
            time.push_back(c/ (f * buynum + 2));

            
        }
        time.push_back((x - c)/(f * buynum + 2));
        double total = 0;
        for (int i = 0; i < (int)time.size(); i++) {
            total = total + time[i];
        }
        
        
        static int id = 0;

            fout << "Case #"<< ++id<<": "<<setprecision(10)<< total<<endl;
    }
    
    return 0;
}

