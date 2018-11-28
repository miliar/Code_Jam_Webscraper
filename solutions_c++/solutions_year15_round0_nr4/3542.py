//
//  main.cpp
//  Ominous_Omino
//
//  Created by Zsuzsanna Sas  on 2015.04.11..
//  Copyright (c) 2015 andras1999. All rights reserved.
//

#include <iostream>

using namespace std;

int main(int argc, const char * argv[])
{
    int numOfTests;
    bool ret_val[numOfTests];
    int x[numOfTests], r[numOfTests], c[numOfTests];

    //true: KI LEHET MINDENKÉPPEN RAKNI, TEHÁT GABRIEL NYERT

    cin>>numOfTests;

    for(int i=1;i<=numOfTests;i++){

        cin>>x[i-1]>>r[i-1]>>c[i-1];



        if(x[i-1]==1)ret_val[i-1]=true;

        else if(x[i-1]==2){
            if((r[i-1]*c[i-1])%2==0)ret_val[i-1]=true;
            else ret_val[i-1]=false;

        }



        else if(x[i-1]==3){
            if((r[i-1]*c[i-1])%3==0 && r[i-1]*c[i-1]>=6)ret_val[i-1]=true;
            else ret_val[i-1]=false;

        }


else if(x[i-1]==4)
{

    if(r[i-1]*c[i-1]>=12 && (c[i-1]*r[i-1])%4==0)ret_val[i-1]=true;
    else ret_val[i-1]=false;


    }

    }

    string str;
    for(int i=1;i<=numOfTests;i++){
        if(ret_val[i-1])str="GABRIEL";
        else str="RICHARD";



    cout<<"Case #"<<i<<": "<<str<<endl;


    }


    return 0;
}

