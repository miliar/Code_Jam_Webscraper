//
//  main.cpp
//  deceitful war
//
//  Created by Harshit Singh on 12/04/14.
//  Copyright (c) 2014 Harshit Singh. All rights reserved.
//

#include <iostream>
#include<iomanip>
#include<string.h>
#include <fstream>
using namespace std;
int main(int argc, const char * argv[])
{
    
    int t,i,j,k;
    int n;
    int war,dwar;
    double naomi[1005],ken[1005],temp;
    ifstream myReadFile;
    myReadFile.open("D-large.in");
    if (myReadFile.is_open()) {
        myReadFile>>t;
        for(i=1;i<=t;i++)
        {
            war=0;dwar=0;
            myReadFile>>n;
            for(j=0;j<n;j++)
                myReadFile>>naomi[j];
            for(j=0;j<n;j++)
                myReadFile>>ken[j];
            sort(naomi,naomi+n);
            sort(ken,ken+n);
            k=0;
            for(j=0;j<n;j++)
            {
                temp=ken[j];
                while(naomi[k]<temp && k<n)
                {
                    k++;
                }
                if(naomi[k]>temp && k<n)
                { k++;
                    dwar++;}
            }
            k=0;
            for(j=0;j<n;j++)
            {
                temp=naomi[j];
                while(ken[k]<temp && k<n)
                {
                    k++;
                }
                if(ken[k]>temp && k<n)
                {k++;
                    war++;}
            }
            
            ofstream myfile;
            myfile.open ("output25.txt",std::fstream::out | std::fstream::app);
            myfile<<"Case #"<<i<<": "<<dwar<<" "<<n-war<<endl;
            myfile.close();
            //Case #1: 0 0
            //cout<<dwar<<" "<<n-war<<endl;
        }
    }
    else
    {
        cout<<"error";
    }
    return 0;
}

