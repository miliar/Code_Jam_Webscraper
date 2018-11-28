//
//  main.cpp
//  StandingOvation
//
//  Created by Sneha Rishi on 4/10/15.
//  Copyright (c) 2015 Bikram Singh. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
using namespace std;
int main(int argc, const char * argv[]) {
    ifstream inFile;
    ofstream outFile;
    inFile.open("Small.txt");
    outFile.open("SmallAnswer.txt");
    //Check for error
    if(inFile.fail())
    {
        cerr << "File not found" << endl;
        exit(1);
    }
    string item ="";
    string totalcases;
    
    getline(inFile, totalcases);
    int tc = 0;
    stringstream(totalcases) >> tc;
    //cout<<tc<<endl;
    for(int i=0;i<tc;i++)
    {
        //cout << "Case #" << i+1<<":";
        getline(inFile, item);
        stringstream ss(item);
        //cout<<item<<endl;
        size_t pos = item.find(" ");
        string str1 = item.substr (0,pos);
        string str2 = item.substr (pos+1,item.length());
        int Smax ;
        stringstream(str1)>>Smax;
        
        //cout<<Smax<<" "<<str2<<endl;
        long long total=0;
        int Pcount = 0;
        for(int j=0;j<=Smax;j++)
        {
            int Sjint = str2[j] - '0';
            if(j>total && Sjint >0)
            {
                Pcount+=(j-total);
                total = total +Pcount;
            }
            if(total>Smax)
                break;
            
            //cout<<"str2j:"<<str2[j]<<endl;
            //cout<<"Sjint:"<<Sjint<<endl;
            total += Sjint;
            //cout<<"total:"<<total<<endl;

        }
        outFile<<"Case #"<<i+1<<": "<<Pcount<<endl;
    }
    
    inFile.close();
    outFile.close();
    
}

