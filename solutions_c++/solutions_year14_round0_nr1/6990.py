//
//  main.cpp
//  Magic Trick
//
//  Created by Pritam Khan on 12/04/14.
//  Copyright (c) 2014 PK. All rights reserved.
//
#include <fstream>
#include <stdlib.h>
using namespace std;
int main(int argc,char* argv[])
{
    ifstream in;
    ofstream out;
    in.open(argv[1]);
    out.open("ans.out");
    int test;
    in>>test;
    for(int m=1;m<=test;m++)
    {
        int row1,row2,temp = 0,t_a[4],t_b[4];
        in>>row1;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(i==row1-1)
                    in >> t_a[j];
                else
                    in>> temp;
            }
        }
        in>>row2;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                
                if(i==row2-1)
                    in>>t_b[j];
                else
                    in>>temp;
            }
        }
        int count=0;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
                if(t_a[i]==t_b[j])
                {
                    temp=i;
                    count++;
                }
        }
        switch (count) {
            case 0:
                out<<"Case #"<<m<<": Volunteer cheated!"<<endl;
                break;
            case 1:
                out<<"Case #"<<m<<": "<<t_a[temp]<<endl;
                break;
            default:
                out<<"Case #"<<m<<": Bad magician!"<<endl;
                break;
        }
    }
    in.close();
    out.close();
    return 0;
}