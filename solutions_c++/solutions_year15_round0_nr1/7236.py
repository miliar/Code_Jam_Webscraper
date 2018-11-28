//
//  main.cpp
//  Standing Ovation
//
//  Created by Kyle Sandell on 4/10/15.
//  Copyright (c) 2015 Kyle Sandell. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <stdint.h>
#include <string>
using namespace std;


int rows[1000];
int checksum(int numRows, int prevNumberOfFriends){
    int sum=0;
    sum+=prevNumberOfFriends;
    for(int r=0;r<numRows/*-1*/;r++)
    {
        sum+=rows[r];
    }
    if (numRows>sum) {//there arent enough members to make the audience stand up
        return (numRows-sum);
    }
    return 0;//no friends needed
}


int main(int argc, const char * argv[]) {
    // insert code here...
    //read file
    ifstream openFile;
    openFile.open("A-large.in");
    ofstream outfile;
	outfile.open("out.txt");
    string levels="";
    int testCases;
    int sMax;//max shyness level(max array level)
    int friendsNeeded=0;
    int tRows=1;
    openFile>>testCases;
    
    for (int times=1; times<testCases+1; times++) {
        openFile>>sMax;
        openFile>>levels;
        if(sMax==0)
        {
            sMax=1;
            friendsNeeded=0;
        }
        else{
            for(int i=0; i<=sMax;i++)
            {
				//cout<<levels[i]<<endl;
                rows[i]=(levels[i]-48);
				
            }
        
			for (int sumRows=1; sumRows<=sMax; sumRows++) {
				friendsNeeded+=checksum(sumRows, friendsNeeded);
            }
        }
        outfile<<"Case #"<<times<<": "<<friendsNeeded<<endl;
        cout<<"Case #"<<times<<": "<<friendsNeeded<<endl;
        sMax=0;
        friendsNeeded=0;
        memset(rows, 0, 1000);
    }
    return 0;
}