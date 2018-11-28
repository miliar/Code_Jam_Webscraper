//
//  main.cpp
//  standing_ovation
//
//  Created by Zsuzsanna Sas  on 2015.04.11..
//  Copyright (c) 2015 andras1999. All rights reserved.
//

#include <iostream>
using namespace std;

int main(int argc, const char * argv[])
{


    int numOfTests;
    cin>>numOfTests;
    int ret_val[numOfTests];



    for (int i=1; i<=numOfTests; i++) {
        ret_val[i-1]=0;
        int num;


        cin>>num;



        int e[num+1];


        int standing=0;
        string curStr="";

        cin>>curStr;



        for(int j=0;j<=num;j++){

            e[j]=curStr[j]-48;

            if(j<=standing)standing+=e[j];

            else {ret_val[i-1]++; standing++; j--;}


        }



    }

    for(int i=0;i<=numOfTests-1;i++)
    cout<<"Case #"<<i+1<<": "<<ret_val[i]<<endl;
    return 0;
}

