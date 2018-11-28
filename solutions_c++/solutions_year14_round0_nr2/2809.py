//
//  main.cpp
//  cookieclicker
//
//  Created by Harshit Singh on 12/04/14.
//  Copyright (c) 2014 Harshit Singh. All rights reserved.
//

#include <iostream>
#include<stdio.h>
#include<iomanip>
#include<string.h>
#include <fstream>
using namespace std;
int main(int argc, const char * argv[])
{

    int t,i;
    double c,f,x;
    double t1,t2,l,s1,s2;
    ifstream myReadFile;
    myReadFile.open("B-large.in");
    if (myReadFile.is_open()) {
    myReadFile>>t;
    //cout << fixed << setprecision(2) <<1.2;
    for(i=1;i<=t;i++)
    {
        myReadFile>>c;
        myReadFile>>f;
        myReadFile>>x;
        l=2;s1=0;
        t1=x/2;
        t2=x/2;
        while(t1>=t2)
        {
            t1=t2;
            s1=s1+(c/l);
            l+=f;
            s2=(x/l);
            t2=s1+s2;
        }
        ofstream myfile;
        myfile.open ("output22.txt",std::fstream::out | std::fstream::app);
        myfile<<"Case #"<<i<<": "<<fixed << setprecision(7)<<t1<<endl;
        myfile.close();
       // cout<<"Case #"<<i<<": "<<fixed << setprecision(7)<<t1<<endl;
    }
    }
    else
    {
        cout<<"error";
    }
    return 0;
}

