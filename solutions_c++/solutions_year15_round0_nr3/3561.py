//
//  main.cpp
//  exa
//
//  Created by Mr.Note on 4/11/15.
//  Copyright (c) 2015 Mr.Note. All rights reserved.
//

#include <fstream>
#include <string>
#include <map>
#include <iostream>
using namespace std;




int main(int argc, const char * argv[])
{
    
    ifstream in;
    ofstream out;
    in.open("C-small-attempt2.in");
    out.open("output.txt");
    
    map<char,int> goo;
    char any[4][4];
    int teemp[4][4];
    int quan;
    unsigned long idk,yrh;
    string st;
    int a1,a2,a3,a4,cas=1;
    char az;

    
    teemp[3][0]=1;
    any[0][0]='1';
    teemp[0][0]=1;
    goo['1']=0;
    any[0][1]='i';
    teemp[0][1]=1;
    goo['i']=1;
    any[0][2]='j';
    teemp[0][2]=1;
    goo['j']=2;
    any[0][3]='k';
    teemp[0][3]=1;
    goo['k']=3;
    any[1][0]='i';
    teemp[1][0]=1;
    any[1][1]='1';
    teemp[1][1]=-1;
    any[1][2]='k';
    teemp[1][3]=-1;
    any[1][3]='j';
    teemp[1][2]=1;
    any[2][0]='j';
    teemp[2][0]=1;
    any[2][1]='k';
    teemp[2][1]=-1;
    any[2][2]='1';
    teemp[2][3]=1;
    any[2][3]='i';
    any[3][0]='k';
    teemp[3][1]=1;
    any[3][1]='j';
    teemp[3][2]=-1;
    any[3][2]='i';
    teemp[3][3]=-1;
    any[3][3]='1';
    teemp[2][2]=-1;
    
    
    
    in>>quan;
    
    
    while(cas<=quan)
    {
         a1=1;
         a2 = 1;
        a3 = 0;
        a4=0;
        in>>idk>>yrh;
        in>>st;
        
        
        
        for(;a4<yrh;a4++)
        {
            for(int al=0;al<st.size();al++)
            {
                az=any[a3][goo[st[al]]];
                a1*=teemp[a3][goo[st[al]]];
                if(goo[az]== a2)
                {
                    a2++;
                    az='1';
                }
                a3=goo[az];
            }
            
        }
        
        if(a2 == 4 && a1==1 &&az=='1'  )
            out<<"Case #"<<cas<<": YES"<<endl;
        else
            out<<"Case #"<<cas<<": NO"<<endl;
        cas++;
    }

    
    
    
        return 0;
}

