//
//  counting_sheep.cpp
//  CodeJam_2016
//
//  Created by Snehil Vishwakarma on 4/8/16.
//  Copyright © 2016 Indiana University Bloomington. All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main()
{
    int T,i,c,g,r;
    long N,S,temp;
    vector<bool> V(10);
    ifstream f1;
    f1.open("IS1_2016.in");
    ofstream f2;
    f2.open("OS1_2016.out");
    f1>>T;
    for(i=0;i<T;i++)
    {
        f1>>N;
        if(N==0)
            f2<<"Case #"<<(i+1)<<": INSOMNIA"<<"\n";
        else
        {
            c=0;
            g=1;
            fill(V.begin(),V.end(),0);
            do
            {
                S=g*N;
                temp=S;
                while(temp>0)
                {
                    r=temp%10;
                    if(V[r]==false)
                    {
                        c++;
                        V[r]=true;
                    }
                    temp=temp/10;
                }
                g++;
            }while (c<10);
            f2<<"Case #"<<(i+1)<<": "<<S<<"\n";
        }
    }
    f1.close();
    f2.close();
    return 0;
}