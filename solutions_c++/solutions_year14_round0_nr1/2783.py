//
//  main.cpp
//  magictrick
//
//  Created by Harshit Singh on 12/04/14.
//  Copyright (c) 2014 Harshit Singh. All rights reserved.
//

#include <iostream>
#include <stdio.h>
#include<string.h>
#include <fstream>
using namespace std;
int main(int argc, const char * argv[])
{
    int t,j;
    int arr[4][4];
    int arr1[30];
    int i,row,count,ans,k;
    
    ifstream myReadFile;
    myReadFile.open("A-small-attempt2.in");
    if (myReadFile.is_open()) {
    myReadFile>>t;
        for(k=1;k<=t;k++)
    {
        
        count=0;
        ans=0;
        
        for(i=0;i<30;i++)
            arr1[i]=0;
        
        myReadFile>>row;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                myReadFile>>arr[i][j];
                if((i+1)==row)
                {arr1[arr[i][j]]=1;}
                    
            }
        }
        myReadFile>>row;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                myReadFile>>arr[i][j];
                if((i+1)==row)
                    if(arr1[arr[i][j]]==1)
                    { count++;ans=arr[i][j];}
                
            }
        }
        ofstream myfile;
        
        if(count==0){myfile.open ("output19.txt",std::fstream::out | std::fstream::app);
            myfile<<"Case #"<<k<<": Volunteer cheated!"<<endl;
            myfile.close();}
        else if(count==1)
            {myfile.open ("output19.txt",std::fstream::out | std::fstream::app);
            myfile<<"Case #"<<k<<": "<<ans<<endl;
                myfile.close();}
        else{myfile.open ("output19.txt",std::fstream::out | std::fstream::app);
            myfile<<"Case #"<<k<<": Bad magician!"<<endl;
             myfile.close();}
        
    }
    }
    else
    {
        cout<<"error";
    }
    return 0;
}

